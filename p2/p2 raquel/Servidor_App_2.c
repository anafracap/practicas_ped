#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main() {
    int fd[2];
    char datetime[100];
    time_t rawtime;
    struct tm *info;

    // Aquí se crea la tubería
    if (pipe(fd) == -1) {
        perror("Error en la creación de la tuberia");
        exit(EXIT_FAILURE);
    }

    // Aquí conseguimos la fecha y hora actual
    time(&rawtime);
    info = localtime(&rawtime);

    // Modificación de la fecha y hora
    strftime(datetime, sizeof(datetime), "%Y-%m-%d %H:%M:%S", info);

    // Aquí enviamos la fecha y hora al cliente
    write(fd[1], datetime, sizeof(datetime));

    return 0;
}