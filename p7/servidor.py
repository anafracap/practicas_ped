import os, sys, socket

def send_all_clients(message):
    for nick, c in clients.items():
        print(nick, c, file=sys.stderr)
        try:
            c.send(message.encode('utf-8'))
        except:
            # Eliminar el cliente si hay algún problema de conexión
            del clients[nick]


def verify_nick(cli_sock):
    identify = "Please enter your UNIQUE nickname: "
    cli_sock.send(identify.encode('utf-8'))
    nick = cli_sock.recv(1024).decode('utf-8')
    print(nick, file=sys.stderr)
    if nick in clients:
        message = "Your nickname is already in use, unable to log in \n"
        cli_sock.send(message.encode('utf-8'))
        cli_sock.close()
        return False
    else:
        clients[nick] = cli_sock
        print(list(clients), file=sys.stderr)
        login = "You have successfully logged in! Type 'exit' to leave the chat.\n"
        cli_sock.send(login.encode('utf-8'))
        send_all_clients(f"{nick} has joined the chat!")
        return nick

def continue_conversation(cli_sock, nick):
    while True:
        message = cli_sock.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            cli_sock.send("exit".encode())
            cli_sock.close()
            del clients[nick]
            send_all_clients(f"{nick} has left the chat.")
            break
        print(message, file=sys.stderr)
        send_all_clients(f"{nick}: {message}")
        


server_address = "0.0.0.0"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_address, server_port))
server_socket.listen()
print(server_socket, file=sys.stderr)

clients = {}

try: 
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            nick = verify_nick(client_socket)
            if nick:
                continue_conversation(client_socket, nick)
        except (BrokenPipeError, ConnectionResetError):
            string = "Broken pipe exception occurred. Connection closed unexpectedly by: %s \n" % nick
            print(string, file=sys.stderr)
            if client_socket in clients.values():
                del clients[nick]
                client_socket.close()
            continue
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server. \n")
finally:
    server_socket.close()

