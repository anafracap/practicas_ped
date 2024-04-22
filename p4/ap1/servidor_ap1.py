import os, sys, socket

sys.argv[0] = "serv2"

server_address = "/tmp/ped4_p4_ap1_server.sock"

if os.path.exists(server_address):
    os.remove(server_address)
    
server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen() #cambiar para varias conexiones al tiempo

try: 
    while True:
        connection, client_address = server_socket.accept()

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
                connection.close()
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")

finally:
    server_socket.close()
    os.unlink(server_address)