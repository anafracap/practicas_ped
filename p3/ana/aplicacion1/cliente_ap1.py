import sys

class Client:
    def __init__(self, server_fifo, client_fifo):
        self.server_fifo = server_fifo
        self.client_fifo = client_fifo

    def send_message(self, message):
        with open(self.client_fifo, "wb") as wc:
            wc.write(message.encode('utf8'))

    def receive_message(self):
        with open(self.server_fifo, "rb") as rc:
            while True:
                byteLine = rc.read()
                if not byteLine:
                    break
                sys.stdout.buffer.write(byteLine)
    
    def start(self, message):
        client.send_message(message)
        client.receive_message()


if __name__ == "__main__":
    serverWrites = "/tmp/p3_ap1_server_writes_ped4_ana"
    clientWrites = "/tmp/p3_ap1_client_writes_ped4_ana"
    message = sys.argv[1]
    
    client = Client(serverWrites, clientWrites)
    client.start(message)