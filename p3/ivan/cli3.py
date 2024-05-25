import os
import sys

def main():
    # Nombre de la FIFO (tubería con nombre)
    fifo_name = '/tmp/fifo_cliente_grupo3'

    # Nombre del archivo a solicitar
    file_name = 'documento.txt'

    # Verificar si la FIFO ya existe, si no, crearla
    if not os.path.exists(fifo_name):
        os.mkfifo(fifo_name)

    try:
        # Abrir la FIFO para escritura
        with open(fifo_name, 'w') as fifo:
            # Escribir el nombre del archivo en la FIFO
            fifo.write(file_name)

        # Leer la respuesta del servidor
        with open(fifo_name, 'r') as fifo:
            response = fifo.readline().strip()
            print(response)

    except FileNotFoundError:
        # Si no se puede conectar con el servidor, imprimir un mensaje de error
        print("Error: No se pudo conectar con el servidor.")
        sys.exit(1)

if __name__ == "__main__":
    main()

