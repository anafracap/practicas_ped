import socket

def cliente():
    # Crear un socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conectar el socket al servidor
    cliente_socket.connect(('localhost', 8080))
    
    # Solicitar al usuario su nombre
    nombre = input("Ingrese su nombre: ")
    cliente_socket.sendall(nombre.encode('utf-8'))
    
    # Recibir mensajes del servidor y mostrarlos en pantalla
    while True:
        mensaje = cliente_socket.recv(1024)
        print(mensaje.decode('utf-8'))

if __name__ == "__main__":
    cliente()
