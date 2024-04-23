import os
import sys
import multiprocessing

def servidor(pipe):
    while True:
        path = pipe.recv()
        try:
            with open(path, 'r') as f:
                contenido = f.read()
            pipe.send(contenido)
        except FileNotFoundError:
            pipe.send("Error: El archivo no existe.")
        except Exception as e:
            pipe.send(f"Error: {str(e)}")

def cliente(pipe):
    path = input("Introduce la ruta del archivo: ")
    pipe.send(path)
    respuesta = pipe.recv()
    print(respuesta)

if __name__ == "__main__":
    # Creamos la tubería
    pipe_servidor, pipe_cliente = multiprocessing.Pipe()

    # Creamos los procesos cliente y servidor
    proc_servidor = multiprocessing.Process(target=servidor, args=(pipe_servidor,))
    proc_cliente = multiprocessing.Process(target=cliente, args=(pipe_cliente,))

    # Iniciamos los procesos
    proc_servidor.start()
    proc_cliente.start()

    # Esperamos a que los procesos terminen
    proc_cliente.join()
    proc_servidor.terminate()
