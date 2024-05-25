import os

class Server:
    def __init__(self, server_fifo, client_fifo):
        self.server_fifo = server_fifo
        self.client_fifo = client_fifo
        self._create_fifos()

    def _create_fifos(self):
        if not os.path.exists(self.client_fifo):
            os.mkfifo(self.client_fifo)
        if not os.path.exists(self.server_fifo):
            os.mkfifo(self.server_fifo)

    def start(self):
        try:
            while True:
                with open(self.client_fifo, "rb") as rs:
                    path = rs.read().decode('utf8').strip()

                with open(path, 'rb') as fileO:  
                    while True:
                        content = fileO.read()
                        if not content:
                            fileO.close()
                            break
                        with open(self.server_fifo, "wb") as ws:
                            ws.write(content)
        except KeyboardInterrupt:
            os.write(2, b"Keyboard interrupt received. Exiting server.")
        finally:
            if self.server_fifo:
                os.unlink(self.server_fifo)
            if self.client_fifo:
                os.unlink(self.client_fifo)

if __name__ == "__main__":
    serverWrites = "/tmp/p3_ap1_server_writes_ped4_ana"
    clientWrites = "/tmp/p3_ap1_client_writes_ped4_ana"
    server = Server(serverWrites, clientWrites)
    server.start()
