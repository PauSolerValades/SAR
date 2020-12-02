#!/usr/bin/env python3

import os

from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor

import szasar

PORT = 6012
FILES_PATH = "files"
MAX_FILE_SIZE = 10 * 1 << 20 # 10 MiB
SPACE_MARGIN = 50 * 1 << 20  # 50 MiB
USERS = ("anonimous", "sar", "sza")
PASSWORDS = ("", "sar", "sza")

class State:
	Identification, Authentication, Main, Downloading, Uploading, Data = range(6)

class FD(LineReceiver):
	def __init__(self):
		self.state = State.Identification

	def lineReceived(self, line):
		message = line.decode("ascii")

		if message.startswith( szasar.Command.User ):
			if( self.state != State.Identification ):
				self.sendER()
				return
			try:
				user = USERS.index( message[4:] )
			except:
				self.sendER( 2 )
			else:
				self.sendOK()
				self.user = user
				self.state = State.Authentication

		elif message.startswith( szasar.Command.Password ):
			if self.state != State.Authentication:
				self.sendER()
				return
			if( self.user == 0 or PASSWORDS[self.user] == message[4:] ):
				self.sendOK()
				self.state = State.Main
			else:
				self.sendER( 3 )
				self.state = State.Identification

		elif message.startswith( szasar.Command.List ):
			if self.state != State.Main:
				self.sendER()
				return
			try:
				message = "OK\r\n"
				for filename in os.listdir( FILES_PATH ):
					filesize = os.path.getsize( os.path.join( FILES_PATH, filename ) )
					message += "{}?{}\r\n".format( filename, filesize )
			except:
				self.sendER( 4 )
			else:
				self.sendLine( message.encode( "ascii" ) )

		elif message.startswith( szasar.Command.Download ):
			if self.state != State.Main:
				self.sendER()
				return
			filename = os.path.join( FILES_PATH, message[4:] )
			try:
				filesize = os.path.getsize( filename )
			except:
				self.sendER( 5 )
				return
			else:
				self.sendOK( filesize )
				self.filename = filename
				self.state = State.Downloading

		elif message.startswith( szasar.Command.Download2 ):
			if self.state != State.Downloading:
				self.sendER()
				return
			self.state = State.Main
			try:
				with open( self.filename, "rb" ) as f:
					filedata = f.read()
			except:
				self.sendER( 6 )
			else:
				self.sendOK()
				self.transport.write( filedata )

		elif message.startswith( szasar.Command.Upload ):
			if self.state != State.Main:
				self.sendER()
				return
			if self.user == 0:
				self.sendER( 7 )
				return
			filename, filesize = message[4:].split('?')
			filesize = int(filesize)
			if filesize > MAX_FILE_SIZE:
				self.sendER( 8 )
				return
			svfs = os.statvfs( FILES_PATH )
			if filesize + SPACE_MARGIN > svfs.f_bsize * svfs.f_bavail:
				self.sendER( 9 )
				return
			self.sendOK()
			self.filename = filename
			self.bytes_left = filesize
			self.filedata = b""
			self.state = State.Uploading

		elif message.startswith( szasar.Command.Upload2 ):
			if self.state != State.Uploading:
				self.sendER()
				return
			self.setRawMode()
			self.state = State.Data

		elif message.startswith( szasar.Command.Delete ):
			if self.state != State.Main:
				self.sendER()
				return
			if self.user == 0:
				self.sendER( 7 )
				return
			try:
				os.remove( os.path.join( FILES_PATH, message[4:] ) )
			except:
				self.sendER( 11 )
			else:
				self.sendOK()

		elif message.startswith( szasar.Command.Exit ):
			self.sendOK()
			return

		else:
			self.sendER()

	def rawDataReceived(self, data):
		self.filedata += data
		self.bytes_left -= len(data)

		if self.bytes_left < 0:
			self.sendER( 10 )
		elif self.bytes_left == 0:
			try:
				with open( os.path.join( FILES_PATH, self.filename), "wb" ) as f:
					f.write( self.filedata )
			except:
				self.sendER( 10 )
			else:
				self.sendOK()
			self.setLineMode()
			self.state = State.Main

	def sendOK( self, params="" ):
		self.sendLine( ("OK{}".format( params )).encode( "ascii" ) )

	def sendER( self, code=1 ):
		self.sendLine( ("ER{}".format( code )).encode( "ascii" ) )

class FDFactory(Factory):
	def buildProtocol(self, addr):
		print( "Conexión aceptada del socket {0.host}:{0.port}.".format( addr ) )
		return FD()

if __name__ == "__main__":
	reactor.listenTCP(PORT, FDFactory())
	reactor.run()
