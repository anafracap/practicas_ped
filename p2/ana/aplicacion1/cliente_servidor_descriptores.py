import os, sys

sys.argv[0] = "cliserv2"

rdS,wdC = os.pipe()         # son file descriptors, no file objects - de cliente a servidor

rdC,wdS = os.pipe()         # son file descriptors, no file objects - de servidor a cliente

pid = os.fork() 

if pid:                   # padre - servidor
    sys.argv[0] = "serv2"
    os.close(rdC)
    os.close(wdC) 
    print (pid)
    data = os.read(rdS, 100).decode('utf8').strip()

    fileD = os.open(data, os.O_RDONLY) 
    
    while True:
        line = os.read(fileD, 100)
        if not line:
            os.close(fileD)
            break
        os.write(wdS, line)

else:                     # hijo - cliente
    sys.argv[0] = "cli2"
    os.close(rdS)
    os.close(wdS) 
    print(pid)
    #message = "./ejemplo.txt"
    message = "/etc/services"
    os.write(wdC, message.encode('utf8'))
    #wc.close()
    while True:
        byteLine = os.read(rdC, 100).decode('utf8').strip()
        if not byteLine:
            break
        print(byteLine)