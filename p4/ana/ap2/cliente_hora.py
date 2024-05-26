import os, sys, socket

class Client:
    def __init__(self, server_address):
            self.server_address = server_address
            self.client_socket = None
        
    def start(self, number_of_iterations):
        pid = str(os.getpid())

        for i in range(number_of_iterations):
            client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            client_socket.connect(server_address)
            client_socket.send(pid.encode('utf-8'))
            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    server_address = sys.argv[1]
    number_of_iterations = int(sys.argv[2])

    client = Client(server_address)
    client.start(number_of_iterations)