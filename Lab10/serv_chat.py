#!/usr/bin/env python3

from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor

MAX_USERS = 100
MAX_MSG_LENGTH = 255
MAX_USER_LENGTH = 1
PORT = 8000

dict = {
    0: "error desconocido",
    1: "sala llena",
    2: "tu user es mierda"
}


class ChatProtocol(LineReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.name = None

    def connectionMade(self):
        self.sendLine("+\r\n".encode("UTF-8"))

    def connectionLost(self, reason):
        self.sendLine( ("-{}\r\n".format( dict[reason] )).encode("UTF-8") )

    def lineReceived(self, line):
        message = line.decode("UTF-8")

        if message.startswith("NME"):
            username = message[3:len(mensaje)-2]
            numUsers = len(self.factory.users)
            if(numUsers > MAX_USERS):
                self.connectionLost(self, 1)
            else:
                if(len(username) <= MAX_USER_LENGTH):
                    self.connectionMade(self)
                    self.factory.users[numUsers] = username
                else:
                    self.connectionLost(self, 2)

class ChatFactory(Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return ChatProtocol(self)

if __name__ == "__main__":
	reactor.listenTCP(PORT, ChatFactory())
	reactor.run()
