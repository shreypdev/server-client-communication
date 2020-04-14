import sys
import socket

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
FILE_NAME = str(sys.argv[3])

BUFFER_SIZE = 1024

#Define a TCP client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Establish a client socket to the target
s.connect((HOST, PORT))

#Send the HTTP GET command
s.sendall( ('GET /' + FILE_NAME + ' HTTP/1.1 ').encode())

#get response from the server and keep appending
msg = ''
while True:
	response = s.recv(BUFFER_SIZE)
	if response:
		msg += response.decode("utf-8")
	else:
		break

#Print the HTML response from the server
print(msg)


