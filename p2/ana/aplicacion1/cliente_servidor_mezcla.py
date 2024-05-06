import os, sys

sys.argv[0] = "cliserv2"

rdS,wdC = os.pipe()         # son file descriptors, no file objects - de cliente a servidor

rdC,wdS = os.pipe()         # son file descriptors, no file objects - de servidor a cliente
rc, ws  = os.fdopen(rdC,'rb',0), os.fdopen(wdS,'wb',0) # file objects  - de servidor a cliente

pid = os.fork() 

if pid:                   # padre - servidor
    sys.argv[0] = "serv2"
    os.close(wdC) 
    rc.close()
    data = os.read(rdS, 100).decode('utf8').strip()

    with open(data, 'rb') as fileO:  
        while True:
            content = fileO.read()
            if not content:
                fileO.close()
                break
            ws.write(content)

else:                     # hijo - cliente
    sys.argv[0] = "cli2"
    os.close(rdS)
    ws.close() 
    message = sys.argv[1]
    os.write(wdC, message.encode('utf8'))
    while True:
        byteLine = rc.read()
        if not byteLine:
            os.close(rdC)
            break
        sys.stdout.buffer.write(byteLine)
