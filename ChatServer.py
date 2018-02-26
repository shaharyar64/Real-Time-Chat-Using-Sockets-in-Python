#!/usr/bin/env python
#import socket module
from socket import *
def chat(connectionSocket):
    while 1:
        sentence=connectionSocket.recv(1024)
    
        if sentence=='close':
            connectionSocket.send("connection Socket terminate request from client...")
            connectionSocket.close()
	    return 0
        else:
            rpl=raw_input("Client: "+sentence+"\nServer: ")    	
    	    connectionSocket.send(rpl)
    
portNumber=5000
ServerSocket=socket(AF_INET,SOCK_STREAM)
ServerSocket.bind(('',portNumber))
ServerSocket.listen(1)
print "Servre is ready"
print "Waiting for request"
connectionSocket,addr=ServerSocket.accept()    
chat(connectionSocket)
ServerSocket.close()
