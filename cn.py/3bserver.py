from socket import *
serverPort = 59
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(1024)
    filename = message.decode()
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        serverSocket.sendto(data.encode(), clientAddress)
    except:
        serverSocket.sendto(b"File not found", clientAddress)