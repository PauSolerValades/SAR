#!/usr/bin/env python3

from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor, ssl
from OpenSSL import SSL

MAX_USERS = 100
MAX_MSG_LENGTH = 255
MAX_USER_LENGTH = 16
MAX_INACTIVITY = 10.0

class ServerTLSContext(ssl.DefaultOpenSSLContextFactory):
    def __init__(self, *args, **kw):
        kw['sslmethod'] = SSL.TLSv1_METHOD
        ssl.DefaultOpenSSLContextFactory.__init__(self, *args, **kw)

class ChatProtocol(LineReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.name = None

    def connectionMade(self):
        if len(self.factory.users) == MAX_USERS:
            self.sendLine(b"-1")
            self.transport.loseConnection()
        else:
            self.sendLine(b"FTR0 1 1 1")

            userlist = " ".join(self.factory.users.keys()).encode("utf-8")
            self.sendLine(b"USR" + userlist)

    def connectionLost(self, reason):
        if self.name:
            del self.factory.users[self.name]
            self.broadcastMessage("OUT" + self.name)

    def lineReceived(self, line):
        line = line.decode("utf-8")

        if line.startswith("NME") and not self.name:
            name = line[3:]
            if " " in name:
                self.sendLine(b"-2")
            elif len(name) > MAX_USER_LENGTH:
                self.sendLine(b"-3")
            elif name in self.factory.users.keys():
                self.sendLine(b"-4")
            else:
                self.name = name
                self.factory.users[self.name] = self
                self.broadcastMessage("INN" + self.name)
                self.sendLine(b"+")
        elif line.startswith("MSG") and self.name:
            message = line[3:]

            timer = reactor.callLater(MAX_INACTIVITY, self.sendLine, b"NOP")

            if len(message) > MAX_MSG_LENGTH:
                self.sendLine(b"-5")
            else:

                f = open("banned.txt", "r")
                arr = f.read().split("\n")
                f.close()

                for i in arr[:-1]:
                    if i in message:
                        message = message.replace(i, "#####")
                
                message = "MSG{} {}".format(self.name, message)
                self.broadcastMessage(message)
                self.sendLine(b"+")

                timer.reset(MAX_INACTIVITY)

        elif line.startswith("WRT"):
            self.broadcastMessage("WRT"+self.name)
        
        elif line.startswith("TLS"):
            ctx = ServerTLSContext(privateKeyFileName='privada.key', certificateFileName='certificado.crt')
            self.transport.startTLS(ctx, self.factory)
            self.sendLine(b"+")

        else:
            self.sendLine(b"-0")

    def broadcastMessage(self, message):
        for protocol in self.factory.users.values():
            if protocol != self:
                protocol.sendLine(message.encode("utf-8"))

class ChatFactory(Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return ChatProtocol(self)

if __name__ == "__main__":
	reactor.listenTCP(8000, ChatFactory())
	reactor.run()
