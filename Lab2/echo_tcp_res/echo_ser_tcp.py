#!/usr/bin/env python3

import socket, os

PORT = 50007
SEND_SIZE = 4096


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
lista =[ "pito","polla","polla","polla"]
s.bind( ('', PORT) ) #assignar la dirección
s.listen( 5 )

def recvlined(s):                 # Iniciar sesión con el servidor
	fin = 0
	first = s.recv(SEND_SIZE) #hemos leido 4096 - 5 - loslbytes de size
	for i in first[4:]:
		fin += 1
		if(i == 35):
			break
	file_size = int(first[4:fin-1].decode())
	file_data = first[fin+1]
	file_size = file_size - len(file_data)
	
	while file_size > len(file_data):
		file_data += s.recv(SEND_SIZE) #asumiendo que recv no lee 0 (parece que es así)
		
	return b"+OK" + file_data

while True:
	#dialogo=socket que llega del cliente. dir_cli = (ip cliente, puerto cliente)
	dialogo, dir_cli = s.accept()
	print( "Cliente conectado desde {}:{}.".format( dir_cli[0], dir_cli[1] ) )
	message = recvlined( dialogo ) #no queremos decodear el video, ya que lo tenemos que escribir en bytes
	try:
		with open("video.mp4", "wb" ) as f:
			f.write( message[3:] )
	except:
		print( "No se ha podido guardar el fichero en disco." )
	else:
		print( "El fichero {} se ha descargado correctamente.".format( "video.mp4") )
	
s.close()

