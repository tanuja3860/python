from socket import *
serverPort = 56
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("The server is ready to receive")
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print("Client connected:", clientAddress)
    filename = connectionSocket.recv(1024).decode()
    try:
        file = open(filename, "rb")
        data = file.read()
        connectionSocket.send(data)
        file.close()
    except:
        connectionSocket.send(b"File not found")
    connectionSocket.close()