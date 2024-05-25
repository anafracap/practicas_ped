import socket

SOCKET_PATH = "/tmp/uds_socket_12345"

def main():
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client_socket.connect(SOCKET_PATH)

    response = client_socket.recv(256).decode()
    print(f"Fecha y hora recibida: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()

