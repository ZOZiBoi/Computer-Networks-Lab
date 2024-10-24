import socket 
import sys

#create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to the port 
server_address = ('localhost', 1234)
print >>sys.stderr,'starting up on %s port %s' % server_address
sock.bind(server_address) #bind() is used to associate the socket with the server address 

#listen for incoming connections 
sock.listen(1)

while True:
    #wait for connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_addr = sock.accept() 
    #listen() puts socket in server mode and accept()
    #wait for an incoming connection. accept() returns an open connection between the 
    #server and client, along with address of the client. the connection is actually 
    #a different socket on another port (assigned my the kernel). Data is read from the 
    #connection with recv() and transmitted with sendall() 
    