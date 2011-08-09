import pyhorde.bithorde as bithorde
from pyhorde.bithorde import connectUNIX, reactor, message, b32decode

import config

class BitHordeClient(bithorde.Client):
    def __init__(self, assets, onStatusUpdate):
        self.assets = assets
        self.onStatusUpdate = onStatusUpdate

    def onConnected(self):
        conf = config.read()
        pressure = int(conf.get('BITHORDE', 'pressure'))
        self.ai = bithorde.AssetIterator(self, self.assets, self.onStatusUpdate, self.whenDone, parallel=pressure)

    def onDisconnected(self, reason):
        if not self.closed:
            print "Disconnected; '%s'" % reason
            try: reactor.stop()
            except: pass

    def onFailed(self, reason):
        print "Failed to connect to BitHorde; '%s'" % reason
        reactor.stop()

    def whenDone(self):
        self.close()
        reactor.stop()
