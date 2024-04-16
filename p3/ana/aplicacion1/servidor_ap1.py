import os, sys

sys.argv[0] = "serv2"

serverWrites = "/tmp/p3_ap1_server_writes_ped4_ana"
clientWrites = "/tmp/p3_ap1_client_writes_ped4_ana"

if not os.path.exists(clientWrites):
    os.mkfifo(clientWrites)

if not os.path.exists(serverWrites):
    os.mkfifo(serverWrites)

with open(clientWrites, "rb") as rs:
    path = rs.read().decode('utf8').strip()

with open(path, 'rb') as fileO:  
    while True:
        content = fileO.read()
        if not content:
            fileO.close()
            break
        with open(serverWrites, "wb") as ws:
            ws.write(content)