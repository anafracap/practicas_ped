import time
import multiprocessing

def servidor(conn):
    while True:
        # Enviar la fecha y hora al cliente
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        conn.send(fecha_hora)

        # Esperar a que el cliente confirme la recepción
        confirmacion = conn.recv()

        time.sleep(1)

def cliente(conn):
    while True:
        # Leer y mostrar la fecha y hora recibida del servidor
        data = conn.recv()
        print("Fecha y hora del servidor:", data)

        # Enviar una confirmación al servidor
        conn.send("Listo")

        time.sleep(1)

if __name__ == '__main__':
    # Crear una conexión entre procesos
    parent_conn, child_conn = multiprocessing.Pipe()

    # Iniciar el servidor y el cliente en procesos separados
    proceso_servidor = multiprocessing.Process(target=servidor, args=(child_conn,))
    proceso_servidor.start()

    proceso_cliente = multiprocessing.Process(target=cliente, args=(parent_conn,))
    proceso_cliente.start()

    # Esperar a que los procesos terminen (esto nunca ocurrirá porque los procesos se ejecutan indefinidamente)
    proceso_servidor.join()
    proceso_cliente.join()
