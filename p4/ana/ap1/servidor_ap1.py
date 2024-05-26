import os, sys, socket

class Server:
    def __init__(self, server_adress):
        self.server_address = server_address
        self.server_socket = None
        self._clear_previous_address()

    def _clear_previous_address(self):
        if os.path.exists(self.server_address):
            os.remove(self.server_address)


    def answer_back(self, connection):
        path_bytes = connection.recv(1024)
        path = path_bytes.decode('utf-8').strip()

        with open(path, 'rb') as fileO:  
            while True:
                content = fileO.read(1024)
                if not content:
                    fileO.close()
                    break
                connection.send(content)
        connection.shutdown(socket.SHUT_WR)
        connection.close()

    def start(self):
        try:
            self.server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.server_socket.bind(self.server_address)

            self.server_socket.listen()

            while True:
                try:
                    connection, client_address = self.server_socket.accept()
                    self.answer_back(connection)
                    connection.close()
                except BrokenPipeError:
                    os.write(2, b"Broken pipe exception occurred. Connection closed unexpectedly.") # no sale en terminal
                    continue
        except KeyboardInterrupt:
            os.write(2, b"Keyboard interrupt received. Exiting server.")
        finally:
            self.server_socket.close()
            os.unlink(self.server_address)

if __name__ == "__main__":
    server_address = sys.argv[1]
    server = Server(server_address)
    server.start()