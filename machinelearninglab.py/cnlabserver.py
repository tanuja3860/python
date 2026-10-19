import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCKET_IP = "127.0.0.1"
SOCKET_PORT = 5050
s.bind((SOCKET_IP, SOCKET_PORT))
print("Server is ready to receive")
data, client_address = s.recvfrom(4096)
print("Client:", data.decode())
s.sendto(data, client_address)
s.close()