import os, sys

serverWrites = "/tmp/server_writes_ped4_ana"
clientWrites = "/tmp/client_writes_ped4_ana"

os.mkfifo(clientWrites)

wc = open(clientWrites, "w")

message = "./ejemplo.txt"
#message = "/etc/services"
wc.write(message.encode('utf8'))

rc = open(serverWrites, "r")

content = rc.read().decode('utf8').strip()

print(content)