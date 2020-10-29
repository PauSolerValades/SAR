#!/usr/bin/env python3

import socket, sys, os
import szasar

LINEA = ('-' * 39)
SERVER = 'localhost'
PORT = 50007
ER_MSG = (
	"Correcto.",
	"Comando desconocido o inesperado.",
	"Parametro inesperado. Se ha recibido un parametro donde no se esperaba."
	"alta parámetro. Falta un parámetro que no es opcional.",
	"Parametro con formato incorrecto.",
	"Clave de paso o password incorrecto.",
	"Error al crear la lista de ficheros.",
	"El fichero no existe.",
	"Error al bajar el fichero.",
	"Un usuario anonimo no tiene permisos para esta operacion.",
	"El fichero es demasiado grande.",
	"Error al preparar el fichero para subirlo.",
	"Error al subir el fichero.",
	"Error al borrar el fichero." )

class Menu:
	Upload, Download, Taglist, Tagasign, Search, Quit = range(1, 7)
	Options = ("Subir video", "Descargar video","Lista de etiquetas de un video", "Asignar una etiqueta a un video", "Buscar un video","Cerrar sesion")

	def menu():
		print( "+{}+".format( '-' * 37 ) )
		print (5%2, " ",3/2)
		for i,option in enumerate( Menu.Options, 1 ):
			print( "| {}.- {:<32}|".format( i, option ) )
		print( "+{}+".format( '-' * 37 ) )

		while True:
			try:
				selected = int( input( "Selecciona una opción: " ) )
			except:
				print( "Opción no válida." )
				continue
			if 0 < selected <= len( Menu.Options ):
				return selected
			else:
				print( "Opción no válida." )

def iserror( message ):
	if( message.startswith( "-ER" ) ):
		code = int( message[4:5] )
		print( ER_MSG[code] )
		return True
	else:
		return False

def int2bytes( n ):
	if n < 1 << 10:
		return str(n) + " B  "
	elif n < 1 << 20:
		return str(round( n / (1 << 10) ) ) + " KiB"
	elif n < 1 << 30:
		return str(round( n / (1 << 20) ) ) + " MiB"
	else:
		return str(round( n / (1 << 30) ) ) + " GiB"



if __name__ == "__main__":
	if len( sys.argv ) > 3:
		print( "Uso: {} [<servidor> [<puerto>]]".format( sys.argv[0] ) )
		exit( 2 )

	if len( sys.argv ) >= 2:
		SERVER = sys.argv[1]
	if len( sys.argv ) == 3:
		PORT = int( sys.argv[2])

	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	s.connect( (SERVER, PORT) )

	"""while True:
		user = input( "Introduce el nombre de usuario: " )
		password = input( "Introduce la contraseña: " )
		message = "{}#{}#{}\r\n".format( szasar.Command.Log, user, password )
		s.sendall( message.encode() )
		message = szasar.recvline(s).decode()
		if iserror( message ):
			continue
		break
	"""


	while True:
		option = Menu.menu()

		if option == Menu.Taglist:
			filename = input( "Indica el ID del fichero que quieres consultar: " )
			message = "{}#{}\r\n".format( szasar.Command.Tag, filename)
			s.sendall( message.encode() )
			message = szasar.recvline( s ).decode() #recibimos el ok con todos los elementois de la lista.
			if iserror( message ):
				continue
			filecount = 1
			print( "Listado de etiquetas del video" )
			print( LINEA )
			lista = message[4:-2].split("#")
			for i in lista:
				print(filecount, "- " + i)
				filecount += 1
			print( LINEA )

		elif option == Menu.Download:
			fileid = input( "Indica el fichero que quieres bajar: " )
			message =  "{}#{}\r\n".format( szasar.Command.Get,fileid )
			s.sendall( message.encode() )
			message = szasar.recvlined( s ) #no queremos decodear el video, ya que lo tenemos que escribir en bytes
			if iserror(message[:5].decode()):
				continue
			try:
				with open(fileid, "wb" ) as f:
					f.write( message[3:] )
			except:
				print( "No se ha podido guardar el fichero en disco." )
			else:
				print( "El fichero {} se ha descargado correctamente.".format( fileid ) )

		elif option == Menu.Upload:
			filename = input( "Indica el fichero que quieres subir: " )
			try:
				filesize = os.path.getsize( filename )
				with open( filename, "rb" ) as f:
					filedata = f.read()
			except:
				print( "No se ha podido acceder al fichero {}.".format( filename ) )
				continue

			message = "{}#{}#".format( szasar.Command.Put, filesize )
			s.sendall( message.encode() + filedata)
			message = szasar.recvline( s ).decode()
			if not iserror( message ):
				print( "El fichero {} se ha enviado correctamente.".format( filename ) )

		elif option == Menu.Tagasign:
			fileid = input( "Indica el fichero al que quieras asignar la etiqueta: " )
			tag = input("Indica la etiqueta que quieres asignar:")
			message =  "{}#{}#{}\r\n".format( szasar.Command.Log,fileid,tag )
			s.sendall( message.encode() )
			message = szasar.recvline( s ).decode()
			if not iserror( message ):
				print( "La etiqueta {} se ha añadido correctamente al fichero {}.".format( tag , fileid) )

		elif option == Menu.Search:
			filename = input( "Indica la etiqueta que quieres busar: " )
			message = "{}#{}\r\n".format( szasar.Command.Fnd, filename)
			s.sendall( message.encode() )
			message = szasar.recvline( s ).decode() #recibimos el ok con todos los elementois de la lista.
			if iserror( message ):
				continue
			filecount = 0
			print( "Listado de videos con esa etiqueta" )
			print( LINEA )
			lista = message[4:-2].split("#")
			if (lista != ['']):
				for i in lista:
					filecount += 1
					print(filecount, "- " + i)
			else:
				print ("No hay ningun video con esa etiqueta :_(")
			print( LINEA)
		elif option == Menu.Quit:
			message = "{}\r\n".format( szasar.Command.Quit )
			s.sendall( message.encode() )
			message = szasar.recvline( s ).decode()
			break
	s.close()
