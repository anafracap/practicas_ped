# cliente_servidor_ficheros.py

import os
import sys

def servidor():
    while True:
        # Leer el path del fichero del cliente
        path = sys.stdin.readline().strip()
        
        try:
            # Intentar abrir y leer el fichero
            with open(path, 'r') as f:
                contenido = f.read()
                # Enviar contenido al cliente
                sys.stdout.write(contenido)
        except FileNotFoundError:
            # Si el fichero no existe, enviar mensaje de error al cliente
            sys.stdout.write("Error: El fichero no existe\n")
        
        # Forzar la salida de la caché
        sys.stdout.flush()

def cliente(path):
    # Enviar el path del fichero al servidor
    sys.stdout.write(path + '\n')
    sys.stdout.flush()
    
    # Leer la respuesta del servidor y mostrarla
    respuesta = sys.stdin.read()
    sys.stdout.write(respuesta)

# Verificar si se está ejecutando como servidor o cliente
if __name__ == "__main__":
    if 'serv2' in sys.argv[0]:
        servidor()
    elif 'cli2' in sys.argv[0]:
        if len(sys.argv) != 2:
            sys.stderr.write("Uso: {} <ruta del fichero>\n".format(sys.argv[0]))
            sys.exit(1)
        cliente(sys.argv[1])
