import os
import sys

def main():
    # Crear una tubería con nombre (pipe)
    pipe_name = 'pipe_servidor'
    os.mkfifo(pipe_name)

    try:
        # Abrir la tubería para lectura
        with open(pipe_name, 'r') as pipe_in:
            while True:
                # Leer el path del archivo enviado por el cliente
                file_path = pipe_in.readline().strip()

                if not file_path:
                    break

                # Intentar abrir el archivo y enviar su contenido
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(contents)
                except FileNotFoundError:
                    print(f"Error: El archivo '{file_path}' no existe")
    finally:
        # Eliminar la tubería
        os.unlink(pipe_name)

if __name__ == "__main__":
    main()

