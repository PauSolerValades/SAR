#!/usr/bin/env python3

import socket, os

PORT = 50014
SEND_SIZE = 4096


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ('', PORT) ) #assignar la dirección
s.listen( 5 )

while True:
	#dialogo=socket que llega del cliente. dir_cli = (ip cliente, puerto cliente)
	dialogo, dir_cli = s.accept()
	print( "Cliente conectado desde {}:{}.".format( dir_cli[0], dir_cli[1] ) )
	while True:
		message = dialogo.recv(SEND_SIZE) #no queremos decodear el video, ya que lo tenemos que escribir en bytes
		dialogo.sendall(b"+OK\r\n")
	
s.close()

