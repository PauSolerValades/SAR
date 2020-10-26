import socket
import sys

PORT = 50002
IP = 456  # Es necesario escribir cual es la IP del servidor al que nos queremos conectar

dir_serv = (IP, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
contador = 0

def log():
    return "log"

def put():
    return "put"

def get():
    return "get"

def tag():
    return "tag"

def st():
    return "tag"

def fnd():
    return "fnd"

def qit():
    return "qit"

def switch(case):
    switcher = {
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
    case = entrada              # 1 PARAMETRO (CASOS: QIT)

if contador == 1:               # 2 PARAMETROS (CASOS: GET/TAG/FND)
    case, p1 = entrada.split()

if contador == 2:               # 3 PARAMETROS (CASOS: LOG/PUT/SET)
    case, p1, p2 = entrada.split()

print (switch(case))
