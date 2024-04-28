import os, sys, socket

def answer_back(connection):
    path_bytes = connection.recv(1024)
    path = path_bytes.decode().strip()

    file_size = os.path.getsize(path)
    file_size_bytes = file_size.to_bytes(8, byteorder='big')
    connection.send(file_size_bytes)

    with open(path, 'rb') as fileO:  
        while True:
            content = fileO.read()
            if not content:
                fileO.close()
                break
            connection.send(content)
    connection.shutdown(socket.SHUT_WR)
    connection.close()

sys.argv[0] = "serv6"

server_address = "0.0.0.0"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_address, server_port))

server_socket.listen()
try: 
    while True:
        try:
            connection, client_address = server_socket.accept()
            pid = os.fork()

            if pid == 0:  # Child process
                server_socket.close()
                answer_back(connection)
                sys.exit(0)
            else:
                connection.close()
        except BrokenPipeError:
            os.write(2, b"Broken pipe exception occurred. Connection closed unexpectedly.") # no sale en terminal
            continue
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")

finally:
    server_socket.close()