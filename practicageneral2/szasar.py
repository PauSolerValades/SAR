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


def recvline_file(s):

	fin = 3
	first = s.recv(SEND_SIZE)			
	if(first[:3].decode() == "-ER"):		#-ERXX
		return b"-ER#13"					#01234
	
	for i in first[3:]:
		fin += 1
		if(i == 35): # Comprobando si i es # en ascii
			break

	file_size = int(first[3:fin-1].decode())
	file_data = first[fin:]
	file_size = file_size - len(file_data)

	done = len(file_data)
	while done < file_size:

		file_data += s.recv(SEND_SIZE)
		done = len(file_data)

		percent = round(done/file_size *100, 2)
		print(percent, "%")

	return b"+OK" + file_data