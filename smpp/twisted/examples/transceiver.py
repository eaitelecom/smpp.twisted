import logging
from twisted.internet import reactor, defer
from smpp.twisted.client import SMPPClientTransceiver, SMPPClientService
from smpp.twisted.config import SMPPClientConfig

class SMPP(object):
    
    def __init__(self, config=None):
        if config is None:
            config = SMPPClientConfig(host='localhost', port=999, username='uname', password='pwd')

            # Uncomment line below to recv SMS via #322223322 only
            # config = SMPPClientConfig(host='localhost', port=999, username='uname', password='pwd', addressTon=AddrTon.UNKNOWN, addressNpi=AddrNpi.ISDN, addressRange='^322223322$')
        self.config = config
        
    @defer.inlineCallbacks
    def run(self):
        try:
            #Bind
            smpp = yield SMPPClientTransceiver(self.config, self.handleMsg).connectAndBind()
            #Wait for disconnect
            yield smpp.getDisconnectedDeferred()
        except Exception, e:
            error = "ERROR: %s" % str(e)
            print(error)
        finally:
            reactor.stop()
    
    def handleMsg(self, smpp, pdu):
        """
        NOTE: you can return a Deferred here
        """
        msg = "Received pdu %s" % pdu
        print(msg)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    SMPP().run()
    reactor.run()
