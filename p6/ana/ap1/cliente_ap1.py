import sys, socket

class Client:
    def __init__(self, server_address, server_port):
        self.server_location = (server_address, server_port)
        self.client_socket = None

    def start(self, file_path):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_address, server_port))
        self.client_socket.send(file_path.encode('utf-8'))
        self.client_socket.shutdown(socket.SHUT_WR)

        while True:
            data = self.client_socket.recv(1024)
            if not data:
                break
            sys.stdout.buffer.write(data)
            
        self.client_socket.close()

if __name__ == "__main__":
    file_path = sys.argv[1]
    server_address = sys.argv[2]
    server_port = int(sys.argv[3])
    client = Client(server_address, server_port)
    client.start(file_path)
