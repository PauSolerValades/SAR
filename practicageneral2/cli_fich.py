#!/usr/bin/env python3

import socket, sys, os
import szasar

LINEA = ('-' * 39)
SERVER = 'localhost'
PORT = 50014
ER_MSG = {
	'01' : "Comando desconocido",
	'02' : "Parametro inesperado. Se ha recibido un parametro donde no se esperaba",
	'03' : "Falta parametro. Falta un parametro que no es opcional",
	'04' : "Parametro con formato incorrecto",
	'11' : "Usuario/contraseña incorrectos",
	'12' : "El servidor no tiene espacio disponible para almacenar el video",
	'13' : "No existe un video con ese identificador (13)",
	'14' : "No existe un video con ese identificador (14)",
	'15' : "No existe un video con ese identificador (15)",

}

class Menu:															# Este menu aparece nada mas loggearse y despues de ejecutar cada funcion del programa.
	Upload, Download, Taglist, Tagasign, Search, Quit = range(1, 7) # Sirve para seleccionar que funcion queremos usar con numeros del 1 al 7
	Options = ("Subir video", "Descargar video","Lista de etiquetas de un video", "Asignar una etiqueta a un video", "Buscar un video","Cerrar sesion")

	def menu():														# Printea  un menu visual para que el usuario elija que quiere que haga el cliente
		print( "+{}+".format( '-' * 37 ) )
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

def iserror( message ):												# Esta funcion checkea la respuesta del servidor para determinar si devuelve error o okey.
	if( message.startswith( "-ER" ) ):								# En caso de que devulva un error printeara una frase relacionada con el numero de error que
		code = message[3:5]											# haya devuelto el servidor
		#-ER11
		#01234
		print( ER_MSG[code] )
		return True
	else:
		return False

def log():
	user = input( "Introduce el nombre de usuario: " )			# El cliente pregunta al usuario su nick
	password = input( "Introduce la contraseña: " )				# El cliente pregunta al usuario su contrasena
	message = "{}{}#{}\r\n".format( szasar.Command.Log, user, password )
	s.sendall( message.encode() )
	return = szasar.recvline(s).decode()

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )			# Configuramos el socket
s.connect( (SERVER, PORT) )										# Efectuamos la conexion con el socket

logged = False


