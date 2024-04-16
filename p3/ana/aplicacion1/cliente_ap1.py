import os, sys

sys.argv[0] = "cli2"

serverWrites = "/tmp/p3_ap1_server_writes_ped4_ana"
clientWrites = "/tmp/p3_ap1_client_writes_ped4_ana"

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