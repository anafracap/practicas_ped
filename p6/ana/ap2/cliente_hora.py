import os, sys, socket

class Client:
    def __init__(self, server_address, server_port):
        self.server_location = (server_address, server_port)
        self.client_socket = None

    def start(self, number_of_iterations):
        pid = str(os.getpid())

        for i in range(number_of_iterations):
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(self.server_location)
            self.client_socket.send(pid.encode('utf-8'))
            data = self.client_socket.recv(1024)
            print(data.decode('utf-8'))

        self.client_socket.close()

if __name__ == "__main__":
    number_of_iterations = int(sys.argv[1])
    server_address = sys.argv[2]
    server_port = int(sys.argv[3])
    client = Client(server_address, server_port)
    client.start(number_of_iterations)