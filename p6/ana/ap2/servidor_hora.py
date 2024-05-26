import os, sys, datetime, socket

class Server:
    def __init__(self, server_port):
        self.server_address = "0.0.0.0"
        self.server_port = server_port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, self.server_port))

        self.server_socket.listen()

        try: 
            while True:
                connection, client_address = self.server_socket.accept()

                pid = connection.recv(1024).decode('utf-8')

                date = datetime.datetime.now().strftime('%c') + '\n'
                connection.send(date.encode('utf-8'))

                connection.close()
        except KeyboardInterrupt:
            os.write(2, b"Keyboard interrupt received. Exiting server.")

        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server_port = int(sys.argv[1])
    server = Server(server_port)
    server.start()    
