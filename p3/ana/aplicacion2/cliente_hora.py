import os, sys, datetime

sys.argv[0] = "cli2"

path = "/tmp/fifo_ped4_ana_aplicacion2"
os.mkfifo(fifo_path)

r = open(path, 'r')
while True:
    line = r.readline().strip()
    if not line:
        break
    print(line)