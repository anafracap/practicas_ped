import os
import sys

def main():
    # Nombre de la tubería
    pipe_name = 'pipe_servidor_fecha_hora'

    try:
        # Abrir la tubería para escritura
        with open(pipe_name, 'w') as pipe_out:
            # Enviar una solicitud vacía al servidor (no se usa en este caso)
            pipe_out.write('\n')

        # Leer la respuesta del servidor e imprimir en la salida estándar
        with open(pipe_name, 'r') as pipe_in:
            response = pipe_in.readline().strip()
            print("Fecha y hora del servidor:", response)

    except FileNotFoundError:
        print("Error: No se pudo conectar con el servidor.")
        sys.exit(1)

if __name__ == "__main__":
    main()

