import os, sys, socket

sys.argv[0] = "cli6"

server_address = sys.argv[2]
server_port = int(sys.argv[3])

pid = str(os.getpid())

for i in range(int(sys.argv[1])):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    client_socket.send(pid.encode())
    data = client_socket.recv(1024)
    print(data.decode())

client_socket.close()