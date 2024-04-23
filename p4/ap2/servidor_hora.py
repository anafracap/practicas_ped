import os, sys, datetime, socket, select

sys.argv[0] = "serv2"

server_address = "/tmp/ped4_p4_ap2_server.sock"
server_address = sys.argv[1]

if os.path.exists(server_address):
    os.remove(server_address)
    
server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_socket.bind(server_address)
server_socket.listen() #cambiar para varias conexiones al tiempo

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
    os.unlink(server_address)
