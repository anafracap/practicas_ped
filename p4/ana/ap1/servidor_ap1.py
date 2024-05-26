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

server_address = sys.argv[1]

if os.path.exists(server_address):
    os.remove(server_address)
    
server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_socket.bind(server_address)
print(server_socket)

server_socket.listen() #cambiar para varias conexiones al tiempo

try: 
    while True:
        try:
            connection, client_address = server_socket.accept()
            print(connection)
            answer_back(connection)
            connection.close()
        except BrokenPipeError:
            os.write(2, b"Broken pipe exception occurred. Connection closed unexpectedly.") # no sale en terminal
            continue
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")
finally:
    server_socket.close()
    os.unlink(server_address)