import os, sys, socket

sys.argv[0] = "cli5"

server_address = sys.argv[2]
server_port = int(sys.argv[3])

message = sys.argv[1]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(message.encode(), (server_address, server_port))

while True:
    data, _ = client_socket.recvfrom(1024)
    if not data:
        break
    client_socket.sendto("ack".encode(), (server_address, server_port))
    sys.stdout.buffer.write(data)

