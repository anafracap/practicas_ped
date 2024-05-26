import os, datetime

class Server:
    def __init__(self, ask_server_path):
        self.ask_server = ask_server_path
        self.path_write = None
        self._create_fifo()

    def _create_fifo(self):
        if not os.path.exists(self.ask_server):
            os.mkfifo(self.ask_server)

    def start(self):
        try:
            while True:
                with open(self.ask_server, 'rb') as fifo_ask:
                    pid = fifo_ask.readline()
                    self.path_write = "/tmp/fifo_ped4_ana_p3_aplicacion2_%s" % pid.decode('utf-8')

                with open(self.path_write, 'wb') as w: 
                    date = datetime.datetime.now().strftime('%c') + '\n'
                    w.write(date.encode('utf-8'))
        except KeyboardInterrupt:
            os.write(2, b"Keyboard interrupt received. Exiting server.")
        finally:
            if os.path.exists(self.ask_server):
                os.unlink(self.ask_server)
            if self.path_write and os.path.exists(self.path_write):
                os.unlink(self.path_write)

if __name__ == "__main__":
    path_ask = "/tmp/fifo_ped4_ana_p3_aplicacion2_ask_server"
    server = Server(path_ask)
    server.start()

