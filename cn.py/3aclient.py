from socket import *
serverName = "127.0.0.1"
serverPort = 56
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
filename = input("Enter file name: ")
clientSocket.send(filename.encode())
data = clientSocket.recv(4096)
print("\nFile contents:")
print(data.decode())
clientSocket.close()