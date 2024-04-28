import os, sys, socket

sys.argv[0] = "serv5"

server_address = "0.0.0.0"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))

try: 
    while True:
        try:
            data, client_address = server_socket.recvfrom(1024)
            path = data.decode().strip()

            file_size = os.path.getsize(path)
            file_size_bytes = file_size.to_bytes(8, byteorder='big')
            server_socket.sendto(file_size_bytes, client_address)

            with open(path, 'rb') as fileO:  
                while True:
                    content = fileO.read(1024)
                    if not content:
                        fileO.close()
                        break
                    server_socket.sendto(content, client_address)
            connection.shutdown(socket.SHUT_WR)
            connection.close()
        except BrokenPipeError:
            os.write(2, b"Broken pipe exception occurred. Connection closed unexpectedly.")
            continue
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")

finally:
    server_socket.close()