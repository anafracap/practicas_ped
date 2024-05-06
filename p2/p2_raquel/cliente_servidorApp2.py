import os
import sys
from multiprocessing import Process, Pipe

def servidor(conn):
    # Cerrar el extremo de escritura para evitar errores
    conn.close()
    
    data = conn.recv().decode('utf8').strip()
    print("Servidor: Recibido path del archivo:", data)
    try:
        with open(data, 'r') as file:
            contenido = file.read()
            conn.send(contenido.encode('utf8'))
            print("Servidor: Enviando contenido del archivo al cliente")
    except FileNotFoundError:
        error_msg = "Error: El archivo no existe"
        conn.send(error_msg.encode('utf8'))
        print("Servidor: Archivo no encontrado, enviando mensaje de error")

def cliente(conn, ruta_archivo):
    # Cerrar el extremo de lectura para evitar errores
    conn.close()

    # Enviar el path del archivo al servidor
    conn.send(ruta_archivo.encode('utf8'))
    print("Cliente: Enviando path del archivo al servidor:", ruta_archivo)

    # Leer la respuesta del servidor y mostrarla en la salida estándar
    response = conn.recv().decode('utf8')
    print("Cliente: Respuesta del servidor recibida:", response)
    sys.stdout.write(response)

if __name__ == "__main__":
    # Crear las tuberías
    servidor_conn, cliente_conn = Pipe()

    # Obtener la ruta del archivo del primer argumento pasado desde la línea de comandos
    ruta_archivo = sys.argv[1]

    # Crear procesos para el cliente y el servidor
    servidor_process = Process(target=servidor, args=(servidor_conn,))
    cliente_process = Process(target=cliente, args=(cliente_conn, ruta_archivo))

    # Iniciar los procesos
    servidor_process.start()
    cliente_process.start()

    # Esperar a que los procesos terminen
    servidor_process.join()
    cliente_process.join()

