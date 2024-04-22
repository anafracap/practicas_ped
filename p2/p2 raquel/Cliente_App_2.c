#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int fd[2];
    char datetime[100];

    // Creación de la tubería aquí
    if (pipe(fd) == -1) {
        perror("Se ha producido un error al crear la tuberia");
        exit(EXIT_FAILURE);
    }

    // Leemos aquí la fecha y la hora del servidor
    read(fd[0], datetime, sizeof(datetime));
    printf("Fecha y hora del servidor recibida correctamente: %s\n", datetime);

    return 0;
}