import os, sys, socket

sys.argv[0] = "cli2"

server_address = "/tmp/ped4_p4_ap1_server.sock"
server_address = sys.argv[2]

message = "./ejemplo.txt"
message = sys.argv[1]

client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client_socket.connect(server_address)
client_socket.send(message.encode())

file_size_bytes = client_socket.recv(8)
file_size = int.from_bytes(file_size_bytes, byteorder='big')

while True:
    byteLine = client_socket.recv(file_size)
    if not byteLine:
        break
    sys.stdout.buffer.write(byteLine)
