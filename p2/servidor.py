import os
import time

# Crear la tubería
r, w = os.pipe()

# Crear el proceso hijo
pid = os.fork()

if pid:  # Proceso padre
    os.close(w)
    r = os.fdopen(r)
    while True:
        # Leer la fecha y hora del sistema
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # Enviar la fecha y hora al cliente a través de la tubería
        os.write(w, fecha_hora.encode('utf-8') + b'\n')
        time.sleep(1)
else:  # Proceso hijo
    os.close(r)
