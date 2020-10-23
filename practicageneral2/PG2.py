import socket, sys

PORT = 50002
IP = 456               #Es necesario escribir cual es la IP del servidor al que nos queremos conectar

dir_serv = (IP, PORT)
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )



while True:
    entrada = input()
    if (entrada.startswith("LOG") ) :
        print("pito")
        mensaje = input()
    if not mensaje:
        break
        
        
        s.sendall( mensaje.encode() )
    # Es necesario un blucle porque no hay garantías de que la respuesta
    # completa se reciba en una única lectura.
        bytes_por_leer = len( mensaje.encode() )
        mensaje = b""
        while bytes_por_leer:
            buf = s.recv( bytes_por_leer )
            mensaje += buf
            bytes_por_leer -= len( buf )
        print( mensaje.decode() )
s.close()