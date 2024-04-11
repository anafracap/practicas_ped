import os, sys

rdS,wdC = os.pipe()         # son file descriptors, no file objects - de cliente a servidor

rdC,wdS = os.pipe()         # son file descriptors, no file objects - de servidor a cliente

pid = os.fork() 

if pid:                   # padre - servidor
    os.close(rdC)
    os.close(wdC) 
    print (pid)
    data = ""
    while True:
        byte = os.read(rdS, 10).decode('utf8').strip()
        if not byte:
            break
        data = data + byte

    fileD = os.open(data, os.O_RDONLY) 
    
    offset = 0
    while True:
        bytes_sent = os.sendfile(wdS, fileD, offset, 100)
        offset = offset + 100 
        if not bytes_sent:
            os.close(fileD)
            break

else:                     # hijo - cliente
    os.close(rdS)
    os.close(wdS) 
    print(pid)
    message = "/Users/anafraile/Clases/uni-clases/23-24/sem2/ped/practicas/p2/ana/aplicacion1/ejemplo.txt"
    #message = "/etc/services"
    os.write(wdC, message.encode('utf8'))
    #wc.close()
    while True:
        byteLine = os.read(rdC, 100).decode('utf8').strip()
        if not byteLine:
            break
        print(byteLine)