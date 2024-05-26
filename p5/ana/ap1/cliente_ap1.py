import sys, socket

class Client:
    def __init__(self, server_address, server_port):
        self.server_location = (server_address, server_port)
        self.client_socket = None

    def start(self, file_path):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.client_socket.sendto(file_path.encode('utf-8'), self.server_location)

        while True:
            data, _ = self.client_socket.recvfrom(1024)
            if not data:
                break
            self.client_socket.sendto("ack".encode('utf-8'), self.server_location)
            sys.stdout.buffer.write(data)

if __name__ == "__main__":
    file_path = sys.argv[1]
    server_address = sys.argv[2]
    server_port = int(sys.argv[3])
    client = Client(server_address, server_port)
    client.start(file_path)
