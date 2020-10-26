import socket
import sys

PORT = 50002
IP = 456  # Es necesario escribir cual es la IP del servidor al que nos queremos conectar

dir_serv = (IP, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
contador = 0

def log():                          # PARAMETROS: USUARIO + CONTRASEÑA
    return "log"                    # Iniciar sesión con el servidor

def put():                          # PARAMETROS: TAMAÑO DEVIDEO + CONTENIDO DE VIDEO
    return "put"                    #Subir video al servidor

def get():                          # PARAMETROS: ID DE VIDEO
    return "get"                    # Descagar un video del servidor

def tag():                          # PARAMETROS ID VIDEO
    return "tag"                    # Obtener la lista de etiquetas de un vídeo

def st():                           # PARAMETROS ID VIDEO + ETIQUETA
    return "tag"                    # Asignar una etiqueta a un video

def fnd():                          # PARAMETROS ETIQUETA
    return "fnd"                    # Buscar vídeos que tengan determinada etiqueta

def qit():
    return "qit"                    # Cerrar la sesión

def switch(case):                   # Ya que en Python3 no existe la función switch por defecto hemos implementado usando la función diccionario
    switcher = {                    # una funcion que imita su comportamiento
        'LOG': log(),
        'PUT': put(),
        'GET': get(),
        'TAG': tag(),
        'SET': st(),
        'FND': fnd(),
        'QIT': qit()
    }
    return switcher.get(case)
    

entrada = input()                   # Utilizado para cobtrolar todos los tipos de entrada que podemos tener (1,2 y 3 parametros)
for caracter in entrada:
    if caracter == " ":             # Recorremos el input contando cuantos parametros hay para que no salte el
        contador = contador + 1     # error de split, al no poder asignar todas las variables
        print(contador)

if contador == 0:
    case = entrada                  # 1 PARAMETRO (CASOS: QIT)

if contador == 1:                   # 2 PARAMETROS (CASOS: GET/TAG/FND)
    case, p1 = entrada.split()

if contador == 2:                   # 3 PARAMETROS (CASOS: LOG/PUT/SET)
    case, p1, p2 = entrada.split()

print (switch(case))
