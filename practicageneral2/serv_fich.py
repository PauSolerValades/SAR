#!/usr/bin/env python3

import socket, sys, os, signal
import szasar

PORT = 6012
FILES_PATH = "files"
MAX_FILE_SIZE = 10 * 1 << 20 # 10 MiB
SPACE_MARGIN = 50 * 1 << 20  # 50 MiB
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
USERS = "+OKcipote#anal#cipote\r\n"
filecount = 0
lista = USERS[3:-2].split("#")
for i in lista:
	print(filecount, "- " + i)
	filecount += 1
PASSWORDS = ("", "sar", "sza")