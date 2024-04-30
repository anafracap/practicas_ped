import os, sys, socket


def verify_nick(cli_sock):
    nick = cli_sock.recv(1024).decode('utf-8')
    print(nick)
    if nick in clients:
        message = "Your nickname is already in use, unable to log in"
        cli_sock.send(message.encode('utf-8'))
        cli_sock.close()
        return False
    else:
        clients[nick] = cli_sock
        print(list(clients))
        login = "You have successfully logged in"
        cli_sock.send(login.encode('utf-8'))
        return nick

def continue_conversation(cli_sock):
    while True:
        message = cli_sock.recv(1024).decode('utf-8')
        print(message)
        for nick, c in clients.copy().items():
            if c != cli_sock:
                try:
                    c.send(message.encode('utf-8'))
                except:
                    # Eliminar el cliente si hay algún problema de conexión
                    del clients[nick]


server_address = "0.0.0.0"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_address, server_port))
server_socket.listen()
print(server_socket)

clients = {}

try: 
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            nick = verify_nick(client_socket)

            pid = os.fork()

            if pid == 0:  # Child process
                server_socket.close() #stop listening for new connections
                if nick:
                    continue_conversation(client_socket)
                sys.exit(0)
            else:
                client_socket.close()
        except (BrokenPipeError, ConnectionResetError):
            string = b"Broken pipe exception occurred. Connection closed unexpectedly by: %s" % nick
            os.write(2, string)
            if client_socket in clients.values():
                del clients[nick]
                client_socket.close()
            continue
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")
finally:
    server_socket.close()

