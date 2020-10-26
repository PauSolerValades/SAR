#!/usr/bin/env python3

import socket, sys, select

PORT = 50003
TIMER = 1
MAX_INTENTOS = 3

if len( sys.argv ) != 2:
	print( "Uso: {} <servidor>".format( sys.argv[0] ) )
	exit( 1 )

print( "Servidor:", sys.argv[1], "Dirección IP:", socket.gethostbyname( sys.argv[1] ) )

dir_serv = (sys.argv[1], PORT)

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

s.connect( dir_serv ) #no crea ninguna conexión, esto es el tcp. Lo que hace es recordar a quién he enviado los mensajes lol.

print( "Introduce el mensaje que quieres enviar (mensaje vacío para terminar):" )
while True:
	mensaje = input()
	if not mensaje:
		break
	intentos = 1
	while True:
		s.send( mensaje.encode() )
		#le pasas los sockets y el tiempo que tienen que esperar antes de salir del recv
		recibido, _, _ = select.select( [ s ], [], [], TIMER )
		if recibido:
			break
		else:
			print( "Fallo en el intento nº {}. No se ha recibido respuesta en el tiempo especificado ({} s).".format( intentos, TIMER ) )
			intentos += 1
			if intentos > MAX_INTENTOS:
				print ( "Superado el numero maximo de retransmisiones ({}) con este mensaje: {}".format( MAX_INTENTOS, mensaje ) )
				exit( 1 )
	buf = s.recv( 1024 ) #recordemos que se queda aquí esperando los mensajes. Si en TIMER no ha llegado nada, cierras la conexión.
	print( buf.decode() )
s.close()
