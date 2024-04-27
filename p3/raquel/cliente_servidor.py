import socket
import time
import multiprocessing

def servidor():
    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar el socket al puerto
    servidor_socket.bind(('localhost', 8080))

    # Escuchar conexiones entrantes
    servidor_socket.listen(1)

    while True:
        # Esperar a que el cliente se conecte
        print("Esperando conexión...")
        cliente_socket, cliente_direccion = servidor_socket.accept()

        # Enviar la fecha y hora al cliente
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cliente_socket.sendall(fecha_hora.encode('utf-8'))

        # Esperar a que el cliente confirme la recepción
        confirmacion = cliente_socket.recv(1024)

        # Cerrar la conexión
        cliente_socket.close()

        time.sleep(1)

def cliente():
    # Crear un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el socket al servidor
    cliente_socket.connect(('localhost', 8080))

    while True:
        # Leer y mostrar la fecha y hora recibida del servidor
        data = cliente_socket.recv(1024)
        print("Fecha y hora del servidor:", data.decode('utf-8'))

        # Enviar una confirmación al servidor
        cliente_socket.sendall(b"Listo")

        time.sleep(1)

if __name__ == '__main__':
    # Iniciar el servidor y el cliente en procesos separados
    proceso_servidor = multiprocessing.Process(target=servidor)
    proceso_servidor.start()

    proceso_cliente = multiprocessing.Process(target=cliente)
    proceso_cliente.start()

    # Esperar a que los procesos terminen (esto nunca ocurrirá porque los procesos se ejecutan indefinidamente)
    proceso_servidor.join()
    proceso_cliente.join()

