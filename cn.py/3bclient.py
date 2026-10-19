from socket import *
serverName = "127.0.0.1"
serverPort = 59
clientSocket = socket(AF_INET, SOCK_DGRAM)
filename = input("Enter file name: ")
clientSocket.sendto(filename.encode(), (serverName, serverPort))
data, serverAddress = clientSocket.recvfrom(4096)
print("\nFile contents:")
print(data.decode())
clientSocket.close()