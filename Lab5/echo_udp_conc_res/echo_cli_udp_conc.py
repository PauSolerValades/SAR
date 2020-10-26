#!/usr/bin/env python3

import socket, sys

PORT = 50005
MAX_BUF = 1024

if len( sys.argv ) != 2:
	print( "Uso: {} <servidor>".format( sys.argv[0] ) )
	exit( 1 )

dir_serv = (sys.argv[1], PORT)

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

"""
Primer hem de fer una passada del bulce fora per poder saber amb quin socket ens connecta el servidor.
"""

mensaje = input( "Introduce el mensaje que quieres enviar (mensaje vacío para terminar):\n" )
if not mensaje:
	exit( 0 )
s.sendto( mensaje.encode(), dir_serv )

buf, dir_serv2 = s.recvfrom( MAX_BUF )
print( buf.decode() )

s.connect( dir_serv2 )

while True:
	mensaje = input()
	if not mensaje:
		break
	s.send( mensaje.encode() )
	buf = s.recv( MAX_BUF )
	print( buf.decode() )
s.send( b"" )
s.close()
