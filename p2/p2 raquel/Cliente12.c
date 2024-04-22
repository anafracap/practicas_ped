import os

# Creación de tuberías
client_to_server_read, client_to_server_write = os.pipe()
server_to_client_read, server_to_client_write = os.pipe()

# Creación del proceso hijo
pid = os.fork()

if pid:  # Proceso padre (servidor)
    # Cierre de extremos no necesarios
    os.close(client_to_server_read)
    os.close(server_to_client_write)

    # Recepción del mensaje del cliente (ruta del archivo)
    file_path = os.read(client_to_server_write, 1024).decode('utf-8').strip()

    # Lectura del archivo y envío al cliente
    with open(file_path, 'r') as file:
        for line in file:
            os.write(server_to_client_read, line.encode('utf-8'))

    # Cierre de extremos restantes
    os.close(client_to_server_write)
    os.close(server_to_client_read)

else:  # Proceso hijo (cliente)
    # Cierre de extremos no necesarios
    os.close(client_to_server_write)
    os.close(server_to_client_read)

    # Envío de la ruta del archivo al servidor
    file_path = "/Users/anafraile/Clases/uni-clases/23-24/sem2/ped/practicas/p2/ana/aplicacion1/ejemplo.txt"
    os.write(client_to_server_read, file_path.encode('utf-8'))

    # Lectura de la respuesta del servidor
    response = os.read(server_to_client_write, 1024).decode('utf-8').strip()
    print(response)

    # Cierre de extremos restantes
    os.close(client_to_server_read)
    os.close(server_to_client_write)
