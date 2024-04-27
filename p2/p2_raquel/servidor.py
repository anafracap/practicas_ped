import time
import multiprocessing

def enviar_fecha_hora(pipe):
    print("Proceso hijo iniciado.")
    while True:
        # Leer la fecha y hora del sistema
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # Enviar la fecha y hora al cliente a través de la tubería
        pipe.send(fecha_hora.encode('utf-8'))
        time.sleep(1)

if __name__ == '__main__':
    # Crear la tubería
    conexion_servidor, conexion_cliente = multiprocessing.Pipe()
    # Crear el proceso para enviar datos al cliente
    proceso_servidor = multiprocessing.Process(target=enviar_fecha_hora, args=(conexion_servidor,))
    proceso_servidor.start()
