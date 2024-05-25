import os, sys

class Client:
    def __init__(self, ask_server, get_from_server):
        self.ask_server = ask_server
        self.get_from_server = get_from_server
        self._create_fifo()
    
    def _create_fifo(self):
        if not os.path.exists(self.get_from_server):
            os.mkfifo(self.get_from_server)

    def start(self, number_of_iterations):
        for i in range(number_of_iterations):
            with open(self.ask_server, 'wb') as w: 
                w.write(str(os.getpid()).encode('utf-8'))

            with open(self.get_from_server, 'rb') as fifo_file:
                data = fifo_file.readline()
                os.write(1, data)

        os.unlink(self.get_from_server)

if __name__ == "__main__":
    path_ask = "/tmp/fifo_ped4_ana_p3_aplicacion2_ask_server"
    pid = str(os.getpid())
    path_time = "/tmp/fifo_ped4_ana_p3_aplicacion2_%s" % pid

    number_of_iterations = int(sys.argv[1])

    client = Client(path_ask, path_time)
    client.start(number_of_iterations)