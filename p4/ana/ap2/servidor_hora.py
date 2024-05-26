import os, sys, datetime, socket

class Server:
    def __init__(self, server_address):
        self.server_address = server_address
        self.path_write = None
        self._clear_previous_address()

    def _clear_previous_address(self):
        if os.path.exists(self.server_address):
            os.remove(self.server_address)
    
    def start (self):
        self.server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_socket.bind(self.server_address)
        self.server_socket.listen() #cambiar para varias conexiones al tiempo

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
            os.unlink(self.server_address)

if __name__ == "__main__":
    server_address = sys.argv[1]
    server = Server(server_address)
    server.start()
