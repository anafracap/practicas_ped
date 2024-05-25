import os, sys

class Ficheros:
    def __init__(self, message):
        self.message = message
        self.rdS, self.wdC = os.pipe()  # Client to server pipe
        self.rdC, self.wdS = os.pipe()  # Server to client pipe
        self.rc = os.fdopen(self.rdC, 'rb', 0)  # File object for server to client pipe
        self.ws = os.fdopen(self.wdS, 'wb', 0)  # File object for server to client pipe

    def start(self):
        pid = os.fork()

        if pid:  # Parent - server
            self.run_server()
        else:  # Child - client
            self.run_client()

    def run_server(self):
        os.close(self.wdC) 
        self.rc.close()
        data = os.read(self.rdS, 100).decode('utf8').strip()
        with open(data, 'rb') as fileO:  
            while True:
                content = fileO.read()
                if not content:
                    fileO.close()
                    break
                self.ws.write(content)

    def run_client(self):
        os.close(self.rdS)
        self.ws.close() 
        message = sys.argv[1]
        os.write(self.wdC, message.encode('utf8'))
        while True:
            byteLine = self.rc.read()
            if not byteLine:
                os.close(self.rdC)
                break
            sys.stdout.buffer.write(byteLine)

if __name__ == "__main__":
    message = sys.argv[1]
    ficheros = Ficheros(message)
    ficheros.start()
