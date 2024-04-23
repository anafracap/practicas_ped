import os, sys, socket

sys.argv[0] = "cli5"

server_address = sys.argv[2]
server_port = int(sys.argv[3])

message = sys.argv[1]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))
client_socket.send(message.encode())

file_size_bytes, _ = client_socket.recvfrom(8)
file_size = int.from_bytes(file_size_bytes, byteorder='big')

received_size = 0
while received_size < file_size:
    data = client_socket.recv(1024)
    received_size += len(data)
    sys.stdout.buffer.write(data)

