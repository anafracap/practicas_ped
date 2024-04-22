import os, sys, socket

sys.argv[0] = "cli2"

server_address = "127.0.0.1" 
server_port = int(sys.argv[1])

pid = str(os.getpid())

for i in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(pid.encode(), (server_address, server_port))
    data, _ = client_socket.recvfrom(1024)
    print(data.decode())

client_socket.close()