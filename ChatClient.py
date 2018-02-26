from socket import *
def chat (connectionSocket):
    while 1:
        sentence=raw_input("Client: ")
        connectionSocket.send(sentence)
        modeifiedSentence=connectionSocket.recv(1024)
        print "Server: "+modeifiedSentence
        if sentence=="close":
            connectionSocket.close()
            break
            
serverName="192.168.1.103"
portNumber=5000
connectionSocket=socket(AF_INET,SOCK_STREAM)
serverIp=raw_input("Enter ip to connect: ")
print "Initiating request..."
try:
    connectionSocket.connect((serverIp,portNumber))
    print "Connected to server.You can start chat"
    chat(connectionSocket)
except:
    print "Server not found"

    




