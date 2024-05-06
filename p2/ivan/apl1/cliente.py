import os
import sys

def main():
    # Nombre de la tubería
    pipe_name = 'pipe_servidor'

    # Path del archivo a solicitar
    file_path = os.path.join(os.getcwd(), 'documento.txt')

    try:
        # Abrir la tubería para escritura
        with open(pipe_name, 'w') as pipe_out:
            # Enviar el path del archivo al servidor
            pipe_out.write(file_path + '\n')

    except FileNotFoundError:
        print("Error: No se pudo conectar con el servidor.")
        sys.exit(1)

if __name__ == "__main__":
    main()

