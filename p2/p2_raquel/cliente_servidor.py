import time
import multiprocessing

def servidor(pipe):
    while True:
        # Esperar a que el cliente se conecte
        pipe.recv()

        # Enviar la fecha y hora al cliente
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pipe.send(fecha_hora.encode('utf-8'))
        time.sleep(1)

if __name__ == '__main__':
    # Crear la tubería
    conexion_servidor, conexion_cliente = multiprocessing.Pipe()

    # Iniciar el servidor
    proceso_servidor = multiprocessing.Process(target=servidor, args=(conexion_servidor,))
    proceso_servidor.start()

    # Conectar el cliente
    conexion_cliente.send("Conectar")

    while True:
        # Leer y mostrar la fecha y hora recibida del servidor
        fecha_hora = conexion_cliente.recv().decode('utf-8').strip()
        print("Fecha y hora del servidor:", fecha_hora)
