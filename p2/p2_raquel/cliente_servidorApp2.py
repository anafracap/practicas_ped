import os
import sys

def servidor():
    # Cerrar los extremos que no se utilizan para evitar errores
    sys.argv[0] = "servidor"
    os.close(wdC)
    os.close(rdC)
    
    data = os.read(rdS, 100).decode('utf8').strip()
    print("Servidor: Recibido path del archivo:", data)
    try:
        with open(data, 'r') as file:
            contenido = file.read()
            os.write(wdS, contenido.encode('utf8'))
            print("Servidor: Enviando contenido del archivo al cliente")
    except FileNotFoundError:
        error_msg = "Error: El archivo no existe"
        os.write(wdS, error_msg.encode('utf8'))
        print("Servidor: Archivo no encontrado, enviando mensaje de error")

def cliente():
    # Cerrar los extremos que no se utilizan para evitar errores
    sys.argv[0] = "cliente"
    os.close(rdS)
    os.close(wdS)

    # Obtener la ruta del archivo del primer argumento pasado desde la línea de comandos
    ruta_archivo = sys.argv[1]

    # Enviar el path del archivo al servidor
    os.write(wdC, ruta_archivo.encode('utf8'))
    print("Cliente: Enviando path del archivo al servidor:", ruta_archivo)

    # Leer la respuesta del servidor y mostrarla en la salida estándar
    response = os.read(rdC, 1000).decode('utf8')
    print("Cliente: Respuesta del servidor recibida:", response)
    sys.stdout.write(response)

if __name__ == "__main__":
    # Crear las tuberías
    rdS, wdS = os.pipe()  # Cliente a servidor
    rdC, wdC = os.pipe()  # Servidor a cliente
    
    pid = os.fork()

    if pid:  # Proceso padre (servidor)
        servidor()
    else:  # Proceso hijo (cliente)
        cliente()
