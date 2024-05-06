import os
import sys
from datetime import datetime
import time  # Importar el módulo time

def main():
    # Crear una tubería con nombre (pipe)
    pipe_name = 'pipe_servidor_fecha_hora'
    os.mkfifo(pipe_name)

    try:
        # Abrir la tubería para lectura
        with open(pipe_name, 'r') as pipe_in:
            while True:
                # Leer la petición del cliente (no se usa en este caso)

                # Obtener la fecha y hora actual
                now = datetime.now()
                # Formatear la fecha y hora en el formato deseado
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                
                # Enviar la fecha y hora al cliente
                print(date_time_str)

                # Esperar un segundo para mantener la precisión mínima
                time.sleep(1)

    finally:
        # Eliminar la tubería
        os.unlink(pipe_name)

if __name__ == "__main__":
    main()

