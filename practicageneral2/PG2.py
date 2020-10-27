import socket
import sys

PORT = 50002
IP = 456  # Es necesario escribir cual es la IP del servidor al que nos queremos conectar

dir_serv = (IP, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

case = 'INICIO'

def log(x,y):
    print("cipote")                     # PARAMETROS: USUARIO + CONTRASEÑA                   # Iniciar sesión con el servidor

def put(x,y):                           # PARAMETROS: TAMAÑO DE VIDEO + CONTENIDO DE VIDEO
    return "put"                        #Subir video al servidor

def get(x):                             # PARAMETROS: ID DE VIDEO
    return "get"                        # Descagar un video del servidor

def tag(x):                             # PARAMETROS ID VIDEO
    return "tag"                        # Obtener la lista de etiquetas de un vídeo

def st(x,y):                            # PARAMETROS ID VIDEO + ETIQUETA
    return "st"                         # Asignar una etiqueta a un video

def fnd(x):                             # PARAMETROS ETIQUETA
    return "fnd"                        # Buscar vídeos que tengan determinada etiqueta

def qit():                              # PARAMETROS
    return "qit"                        # Cerrar la sesión

    
while case != 'QIT':
    contador = 0
    entrada = input()                   # Utilizado para controlar todos los tipos de entrada que podemos tener (1,2 y 3 parametros)
    for caracter in entrada:
        if caracter == " ":             # Recorremos el input contando cuantos parametros hay para que no salte el
            contador = contador + 1     # error de split, al no poder asignar todas las variables

    if contador == 0:
        case = entrada                  # 1 PARAMETRO (CASOS: QIT)
        if case == 'QIT':
            break
        else: print("Comando o numero de parametros erroneos")

    if contador == 1:                   # 2 PARAMETROS (CASOS: GET/TAG/FND)
        case, p1 = entrada.split()
        if case == 'GET':
            get(p1)
        elif case == 'TAG':
            tag(p1)
        elif case == 'FND':
            fnd(p1)
        else : print("Comando o numero de parametros erroneos")

    if contador == 2:                   # 3 PARAMETROS (CASOS: LOG/PUT/SET)
        case, p1, p2 = entrada.split()
        if case == 'LOG':
            log(p1,p2)
        elif case == 'PUT':
            put(p1,p2)
        elif case == 'ST':
            st(p1,p2)
        else: print("Comando o numero de parametros erroneos")
    
    
    