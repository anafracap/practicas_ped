import os, sys

sys.argv[0] = "cliserv2"

serverWrites = "/tmp/p3_ap1_server_writes_ped4_ana"
clientWrites = "/tmp/p3_ap1_client_writes_ped4_ana"

if not os.path.exists(clientWrites):
    os.mkfifo(clientWrites)

if not os.path.exists(serverWrites):
    os.mkfifo(serverWrites)

pid = os.fork() 

if pid:                   # padre - servidor
    sys.argv[0] = "serv2"
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
    os.unlink(clientWrites)
    os.unlink(serverWrites)

else:                     # hijo - cliente
    sys.argv[0] = "cli2"
    #message = "./ejemplo.txt"
    #message = "/etc/services"
    #message = "/bin/sh"
    message = sys.argv[1]
    with open(clientWrites, "wb") as wc:
        wc.write(message.encode('utf8'))

    with open(serverWrites, "rb") as rc:
        while True:
            byteLine = rc.read()
            if not byteLine:
                break
            sys.stdout.buffer.write(byteLine)
