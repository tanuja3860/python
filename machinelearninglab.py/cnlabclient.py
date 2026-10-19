import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCKET_IP = "127.0.0.1"
SOCKET_PORT = 5050
MESSAGE = input("Enter the message: ")
s.sendto(MESSAGE.encode(), (SOCKET_IP, SOCKET_PORT))
data = s.recvfrom(4096)
print("Server:", data[0].decode())
s.close()