while True:

	if logged == False:
		msg = log()

		if not iserror(msg):	
			logged == True
		else
			continue

	option = Menu.menu()										# Printea el menu para que el usuario vea las diferentes opciones y elija la requerida

	if option == Menu.Upload:									# Esta funcion nos permite enviar un video al servidor para guardarlo alli
		filename = input( "Indica el fichero que quieres subir: " )
		try:
			filesize = os.path.getsize( filename )				# Primero, intentara acceder al archivo y leerlo. En caso de error el cliente se lo printeara al usuario
			with open( filename, "rb" ) as f:
				filedata = f.read()
				print("Tamaño: ", len(filedata), " bytes")
		except:
			print( "No se ha podido acceder al fichero {}.".format( filename ) )
			continue

		message = "{}{}#".format( szasar.Command.Put, filesize ) 
		s.sendall( message.encode() + filedata)					# Enviamos el mensaje junto, pero lo juntamos directamente en bytes para no tener que traducir bytes a strings.
		message = szasar.recvline( s ).decode()					# Recibimos la respuesta del servidor respecto a la consulta enviada por el cliente
		if not iserror( message ):								# En caso de que haya sido satisfactorio el cliente nos lo hara saber mediante un print
			print( "El fichero {} se ha enviado correctamente.".format( filename ) )
																# En caso contrario, el cliente nos printeara el error correspondiente al fallo del proceso

	elif option == Menu.Download:								# Esta funcion nos permite descargar un video del cual enviaremos el ID
		fileid = input( "Indica el fichero que quieres bajar: " )
		message =  "{}{}\r\n".format( szasar.Command.Get, fileid )
		s.sendall( message.encode() )
		message = szasar.recvline_file( s )							# Recibimos la respuesta del servidor respecto a la consulta enviada por el cliente
		if iserror(message[:5].decode()):						# Comprobamos si la respuesta del servidor es correcta, en este caso el cliene intentara escribir los 
			continue											# datos del video enviados por el servidor, en caso de que haya un error al escribir, lo printera.
		try:													# Si la respuesta es erronea el cliente printeara la explicacion del error y volvera a printear
			with open(fileid, "wb" ) as f:						# el menu para que el cliente decida que opcion quiere realizar
				f.write( message[3:] )
		except:
			print( "No se ha podido guardar el fichero en disco." )
		else:
			print( "El fichero {} se ha descargado correctamente.".format( fileid ) )

	
	elif option == Menu.Taglist:									# Esta funcion nos permite consultar los tags de un video el cual enviaremos el ID
		filename = input( "Indica el ID del fichero que quieres consultar: " )
		message = "{}{}\r\n".format( szasar.Command.Tag, filename)
		s.sendall( message.encode() )
		message = szasar.recvline( s ).decode()					# Recibimos la respuesta del servidor respecto a la consulta enviada por el cliente
		if iserror( message ):									# Comprobamos si la respuesta del servidor es correcta, en este caso el cliene printeara
			continue											# los tags del video. Si la respuesta es erronea el cliente printeara la explicacion del 
		filecount = 1											# error y volvera a printear el menu para que el cliente decida que opcion quiere realizar
		print( "Listado de etiquetas del video" )
		print( LINEA )
		lista = message[3:-2].split("#")
		for i in lista:
			print(filecount, "- " + i)
			filecount += 1
		print( LINEA )


	elif option == Menu.Tagasign:								# Esta funcion nos permite asignar un tag nuevo a un video el cual indicaremos mediante su ID
		fileid = input( "Indica el fichero al que quieras asignar la etiqueta: " )
		tag = input("Indica la etiqueta que quieres asignar:")
		message =  "{}{}#{}\r\n".format( szasar.Command.Log, fileid, tag )
		s.sendall( message.encode() )							# Enviaremos el ID del video y el tag que ha introducido el usuario en los inputs anteriores
		message = szasar.recvline( s ).decode()					# Recibimos la respuesta del servidor respecto a la consulta enviada por el cliente
		if not iserror( message ):								# Comprobamos si la respuesta del servidor es correcta, en ese caso el cliene printeara la etiqueta y ID del video correspondiente
			print( "La etiqueta {} se ha añadido correctamente al fichero {}.".format( tag , fileid) )
																# En caso contrario, el cliente nos printerara el error correspondiente al fallo del proceso

	elif option == Menu.Search:									# Esta funcion nos permite buscar todos los videos que contengan la etiqueta introducida por el usuario
		filename = input( "Indica la etiqueta que quieres busar: " )
		message = "{}{}\r\n".format( szasar.Command.Fnd, filename)
		s.sendall( message.encode() )
		message = szasar.recvline( s ).decode()					# Recibimos la respuesta del servidor respecto a la consulta enviada por el cliente
		if iserror( message ):									# Comprobamos si la respuesta del servidor es correcta, en este caso el cliene intentara escribir los 
			continue											# los videos que contengan ese tag. Si la respuesta es erronea el cliente printeara la explicacion del
		filecount = 0											# error y volvera a printear el menu para que el cliente decida que opcion quiere realizar
		print( "Listado de videos con esa etiqueta" )
		print( LINEA )
		lista = message[3:-2].split("#")
		if (lista != ['']):
			for i in lista:
				filecount += 1
				print(filecount, "- " + i)
		else:
			print ("No hay ningun video con esa etiqueta :_(")
		print( LINEA)


	elif option == Menu.Quit:									# Esta funcion nos permite desconectarnos del servidor y cerrar el cliente
		message = "{}\r\n".format( szasar.Command.Quit )
		s.sendall( message.encode() )							# Enviamos al servidor la peticion de desconexion para que sepa que vamos a cerrar el socket
		message = szasar.recvline( s ).decode()					# Recibimos 
		logged == False

s.close()
