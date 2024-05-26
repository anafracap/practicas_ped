import os, sys, socket

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
                try:
                    connection, client_address = self.server_socket.accept()
                    pid = os.fork()

                    if pid == 0:  # Child process
                        self.server_socket.close()
                        self.answer_back(connection)
                        sys.exit(0)
                    else:
                        connection.close()
                except BrokenPipeError:
                    os.write(2, b"Broken pipe exception occurred. Connection closed unexpectedly.") # no sale en terminal
                    continue
        except KeyboardInterrupt:
            os.write(2, b"Keyboard interrupt received. Exiting server.")

        finally:
            self.server_socket.close()

    def answer_back(self, connection):
        path_bytes = connection.recv(1024)
        path = path_bytes.decode('utf-8').strip()

        with open(path, 'rb') as fileO:  
            while True:
                content = fileO.read()
                if not content:
                    fileO.close()
                    break
                connection.send(content)
        connection.shutdown(socket.SHUT_WR)
        connection.close()

if __name__ == "__main__":
    server_port = int(sys.argv[1])
    server = Server(server_port)
    server.start()    