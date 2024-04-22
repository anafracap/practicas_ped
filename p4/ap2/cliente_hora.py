import os, sys, socket

sys.argv[0] = "cli2"

server_address = "/tmp/ped4_p4_ap2_server.sock"

pid = str(os.getpid())

for i in range(10):
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    client_socket.send(pid.encode())
    data = client_socket.recv(1024)
    print(data.decode())

client_socket.close()