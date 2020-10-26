#!/usr/bin/env python3

import socket

PORT = 50002

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

s.bind( ('', PORT) ) #assignar la dirección
s.listen( 5 )

while True:
	#dialogo=socket que llega del cliente. dir_cli = (ip cliente, puerto cliente)
	dialogo, dir_cli = s.accept()
	print( "Cliente conectado desde {}:{}.".format( dir_cli[0], dir_cli[1] ) )
	while True:
		buf = dialogo.recv( 1024 )
		if not buf:
			break
		dialogo.sendall( buf )
	print( "Solicitud de cierre de conexión recibida." )
	dialogo.close()
s.close()

