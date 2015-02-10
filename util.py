import codecs, logging, sys
from base64 import urlsafe_b64encode as b64encode
from uuid import uuid4
from time import time

import eventlet
from bithorde import parseHashIds, message
from db import ValueSet

if not sys.stdout.encoding:
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
if not sys.stderr.encoding:
    sys.stderr = codecs.getwriter('utf8')(sys.stderr)

class DelayedAction(object):
    def __init__(self, action):
        self.action = action
        self._scheduled = None

    def schedule(self, delay):
        if self._scheduled is None:
            self._scheduled = eventlet.spawn_after(delay, self._fire)

    def _fire(self):
        self._scheduled = None
        self.action()

ASSET_WAIT_FACTOR = 0.01
def hasValidStatus(dbAsset, t=time()):
    try:
        dbStatus = dbAsset['bh_status']
        dbConfirmedStatus = dbAsset['bh_status_confirmed']
    except KeyError:
        return None
    stable = dbConfirmedStatus.t - dbStatus.t
    nextCheck = dbConfirmedStatus.t + (stable * ASSET_WAIT_FACTOR)
    if t < nextCheck:
        return dbStatus.any() == 'True'
    else:
        return None

def cachedAssetLiveChecker(bithorde, assets, db=None):
    t = time()
    dirty = Counter()
    if db:
        commit_pending = DelayedAction(db.commit)

    def checkAsset(dbAsset):
        dbStatus = hasValidStatus(dbAsset, t)
        if dbStatus is not None:
            eventlet.sleep() # Not sleeping here could starve other greenlets
            return dbAsset, dbStatus

        ids = parseHashIds(dbAsset['xt'])
        if not ids:
            return dbAsset, None

        with bithorde.open(ids) as bhAsset:
            status = bhAsset.status()
            status_ok = status and status.status == message.SUCCESS
            dbAsset[u'bh_status'] = ValueSet((unicode(status_ok),), t=t)
            dbAsset[u'bh_status_confirmed'] = ValueSet((unicode(t),), t=t)
            if status and (status.size is not None):
                if status.size > 2**40:
                    print dbAsset['xt']
                    print status.size
                dbAsset[u'filesize'] = ValueSet((unicode(status.size),), t=t)
            if db:
                db.update(dbAsset)
                commit_pending.schedule(2)

            return dbAsset, status_ok

    return bithorde.pool().imap(checkAsset, assets)

class Counter(object):
    def __init__(self):
        self.i = 0

    def reset(self):
        self.i = 0

    def inc(self, i = 1):
        self.i += i
        return self.i

    def __int__(self):
        return self.i

    def inGibi(self):
        return self.i / (1024*1024*1024.0)

class Progress(Counter):
    def __init__(self, total, unit=''):
        Counter.__init__(self)
        self.total = total
        self.printer = eventlet.spawn(self.run)
        self.unit = unit

    def run(self):
        start_time = last_time = time()
        last_processed = int(self)
        while int(self) < self.total:
            eventlet.sleep(1)
            current_time = time()
            time_diff = time()-last_time
            processed_diff = int(self) - last_processed
            print "\rProcessed: %d/%d%s (%d/sec)" % (self, self.total, self.unit, processed_diff/time_diff),
            sys.stdout.flush()
            last_time = current_time
            last_processed = int(self)
        time_diff = time()-start_time
        print "\rProcessed: %d/%d%s (%d/sec)" % (self, self.total, self.unit, self.total/time_diff)

    def wait(self):
        return self.printer.wait()

def get_folder_id(db, parent_id, name, t):
    directory_attr = u'%s/%s' % (parent_id, name)
    folders = list(db.query_ids({u'directory': directory_attr}))
    if folders:
        if len(folders) > 1:
            logging.basicConfig()
            log = logging.getLogger('util')
            log.warning("Duplicate folders for %s: %r", directory_attr, folders)
        return folders[0]
    else:
        folder_id = u'dir:%s' % b64encode(uuid4().bytes).strip('=')
        folder = db[folder_id]
        folder[u'directory'] = ValueSet((directory_attr,), t=t)
        db.update(folder)
        return folder_id

def make_directory(db, directory, t):
    dir_id = u"dir:"
    for segment in directory:
        dir_id = get_folder_id(db, dir_id, segment, t)
    return dir_id


class Timed:
    def __init__(self, tag):
        self.tag = tag
        self.log = logging.getLogger('timed')

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, type, value, traceback):
        delta = (time() - self.start) * 1000
        self.log.debug("<%s>: %.1fms" % (self.tag, delta))

def timed(method):
    def timed(*args, **kw):
        with Timed("%r (%r, %r)" % (method.__name__, args, kw)):
            res = method(*args, **kw)
            if isinstance(res, GeneratorType):
                return list(res)
            else:
                return res

        return result

    return timed
