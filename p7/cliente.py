import sys, socket, select

def read(cli_sock):
    message = cli_sock.recv(1024).decode('utf-8')
    if message.lower() == 'exit':
        print("Server has closed the connection.", file=sys.stderr)
        cli_sock.close()
        return
    elif not message:
        cli_sock.close()
        print("Server has closed the connection. 2", file=sys.stderr)
    print(message)

def write(cli_sock):
    message = input()
    cli_sock.send(message.encode('utf-8'))
    if message.lower() == 'exit':
        cli_sock.shutdown(socket.SHUT_WR)
        return

server_address = sys.argv[1]
server_port = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_address, server_port))

    nick = input(client_socket.recv(1024).decode('utf-8'))
    client_socket.send(nick.encode('utf-8'))
    print(nick)
    login = client_socket.recv(1024).decode('utf-8')
    print(login)

    while True:
        # Only include client_socket in the list if it's still open
        inputs = [sys.stdin]
        if client_socket.fileno() != -1:  # Check if socket is still open
            inputs.append(client_socket)
        else:
            break

        readable, _, _ = select.select(inputs, [], [])

        for trigger_socket in readable:
            if trigger_socket == sys.stdin:
                write(client_socket)
            else:
                read(client_socket)
    
except KeyboardInterrupt:
    print("Keyboard interrupt received. Exiting client.")
finally:
    if client_socket.fileno() != -1:  # Check if socket is still open
        client_socket.close()
