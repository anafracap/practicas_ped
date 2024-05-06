import os, sys, socket

def read(cli_sock):
    while True:
        message = cli_sock.recv(1024)
        print(message.decode('utf-8'))

def write(cli_sock):
    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

server_address = sys.argv[1]
server_port = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

nick = input("Ingrese su nombre: ")
client_socket.send(nick.encode('utf-8'))

login = client_socket.recv(1024).decode('utf-8')
sys.stderr.write(login)

try:
    pid = os.fork()
    if pid == 0:  # Child process
        read(client_socket)
    else:
        write(client_socket)
    
except KeyboardInterrupt:
    print("Keyboard interrupt received. Exiting client.")
finally:
    client_socket.close()
