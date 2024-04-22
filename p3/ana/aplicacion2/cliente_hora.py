import os, sys, datetime

sys.argv[0] = "cli2"

path_ask = "/tmp/fifo_ped4_ana_p3_aplicacion2_ask_server"

pid = str(os.getpid())
path_time = "/tmp/fifo_ped4_ana_p3_aplicacion2_%s" % pid

if not os.path.exists(path_time):
    os.mkfifo(path_time)

for i in range(10):
    with open(path_ask, 'wb') as w: 
        w.write(pid.encode())

    with open(path_time, 'rb') as fifo_file:
        data = fifo_file.readline()
        os.write(1, data)

os.unlink(path_time)