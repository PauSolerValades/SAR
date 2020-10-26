#!/usr/bin/env python3

import socket

DIR = "224.0.0.11" #dirección ip para sólo multicast.
PORT = 50006
GRUPO = "Fulano y Mengano".encode()

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

s.bind( ('', PORT) )


mreq = socket.inet_aton( DIR ) + socket.inet_aton( "0.0.0.0" ) #ip 0.0.0.0 puede recibir mensajes multicast y normales.
s.setsockopt( socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq ) #joindonde el tercer argumento, ue es la ip multicast más la normal en bytes (mreq)

buf, dir_emisor = s.recvfrom( 1024 )
if( len( buf ) != 10 ):
	print( "¡Error! Se esperaban recibir 10 bytes y se han recibido {}.".format( len( buf ) ) )
else:
	print( "Código {} recibido. Reenviando al servidor...".format( buf.decode() ) )
	s.sendto( buf + GRUPO, dir_emisor )
	buf = s.recv( 1024 )
	if( buf == b"OK" ):
		print( "El proceso ha finalizado correctamente." )
	elif( buf == b"ER" ):
		print( "Algo ha ido mal." )
	else:
		print( "Respuesta desconocida: {}.".format( buf.decode() ) )

s.setsockopt( socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq )
s.close()
