#!/usr/bin/env python3

import socket

PORT = 50001
#creamos socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#hacemos el bind
#para el punto4 tenemos que canviar el 50001 por 0, así coge el puerto disponible.
s.bind(('', 50001))

while True:
	
	mensaje, dir_cli = s.recvfrom(1024)

	host, port = dir_cli
	print("Host:", host, "Port:", port)

	s.sendto(mensaje, dir_cli)

s.close()