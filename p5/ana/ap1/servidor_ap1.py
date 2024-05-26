import os, sys, socket

class Server:
    def __init__(self, server_port):
        self.server_address = "0.0.0.0"
        self.server_port = server_port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.server_address, server_port))

        try: 
            while True:
                data, client_address = self.server_socket.recvfrom(1024)
                path = data.decode('utf-8').strip()

                with open(path, 'rb') as fileO:  
                    while True:
                        content = fileO.read(1024)
                        if not content:
                            self.server_socket.sendto(b"", client_address)
                            break
                        self.server_socket.sendto(content, client_address)
                        self.server_socket.settimeout(30)
                        try:
                            ack, _ = self.server_socket.recvfrom(1024)
                        except socket.timeout:
                            os.write(2, b"Socket timeout, listening for other clients.")
                            break 
                        finally:
                            self.server_socket.settimeout(None)

        except KeyboardInterrupt:
            os.write(2, b"Keyboard interrupt received. Exiting server.")

        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server_port = int(sys.argv[1])
    server = Server(server_port)
    server.start()