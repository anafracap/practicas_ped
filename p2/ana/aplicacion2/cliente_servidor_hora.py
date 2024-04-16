import os, sys, datetime

sys.argv[0] = "cliserv2"

rdC,wdS = os.pipe()         # son file descriptors, no file objects - de servidor a cliente

pid = os.fork() 

if pid:                   # padre - servidor
    sys.argv[0] = "serv2"
    os.close(rdC)
    print (pid)

    while True:
        date = datetime.datetime.now().strftime('%c')
        os.write(wdS, date.encode('utf8'))

else:                     # hijo - cliente
    sys.argv[0] = "cli2"
    os.close(wdS) 
    print(pid)

    while True:
        line = os.read(rdC, 100).decode('utf8').strip()
        if not line:
            break
        print(line)