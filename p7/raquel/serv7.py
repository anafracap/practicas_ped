import socket
import threading

# Diccionario para almacenar las conexiones de los clientes
clientes = {}

# Función para manejar las conexiones de los clientes
def manejar_cliente(cliente_socket, cliente_direccion, cliente_nombre):
    while True:
        # Esperar mensajes del cliente
        mensaje = cliente_socket.recv(1024)
        if not mensaje:
            break
        
        # Reenviar el mensaje a todos los clientes conectados
        mensaje_enviado = f"{cliente_nombre}: {mensaje.decode('utf-8')}"
        for nombre, socket_cliente in clientes.items():
            if socket_cliente != cliente_socket:
                try:
                    socket_cliente.sendall(mensaje_enviado.encode('utf-8'))
                except:
                    # Eliminar el cliente si hay algún problema de conexión
                    del clientes[nombre]
    
    # Cerrar la conexión con el cliente al salir del bucle
    cliente_socket.close()
    del clientes[cliente_nombre]
    print(f"Cliente desconectado: {cliente_nombre}")

def servidor():
    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Enlazar el socket al puerto
    servidor_socket.bind(('localhost', 8080))
    
    # Escuchar conexiones entrantes
    servidor_socket.listen(5)
    print("Servidor listo para recibir conexiones en localhost:8080")
    
    while True:
        # Esperar a que el cliente se conecte
        cliente_socket, cliente_direccion = servidor_socket.accept()
        
        # Recibir el nombre del cliente
        nombre = cliente_socket.recv(1024).decode('utf-8')
        
        # Verificar si el nombre ya está en uso
        if nombre in clientes:
            mensaje = "El nombre ya está en uso. Por favor, elija otro."
            cliente_socket.sendall(mensaje.encode('utf-8'))
            cliente_socket.close()
            continue
        
        # Añadir el cliente al diccionario de clientes
        clientes[nombre] = cliente_socket
        
        # Iniciar un hilo para manejar la conexión con el cliente
        cliente_thread = threading.Thread(target=manejar_cliente, args=(cliente_socket, cliente_direccion, nombre))
        cliente_thread.start()

if __name__ == "__main__":
    servidor()
