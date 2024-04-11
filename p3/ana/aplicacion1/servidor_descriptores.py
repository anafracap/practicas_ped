import os, sys

sys.argv[0] = "serv2"

serverWrites = "/tmp/server_writes_ped4_ana"
clientWrites = "/tmp/client_writes_ped4_ana"

os.mkfifo(clientWrites)

rs = open(clientWrites, "r")
path = rs.read().decode('utf8')strip()

fileD = os.open(path, os.O_RDONLY) 

content = ""
while True:
    line = os.read(fileD, 100).decode
    if not line:
        os.close(fileD)
        break
    content = content + line

ws = open(serverWrites, "w")

ws.write(content.encode('utf8'))