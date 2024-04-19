
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int fd[2];
    char path[100];
    char buffer[1024];

    // Aquí creo la tubería
    if (pipe(fd) == -1) {
        perror("Error al crear la tuberia");
        exit(EXIT_FAILURE);
    }

    // Solicitamos al usuario el path del fichero 
    printf("Ingresa el path del fichero aquí: ");
    scanf("%s", path);

    // Enviamos el path que nos han dado al servidor
    write(fd[1], path, sizeof(path));

    // Aquí leemos la respuesta del servidor
    read(fd[0], buffer, sizeof(buffer));
    printf("Respuesta del servidor: %s\n", buffer);

    return 0;
}