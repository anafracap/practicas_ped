import os, sys, socket

sys.argv[0] = "serv5"

server_address = "0.0.0.0"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))

try: 
    while True:
        data, client_address = server_socket.recvfrom(1024)
        path = data.decode().strip()

        with open(path, 'rb') as fileO:  
            while True:
                content = fileO.read(1024)
                if not content:
                    server_socket.sendto(b"", client_address)
                    break
                server_socket.sendto(content, client_address)
                server_socket.settimeout(30)
                try:
                    ack, _ = server_socket.recvfrom(1024)
                except socket.timeout:
                    os.write(2, b"Socket timeout, listening for other clients.")
                    break 
                server_socket.settimeout(None)

except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")

finally:
    server_socket.close()