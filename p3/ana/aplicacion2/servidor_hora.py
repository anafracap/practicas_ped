import os, sys, datetime

sys.argv[0] = "serv2"

path = "/tmp/fifo_ped4_ana_aplicacion2"
os.mkfifo(fifo_path)

w = open(path, 'w')

date = datetime.datetime.now().strftime('%c')

w.write(date)

