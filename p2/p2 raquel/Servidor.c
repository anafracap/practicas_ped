
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd[2];
    char path[100];
    char buffer[1024];
    int file_descriptor;

    // Crear la tubería
    if (pipe(fd) == -1) {
        perror("Error al crear la tuberia");
        exit(EXIT_FAILURE);
    }

    // Leer el path del archivo enviado por el cliente
    read(fd[0], path, sizeof(path));

    // Abrir y leer el archivo
    file_descriptor = open(path, O_RDONLY);
    if (file_descriptor == -1) {
        // Enviar mensaje de error al cliente
        write(fd[1], "Error: No se pudo abrir el archivo", sizeof("Error: No se pudo abrir el archivo"));
    } else {
        // Leer el contenido del archivo
        read(file_descriptor, buffer, sizeof(buffer));
        // Enviar el contenido del archivo al cliente
        write(fd[1], buffer, sizeof(buffer));
        // Cerrar el archivo
        close(file_descriptor);
    }

    return 0;
}