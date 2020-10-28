import socket
import sys
import select

case = 'INICIO'
PORT = 50006
IP = 'localhost'  # Es necesario escribir cual es la IP del servidor al que nos queremos conectar
TIMEOUT_TIME = 60
FILENAME = "video.txt"
SEND_SIZE = 4096

dir_serv = (IP, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logged = False

def recive(datos):
    s.sendall(datos.encode())
    l = len(datos.encode())                     # Iniciar sesión con el servidor

    acc = b"" 
    ready = select.select([s], [], [], TIMEOUT_TIME)
    if ready[0]:
        while True:
            acc += s.recv(SEND_SIZE)
            if(acc.endswith(b"1013")):
                break
        return acc.decode()
        
def recive_file(datos):
    f = open("video.mp4", mode='wb')

    s.sendall(datos.encode())
    acc = b"" 
    ready = select.select([s], [], [], TIMEOUT_TIME)
    if ready[0]:
        answer, size, data = s.recv(SEND_SIZE).split(b"#")

        if answer == b"-ER":
            return answer.decode()
        
        size = int(size)
        f.write(data)
        compt = 0

        while True:
            f.write(s.recv(SEND_SIZE))
            compt += SEND_SIZE
            if size > compt:
                break
        
    return answer.decode()
            
    

def err(msg):
    return msg.split("#")[1]


def log(user, password):
    global logged
    s.connect( dir_serv )
    respuesta = recive(entrada)

    print(respuesta)
    if respuesta.startswith("+OK"):        
        logged = True
    else:
        print("Err 11")


def put(tVideo, fVideo):                 # PARAMETROS: TAMAÑO DE VIDEO + CONTENIDO DE VIDEO
    f = open(FILENAME, mode='rb')

    filesize = os.path.getsize(FILENAME)

    msg = "PUT#" + filesize + "#"

    #Aquí la función recive pero adapatada para enviar el fichero entero.
    """ 
        Esto lo necesitamso reescribir porque no tenemos ni el path del fichero que queremos reconvertir ni tampoco podemos convertir los bytes del video en strings para después reconvertir-los.
    """
    s.sendall(msg.encode() + f.read())

    acc = b"" 
    ready = select.select([s], [], [], TIMEOUT_TIME)
    if ready[0]:
        while True:
            acc += s.recv(4096)
            if(acc.endswith(b"1013")):
                break
        respuesta = acc.decode()

    if respuesta.startswith("+OK"):
        _, label = respuesta.split("#")
    else:
        print(err(respuesta))


def get(idVideo):                       # PARAMETROS: ID DE VIDEO
    respuesta = recive_file(entrada)

    if respuesta.startswith("+OK"):
        print("Descarga correcta en " + FILENAME)
    else:
        print(err(respuesta))                       # Descagar un video del servidor


def tag(idVideo):  
    respuesta = recive(entrada)                     # PARAMETROS ID VIDEO
                     # Obtener la lista de etiquetas de un vídeo
    if respuesta.startswith("+OK"):
        array = respuesta.split("#")
        array.pop(0)
    else:
        print(err(respuesta))

def st(idVideo, label):                  # PARAMETROS ID VIDEO + ETIQUETA
    respuesta = recive(entrada)                         # Asignar una etiqueta a un video

    if respuesta.startswith("+OK"):
        print("OK.")
    else:
        print(err(respuesta))
        


def fnd(label):                         # PARAMETRif
    respuesta = recive(entrada)

    if respuesta.startswith("+OK"):
        array = respuesta.split("#")
        array.pop(0)
        print(array)
        array.pop(0)
        print(array)
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
