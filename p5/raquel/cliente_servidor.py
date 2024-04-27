import socket
import time
import multiprocessing

# Función para el servidor
def servidor():
    # Crear un socket UDP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enlazar el socket a una dirección y puerto
    servidor_socket.bind(('localhost', 8080))

    print("Servidor listo para recibir conexiones en localhost:8080")

    while True:
        # Recibir datos del cliente
        data, cliente_direccion = servidor_socket.recvfrom(1024)
        print("Mensaje recibido del cliente:", data.decode('utf-8'))

        # Enviar la fecha y hora al cliente
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        servidor_socket.sendto(fecha_hora.encode('utf-8'), cliente_direccion)

# Función para el cliente
def cliente():
    # Crear un socket UDP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Dirección del servidor
    servidor_direccion = ('localhost', 8080)

    # Enviar un mensaje al servidor
    mensaje = "Hora, por favor"
    cliente_socket.sendto(mensaje.encode('utf-8'), servidor_direccion)

    # Recibir la fecha y hora del servidor
    data, _ = cliente_socket.recvfrom(1024)
    print("Fecha y hora del servidor:", data.decode('utf-8'))

if __name__ == "__main__":
    # Ejecutar el servidor en un proceso separado
    proceso_servidor = multiprocessing.Process(target=servidor)
    proceso_servidor.start()

    # Esperar un momento para asegurar que el servidor está listo para recibir conexiones
    time.sleep(1)

    # Ejecutar el cliente
    cliente()
