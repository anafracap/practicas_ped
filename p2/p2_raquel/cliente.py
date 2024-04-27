import os
import time
import multiprocessing

def recibir_datos(pipe):
    while True:
        # Leer la fecha y hora enviada por el servidor
        fecha_hora = pipe.recv().strip()
        print("Fecha y hora del servidor:", fecha_hora)

if __name__ == '__main__':
    # Crear la tubería
    conexion_servidor, conexion_cliente = multiprocessing.Pipe()
    # Crear el proceso para recibir datos del servidor
    proceso_cliente = multiprocessing.Process(target=recibir_datos, args=(conexion_cliente,))
    proceso_cliente.start()
    
    while True:
        # Intentar conectarse al servidor
        try:
            conexion_servidor.send("Conexión establecida")
        except Exception as e:
            print("Error:", e)
        time.sleep(1)
