import os
import sys

def main():
    # Nombre de la FIFO (tubería con nombre)
    fifo_name = '/tmp/fifo_cliente_grupo3'

    # Crear la FIFO si no existe
    if not os.path.exists(fifo_name):
        os.mkfifo(fifo_name)

    try:
        # Abrir la FIFO para lectura
        with open(fifo_name, 'r') as fifo:
            # Leer el nombre del archivo del cliente
            file_name = fifo.readline().strip()

            # Intentar abrir el archivo solicitado
            try:
                with open(file_name, 'r') as file:
                    # Leer el contenido del archivo
                    content = file.read()

                    # Enviar el contenido del archivo al cliente a través de la FIFO
                    sys.stdout.write(content)

            except FileNotFoundError:
                # Si el archivo no existe, enviar un mensaje de error al cliente
                sys.stdout.write("Error: El archivo solicitado no existe")

    finally:
        # Eliminar la FIFO al finalizar
        os.unlink(fifo_name)
        # Agregar una línea para cerrar la conexión después de enviar la respuesta
        sys.exit(0)

if __name__ == "__main__":
    main()

