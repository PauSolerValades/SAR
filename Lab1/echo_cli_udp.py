#!/usr/bin/env python3

import socket as sk, sys

PORT = 50001

# Comprueba que se ha pasado un argumento.
if len( sys.argv ) != 2:
	print( "Uso: {} <servidor>".format( sys.argv[0] ) )
	exit( 1 )

dir_serv = (sys.argv[1], 50001)

s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

print( "Introduce el mensaje que quieres enviar (mensaje vacío para terminar):" )
while True:
	mensaje = input()
	if not mensaje:
		break
	
	mensaje_bytes = mensaje.encode()
	print("Caracteres:", len(mensaje),"\nBytes:", len(mensaje_bytes))
	
	#mensaje.encode() o str.encode(mensaje)
	s.sendto(mensaje_bytes, dir_serv)

	#la seguent linia ha d'estar darrera de sendto, sino et printeja el port auxiliar (0)
	print("IP:", sk.gethostbyname(sk.gethostname()), "Port:", s.getsockname()[1])
	
	buf = s.recv(1024)
	print("Datos del servidor:", buf.decode())

s.close()

