import select,socket

TIMEOUT_TIME = 60
SEND_SIZE = 4096

class Command:
	Log, Put, Get, Tag, Set, Fnd, Quit = ("LOG", "PUT", "GET", "TAG", "SET", "FND", "QIT")

def recvline(s):                 # Iniciar sesión con el servidor

    acc = b"" 
    ready = select.select([s], [], [], TIMEOUT_TIME)
    if ready[0]:
        while True:
            acc += s.recv(SEND_SIZE)
            if(acc.endswith(b"\r\n")):
                break
        return acc
		
def recvall( s, size ):
	message = b''
	while( len( message ) < size ):
		chunk = s.recv( size - len( message ) )
		if chunk == b'':
			raise EOFError( "Connection closed by the peer before receiving the requested {} bytes.".format( size ) )
		message += chunk
	return message


def recvlined(s):

	fin = 0
	first = s.recv(SEND_SIZE)
	if(first[:2].decode() == "-ER"):
		return b"-ER#13"
	
	for i in first[4:]:
		fin += 1
		if(i == 35): # COmprobando ASCII (caritarefacherafacherita)
			break
	file_size = int(first[4:fin-1].decode())
	file_data = first[fin+1]
	file_size = file_size - len(file_data)

	while file_size > len(file_data):
			# asumiendo que recv no lee 0 (parece que es así)
		file_data += s.recv(SEND_SIZE)

	return b"+OK" + file_data