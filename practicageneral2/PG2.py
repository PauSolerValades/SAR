import socket
import sys
import select

case = 'INICIO'
PORT = 50006
IP = 'localhost'  # Es necesario escribir cual es la IP del servidor al que nos queremos conectar
TIMEOUT_TIME = 60

dir_serv = (IP, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logged = False

def recive():
    s.sendall(entrada.encode())
    l = len(entrada.encode())                     # Iniciar sesión con el servidor

    f = b"" 
    ready = select.select([s], [], [], TIMEOUT_TIME)
    if ready[0]:
        while True:
            f += s.recv(4096)
            if(f.endswith(b"1013")):
                break
        return f.decode()

def err(msg):
    return msg.split("#")[1]


def log(user, password):
    global logged
    s.connect( dir_serv )
    print("ctrankada")                # PARAMETROS: USUARIO + CONTRASEÑA
    respuesta = recive()
    print(respuesta)
    if respuesta.startswith("+OK"):        
        logged = True
        print("P")
    else:
        print("Err 11")


def put(tVideo, fVideo):                 # PARAMETROS: TAMAÑO DE VIDEO + CONTENIDO DE VIDEO
    respuesta = recive()

    if respuesta.startswith("+OK"):
        _, label = respuesta.split("#")
    else:
        print(err(respuesta))


def get(idVideo):                       # PARAMETROS: ID DE VIDEO
    respuesta = recive()

    if respuesta.startswith("+OK"):
        _, size, fl = respuesta.split("#")
    else:
        print(err(respuesta))                        # Descagar un video del servidor


def tag(idVideo):  
    respuesta = recive()                     # PARAMETROS ID VIDEO
                     # Obtener la lista de etiquetas de un vídeo
    if respuesta.startswith("+OK"):
        array = respuesta.split("#")
        array.pop(0)
    else:
        print(err(respuesta))

def st(idVideo, label):                  # PARAMETROS ID VIDEO + ETIQUETA
    respuesta = recive()                         # Asignar una etiqueta a un video

    if respuesta.startswith("+OK"):
        print("OK.")
    else:
        print(err(respuesta))
        


def fnd(label):                         # PARAMETRif
    respuesta = recive()

    if respuesta.startswith("+OK"):
        array = respuesta.split("#")
        array.pop(0)
        array.pop(0)
    else:
        print(err(respuesta))


while True:
    contador = 0                        # Utilizado para controlar todos los tipos de entrada que podemos tener (1,2 y 3 parametros)
    entrada = input()
    for caracter in entrada:
        if caracter == "#":             # Recorremos el input contando cuantos parametros hay para que no salte el
            contador = contador + 1     # error de split, al no poder asignar todas las variables

   
    if logged:
        if contador == 0:
            case = entrada                  
            if case == 'QIT':
                s.close()
                break
            else:
                print("Comando o numero de parametros erroneos")
        if contador == 1:                   #
            case, p1 = entrada.split("#")
            if case == 'GET':
                get(p1)
            elif case == 'TAG':
                tag(p1)
            elif case == 'FND':
                fnd(p1)
            else:
                print("Comando o numero de parametros erroneos, se esperaba 1 argumento ")
        elif contador == 2:
                if case == 'PUT':
                    put(p1, p2)
                elif case == 'ST':
                    st(p1, p2)
        else:
            print("Comando o numero de parametros erroneos, se esperaban 2 argumentos")
    else:
        if contador == 0:
            case = entrada                  
            if case == 'QIT':
                s.close()
                break
            else:
                print("Comando o numero de parametros erroneos")
        if contador == 2:                   
            case, p1, p2 = entrada.split("#")
            if case == 'LOG':
                log(p1, p2)
        else:
            print("No hay mas comandos available hasta que te logges")