import os, sys, datetime, socket, select

sys.argv[0] = "serv6"

server_address = "0.0.0.0"
server_port = int(sys.argv[1])
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_address, server_port))

server_socket.listen()

try: 
    while True:
        connection, client_address = server_socket.accept()

        pid = connection.recv(1024).decode()

        date = datetime.datetime.now().strftime('%c') + '\n'
        connection.send(date.encode())

        connection.close()
except KeyboardInterrupt:
    os.write(2, b"Keyboard interrupt received. Exiting server.")

finally:
    server_socket.close()

