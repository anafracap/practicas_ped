import os, sys, datetime

class Hora:
    def __init__(self):
        self.rdC, self.wdS = os.pipe()  # Server to client pipe

    def start(self, number_of_iterations):
        pid = os.fork()

        if pid:  # Parent - server
            self.run_server(number_of_iterations)
        else:  # Child - client
            self.run_client()

    def run_server(self, number_of_iterations):
        os.close(self.rdC)

        for i in range(number_of_iterations):
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
    number_of_iterations = int(sys.argv[1])
    hora.start(number_of_iterations)