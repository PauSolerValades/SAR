#!/usr/bin/env python3

import socket, os

PORT = 50013
SEND_SIZE = 4096


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
lista =[ "pito","polla","polla","polla"]
s.bind( ('', PORT) ) #assignar la dirección
s.listen( 5 )

while True:
	acc = b""
	#dialogo=socket que llega del cliente. dir_cli = (ip cliente, puerto cliente)
	dialogo, dir_cli = s.accept()
	print( "Cliente conectado desde {}:{}.".format( dir_cli[0], dir_cli[1] ) )
	while True:
		acc += dialogo.recv(SEND_SIZE)
		if(acc.endswith(b"\r\n")):
			break

	
	acc = acc.decode()
	print(acc)
	if(acc.startswith("LOG#jon")):
		dialogo.sendall("+OK".encode() + b"\r\n")
	else:
		dialogo.sendall("-ER#11".encode() + b"\r\n")
s.close()

