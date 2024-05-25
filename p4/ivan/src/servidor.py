import os
import socket
import datetime

SOCKET_PATH = "/tmp/uds_socket_12345"

def handle_client(client_socket):
    now = datetime.datetime.now()
    response = now.strftime("%Y-%m-%d %H:%M:%S")
    client_socket.send(response.encode())
    client_socket.close()

def main():
    if os.path.exists(SOCKET_PATH):
        os.remove(SOCKET_PATH)

    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(SOCKET_PATH)
    server_socket.listen(5)

    print(f"Servidor escuchando en {SOCKET_PATH}")

    try:
        while True:
            client_socket, _ = server_socket.accept()
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server_socket.close()
        os.remove(SOCKET_PATH)

if __name__ == "__main__":
    main()

