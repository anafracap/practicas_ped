import os, sys, datetime

class Hora:
    def __init__(self):
        self.rdC, self.wdS = os.pipe()  # Server to client pipe

    def start(self, number_of_iteration):
        pid = os.fork()

        if pid:  # Parent - server
            self.run_server(number_of_iteration)
        else:  # Child - client
            self.run_client()

    def run_server(self, number_of_iteration):
        os.close(self.rdC)

        for i in range(number_of_iteration):
            date = datetime.datetime.now().strftime('%c')
            os.write(self.wdS, date.encode('utf8'))

    def run_client(self):
        os.close(self.wdS) 

        while True:
            line = os.read(self.rdC, 100).decode('utf8').strip()
            if not line:
                break
            print(line)

if __name__ == "__main__":
    hora = Hora()
    number_of_iteration = int(sys.argv[1])
    hora.start(number_of_iteration)