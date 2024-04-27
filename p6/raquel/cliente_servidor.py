import socket
import time
import multiprocessing

# Función para el servidor
def servidor():
    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar el socket a una dirección y puerto
    servidor_socket.bind(('localhost', 8080))

    # Escuchar conexiones entrantes
    servidor_socket.listen(5)

    print("Servidor listo para recibir conexiones en localhost:8080")

    while True:
        # Esperar a que un cliente se conecte
        cliente_socket, cliente_direccion = servidor_socket.accept()
        print("Cliente conectado:", cliente_direccion)

        try:
            # Enviar la fecha y hora al cliente
            fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cliente_socket.sendall(fecha_hora.encode('utf-8'))
        finally:
            # Cerrar la conexión con el cliente
            cliente_socket.close()

# Función para el cliente
def cliente():
    # Crear un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar el socket al servidor
        cliente_socket.connect(('localhost', 8080))

        # Recibir la fecha y hora del servidor
        data = cliente_socket.recv(1024)
        print("Fecha y hora del servidor:", data.decode('utf-8'))
    finally:
        # Cerrar la conexión con el servidor
        cliente_socket.close()

if __name__ == "__main__":
    # Ejecutar el servidor en un proceso separado
    proceso_servidor = multiprocessing.Process(target=servidor)
    proceso_servidor.start()

    # Esperar un momento para asegurar que el servidor está listo para recibir conexiones
    time.sleep(1)

    # Ejecutar el cliente
    cliente()
