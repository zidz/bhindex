import codecs, logging, sys
from base64 import urlsafe_b64encode as b64encode
from uuid import uuid4
from time import time
from warnings import warn

import concurrent
from bithorde import parseHashIds, message
from db import ValueSet

if not getattr(sys.stdout, 'encoding', None):
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
if not getattr(sys.stderr, 'encoding', None):
    sys.stderr = codecs.getwriter('utf8')(sys.stderr)

class DelayedAction(object):
    def __init__(self, action):
        self.action = action
        self._scheduled = None

    def schedule(self, delay):
        if self._scheduled is None:
            self._scheduled = concurrent.spawn_after(delay, self._fire)

    def _fire(self):
        self._scheduled = None
        self.action()

def testDelayedAction():
    class Ctr:
        def __init__(self):
            self.x = 0
        def inc(self):
            self.x += 1

    def test():
        ctr = Ctr()
        a = DelayedAction(ctr.inc)
        a.schedule(0.00)
        a.schedule(0.00)
        concurrent.sleep(0.000)
        assert ctr.x == 1

    test()
    try:
        import eventlet
        eventlet.disabled = True
        reload(concurrent)
        test()
    except ImportError:
        pass

def hasValidStatus(dbAsset, t=time()):
    try: # New status
        availability = dbAsset['bh_availability']
        available = float(availability.any(0))

        if abs(available) > (t - availability.t):
            return available > 0
        else:
            return None
    except:
        pass

    try: # Legacy
        dbStatus = dbAsset['bh_status']
        dbConfirmedStatus = dbAsset['bh_status_confirmed']

        stable = dbConfirmedStatus.t - dbStatus.t
        nextCheck = dbConfirmedStatus.t + stable
        if t < nextCheck:
            return dbStatus.any() == 'True'
        else:
            return None
    except:
        pass

    return None

def _objectAvailability(dbAsset, t):
    '''Returns (bool(lastCheck), time_since_check)'''
    try:
        dbAvailability = dbAsset[u'bh_availability']
        avail = float(dbAvailability.any(0))
        time_since_check = t - dbStatus.t
        return avail, time_since_check
    except:
        pass

    try:
        dbStatus = dbAsset[u'bh_status']
        dbConfirmedStatus = dbAsset[u'bh_status_confirmed']
        time_since_check = (t - dbConfirmedStatus.t)
        if dbStatus.any() == 'True':
            avail = dbConfirmedStatus.t - dbStatus.t
        else:
            avail = -(dbConfirmedStatus.t - dbStatus.t)
        return avail, time_since_check
    except:
        pass

    return None, None

ASSET_WAIT_FACTOR = 0.02
def calcNewAvailability(status_ok, avail, time_since_check):
    if time_since_check is None: time_since_check = 1800
    if avail is None: avail = 0

    bonus = time_since_check * ASSET_WAIT_FACTOR

    if status_ok:
        if avail > 0:
            return avail + bonus
        else:
            return bonus
    else:
        if avail < 0:
            return avail - bonus
        else:
            return -bonus

def testCalcNewAvailabilty():
    assert calcNewAvailability(True, 500, 500) == 500 + (500*ASSET_WAIT_FACTOR)
    assert calcNewAvailability(False, 500, 500) == -(500*ASSET_WAIT_FACTOR)
    assert calcNewAvailability(True, -500, 500) == (500*ASSET_WAIT_FACTOR)
    assert calcNewAvailability(False, -500, 500) == -500 + (-500*ASSET_WAIT_FACTOR)
    assert calcNewAvailability(True, None, None) == 36
    assert calcNewAvailability(False, None, None) == -36

def updateFolderAvailability(db, item, newAvail, t):
    if not db: return

    tgt = t + newAvail

    for dir_mapping in item.get(u'directory', []):
        dir_mapping = dir_mapping.split('/', 1)
        if not len(dir_mapping) == 2:
            continue
        (dir_id, _) = dir_mapping
        directory = db.get(dir_id)

        if not directory.empty():
            objAvail = directory.get(u'bh_availability', 0)
            if objAvail:
                objAvail = objAvail.t + float(objAvail.any(0))
            else:
                objAvail = 0
            if tgt > objAvail:
                directory[u'bh_availability'] = ValueSet(unicode(newAvail), t=t)
                db.update(directory)
                updateFolderAvailability(db, directory, newAvail, t)

def cachedAssetLiveChecker(bithorde, assets, force=False, db=None):
    t = time()
    dirty = Counter()
    if db:
        commit_pending = DelayedAction(db.commit)

    def checkAsset(dbAsset):
        dbStatus = hasValidStatus(dbAsset, t)
        if dbStatus is not None and not force:
            concurrent.cede() # Not sleeping here could starve other greenlets
            return dbAsset, dbStatus

        ids = parseHashIds(dbAsset['xt'])
        if not ids:
            return dbAsset, None

        with bithorde.open(ids) as bhAsset:
            status = bhAsset.status()
            status_ok = status and status.status == message.SUCCESS

            avail, time_since_check = _objectAvailability(dbAsset, t)
            newAvail = calcNewAvailability(status_ok, avail, time_since_check)
            dbAsset[u'bh_availability'] = ValueSet(unicode(newAvail), t=t)
            if newAvail > 0:
                updateFolderAvailability(db, dbAsset, newAvail, t)

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
        self.printer = concurrent.spawn(self.run)
        self.unit = unit

    def run(self):
        start_time = last_time = time()
        last_processed = int(self)
        while int(self) < self.total:
            concurrent.sleep(1)
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

class RepeatingTimer(object):
    def __init__(self, interval, code):
        self.running = True
        self.running = concurrent.spawn(self._run, interval, code)

    def _run(self, interval, code):
        now = time()
        next = now + interval
        while self.running:
            concurrent.sleep(next-now)
            code()
            now = time()
            next = max(now, next + interval)

    def cancel(self):
        self.running = None