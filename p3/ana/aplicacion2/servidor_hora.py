import os, sys, datetime

sys.argv[0] = "serv2"

path_ask = "/tmp/fifo_ped4_ana_p3_aplicacion2_ask_server"

if not os.path.exists(path_ask):
    os.mkfifo(path_ask)

while True:
    with open(path_ask, 'rb') as fifo_ask:
        pid = fifo_ask.readline()
        path_write = "/tmp/fifo_ped4_ana_p3_aplicacion2_%s" % pid.decode()

    with open(path_write, 'wb') as w: 
        date = datetime.datetime.now().strftime('%c') + '\n'
        w.write(date.encode())

