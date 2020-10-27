#!/usr/bin/env python3

import socket

PORT = 50006

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

s.bind( ('', PORT) ) #assignar la dirección
s.listen( 5 )

while True:
	#dialogo=socket que llega del cliente. dir_cli = (ip cliente, puerto cliente)
	dialogo, dir_cli = s.accept()
	print( "Cliente conectado desde {}:{}.".format( dir_cli[0], dir_cli[1] ) )
	while True:
		buf = dialogo.recv( 4096 )
		if not buf:
			break
		mensaje = "+OK#PITO#"
		print(buf)
		dialogo.sendall( mensaje.encode()+b"1013")
	print( "Solicitud de cierre de conexión recibida." )
	dialogo.close()
s.close()

