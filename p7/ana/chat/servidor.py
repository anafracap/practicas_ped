import os, sys, socket

server_address = "0.0.0.0"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen()

clients = {}

try: 
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            pid = os.fork()

            if pid == 0:  # Child process
                server_socket.close() #stop listening for new connections
                nick = verify_nick(client_socket)
                if nick:
                    continue_conversation(client_socket, nick)
                sys.exit(0)
            else:
                client_socket.close()
        except (BrokenPipeError, ConnectionResetError):
            os.write(2, b"Broken pipe exception occurred. Connection closed unexpectedly.")
            if client_socket in clients.values():
                del clients[nick]
                client_socket.close()
            continue
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")
finally:
    server_socket.close()

def verify_nick(cli_sock):
    nick = cli_sock.recv(1024)
    if nick in clients:
        cli_sock.send("Your nickname is already in use, unable to log in")
        cli_sock.close()
        return False
    else:
        clients[nick] = cli_sock
        cli_sock.send("You have successfully logged in")
        return nick

def continue_conversation(cli_sock):
    while True:
        message = cli_sock.recv(1024)
        for nick in clients:
            c = clients[nick]
            c.send(message)


