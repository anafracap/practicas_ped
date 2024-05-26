import sys, socket

class Client:
    def __init__(self, server_address):
        self.server_address = server_address
        self.client_socket = None

    def start(self, file_path):
        self.client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.client_socket.connect(server_address)
        self.client_socket.send(file_path.encode('utf-8'))
        self.client_socket.shutdown(socket.SHUT_WR)
        
        while True:
            byteLine = self.client_socket.recv(1024)
            if not byteLine:
                break
            sys.stdout.buffer.write(byteLine)

        self.client_socket.close()

if __name__ == "__main__":
    file_path = sys.argv[1]
    server_address = sys.argv[2]
    client = Client(server_address)
    client.start(file_path)