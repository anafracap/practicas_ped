import os, sys

rdS,wdC = os.pipe()         # son file descriptors, no file objects - de cliente a servidor
rs, wc  = os.fdopen(rdS,'rb',0), os.fdopen(wdC,'wb',0) # file objects - de cliente a servidor

rdC,wdS = os.pipe()         # son file descriptors, no file objects - de servidor a cliente
rc, ws  = os.fdopen(rdC,'rb',0), os.fdopen(wdS,'wb',0) # file objects  - de servidor a cliente
pid = os.fork() 

if pid:                   # padre - servidor
    rc.close()
    wc.close() 
    print (pid)
    data = rs.read()  # recibe el path completo
    file = open(data.decode('utf8').strip(), 'r')
    print (file)
    content = file.read()
    ws.write(content.encode('utf8')) 
    ws.flush()
    file.close()

else:                     # hijo - cliente
    rs.close() 
    ws.close()
    print(pid)
    message = "/Users/anafraile/Clases/uni-clases/23-24/sem2/ped/practicas/p2/ana/aplicacion1/ejemplo.txt"
    #message = "/etc/services"
    wc.write(message.encode('utf8')) 
    wc.flush() 
    wc.close()
    print(rc.readline().decode('utf8').strip())