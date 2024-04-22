import os, sys, datetime, socket, select

sys.argv[0] = "serv2"

server_address = "127.0.0.1"
server_port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))

try: 
    while True:
        data, client_address = server_socket.recvfrom(1024)
        pid = data.decode()

        date = datetime.datetime.now().strftime('%c') + '\n'
        server_socket.sendto(date.encode(), client_address)
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")

finally:
    server_socket.close()

