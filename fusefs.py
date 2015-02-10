#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import atexit, os, sys, warnings

import llfuse
import errno
import stat
import os.path as path
from time import time
import sqlite3
import logging
from collections import defaultdict
from llfuse import FUSEError

from eventlet.pools import Pool
import itertools

from util import hasValidStatus, timed

log = logging.getLogger()

# For Python 2 + 3 compatibility
if sys.version_info[0] == 2:
    def next(it):
        return it.next()
else:
    buffer = memoryview

current_uid = os.getuid()
current_gid = os.getgid()

ino_source = itertools.count(1)
ino_pool = Pool(create=lambda: next(ino_source), max_size=2**30)

class INode(object):
    MODE_0755 = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH
    MODE_0777 = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH

    def __init__(self):
        super(INode, self).__init__()
        self.ino = ino_pool.get()

    def __del__(self):
        ino_pool.put(self.ino)

    def attr(self):
        entry = llfuse.EntryAttributes()
        entry.st_ino = self.ino
        entry.generation = 0
        entry.entry_timeout = 0.2
        entry.attr_timeout = 10
        entry.st_mode = self.MODE_0755
        entry.st_nlink = 1
        entry.st_uid = current_uid
        entry.st_gid = current_gid
        entry.st_rdev = 1
        entry.st_size = 0

        entry.st_blksize = 512
        entry.st_blocks = 1
        now = time()
        entry.st_atime = now
        entry.st_mtime = now
        entry.st_ctime = now

        return entry

import db, config
config = config.read()
DB=db.open(config.get('DB', 'file'))
fields=set((u'directory', u'name', u'ext', u'xt', u'bh_status', u'bh_status_confirmed', u'filesize'))
def scan(directory_obj):
    dir_prefix = directory_obj.id+'/'
    for obj in DB.query({u'directory': db.Starts(dir_prefix)}, fields=fields):
        name_found = 0
        for directory in obj['directory']:
            if directory.startswith(dir_prefix):
                name = directory[len(dir_prefix):]
                if name:
                    name_found += 1
                    yield name, obj

        if not name_found and obj.any('name'):
            name = obj.any('name')
            ext = obj.any('ext')
            if ext:
                if ext.startswith('.'):
                    name += ext
                else:
                    name += ".%s" % obj.any('ext')
            yield name, obj

def is_available(obj):
    if hasValidStatus(obj):
        return True
    if obj.any('xt'):
        return False
    # It SHOULD now be a directory of unknown status
    return any(is_available(obj) for _, obj in scan(obj))

class File(INode):
    def __init__(self, obj):
        super(File, self).__init__()
        self.obj = obj

    def attr(self):
        entry = super(File, self).attr()
        entry.st_mode |= stat.S_IFREG
        return entry

    def is_available(self):
        return is_available(self.obj)

class Symlink(INode):
    def __init__(self, obj):
        super(Symlink, self).__init__()
        self.obj = obj

    def attr(self):
        entry = super(Symlink, self).attr()
        entry.st_mode |= stat.S_IFLNK
        return entry

    def readlink(self):
        return (u"/tmp/bhfuse/magnet:?xt=urn:" + self.obj.any('xt')).encode('utf8')

    def is_available(self):
        return hasValidStatus(self.obj)

class Directory(INode):
    def __init__(self, obj):
        super(Directory, self).__init__()
        self.obj = obj

    def attr(self):
        entry = super(Directory, self).attr()
        entry.st_mode |= stat.S_IFDIR
        entry.st_nlink = 2
        return entry

    def is_available(self):
        return is_available(self.obj)

    def lookup(self, name):
        results = DB.query({u'directory': u'%s/%s' % (self.obj.id, name)}, fields=fields)
        try:
            obj = next(results)
        except StopIteration:
            raise(llfuse.FUSEError(errno.ENOENT))

        if obj.any('xt'):
            return File(obj)
        else:
            return Directory(obj)

    def readdir(self):
        for name, obj in scan(self.obj):
            if not is_available(obj):
                continue

            if obj.any('xt'):
                inode = File(obj)
            else:
                inode = Directory(obj)

            yield name, inode

class Operations(llfuse.Operations):
    def __init__(self):
        super(Operations, self).__init__()
        self.root = Directory(DB['dir:'])
        self.inode_open_count = defaultdict(int)

        self.inodes = {
            llfuse.ROOT_INODE: self.root
        }

    def _inode_resolve(self, ino, cls=INode):
        try:
            inode = self.inodes[ino]
            assert isinstance(inode, cls)
            return inode
        except KeyError:
            raise(llfuse.FUSEError(errno.ENOENT))

    @timed
    def lookup(self, inode_p, name):
        inode_p = self._inode_resolve(inode_p, Directory)
        inode = inode_p.lookup(name.decode('utf-8'))
        self.inodes[inode.ino] = inode
        return inode.attr()

    def forget(self, inodes):
        # Assuming the kernel only notifies when nlookup really reaches 0
        for ino, nlookup in inodes:
            try:
                del self.inodes[ino]
            except:
                warnings.warn('Tried to forget something already missing.')

    def getattr(self, inode):
        inode = self._inode_resolve(inode)
        return inode.attr()

    def opendir(self, inode):
        inode = self._inode_resolve(inode, Directory)
        return inode.ino

    @timed
    def readdir(self, inode, off):
        if off:
            return

        directory = self._inode_resolve(inode, Directory)

        i = 1
        for name, inode in directory.readdir():
            #self.inodes[inode.ino] = inode
            yield name.encode('utf8'), inode.attr(), i
            i += 1

    def releasedir(self, inode):
        pass

    def readlink(self, inode):
        return self._inode_resolve(inode, Symlink).readlink()

def init_logging():
    formatter = logging.Formatter('%(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

if __name__ == '__main__':
    init_logging()
    try:
        self, mountpoint = sys.argv
    except:
        raise SystemExit('Usage: %s <mountpoint>' % sys.argv[0])

    operations = Operations()

    mount_point_created = None
    if not os.path.exists(mountpoint):
        os.mkdir(mountpoint)
        mount_point_created = mountpoint

    llfuse.init(operations, mountpoint,
                [  'fsname=bhindex', 'nonempty', 'debug', 'default_permissions' ])

    def cleanup(llfuse, remove_mountpoint):
        llfuse.close()
        if remove_mountpoint:
            os.rmdir(remove_mountpoint)

    atexit.register(cleanup, llfuse, mount_point_created)

    try:
        llfuse.main(single=False)
    except:
        log.warn("Error!")
        raise
