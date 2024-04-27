import os

# Crear la tubería
r, w = os.pipe()

# Crear el proceso hijo
pid = os.fork()

if pid:  # Proceso padre
    os.close(w)
    r = os.fdopen(r)
    while True:
        # Leer la fecha y hora enviada por el servidor
        fecha_hora = r.readline().decode('utf-8').strip()
        print("Fecha y hora del servidor:", fecha_hora)
else:  # Proceso hijo
    os.close(r)
