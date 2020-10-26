#!/usr/bin/env python3

import socket, os, signal, select

PORT = 50005
MAX_BUF = 1024
MAX_WAIT = 120

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

s.bind( ('', PORT) )

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

while True:
	buf, dir_cli = s.recvfrom( MAX_BUF )
	if not buf:
		continue
	#hem de crear el fill que crearà el socket
	if not os.fork(): #entra el fill
		s.close() #tanquem el socket original
		dialogo = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) #creem un socket nou
		dialogo.connect( dir_cli ) # i connectem el socket nou amb la direcció del client que ens esperava
		#UDP mejorao de aquí en adelante.
		while buf: #aquest es el bucle per anar esperant missatges, fins aquí com sempre.
			dialogo.send( buf )
			recibido, _, _ = select.select( [ dialogo ], [], [], MAX_WAIT ) #excepte això, que ens demana esperar 120s màxim.
			if not recibido:
				print( "Agotado tiempo máximo de espera ({} s). Fin de la comunicación.".format( MAX_WAIT ) )
				break
			buf = dialogo.recv( MAX_BUF )
		dialogo.close()
		exit( 0 )
s.close()

