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

def cliente(pipe, path):
    try:
        pipe.send(path)
        respuesta = pipe.recv()
        print(respuesta)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    # Comprueba si se proporciona la ruta del archivo como argumento de línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python cliente_servidor.py <ruta_del_archivo>")
        sys.exit(1)

    # Obtiene la ruta del archivo desde los argumentos de línea de comandos
    ruta_del_archivo = sys.argv[1]

    # Creamos la tubería
    pipe_servidor, pipe_cliente = multiprocessing.Pipe()

    # Creamos los procesos cliente y servidor
    proc_servidor = multiprocessing.Process(target=servidor, args=(pipe_servidor,))
    proc_cliente = multiprocessing.Process(target=cliente, args=(pipe_cliente, ruta_del_archivo))

    # Iniciamos los procesos
    proc_servidor.start()
    proc_cliente.start()

    # Esperamos a que ambos procesos terminen
    proc_servidor.join()
    proc_cliente.join()
