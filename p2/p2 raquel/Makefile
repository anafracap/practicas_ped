CC = gcc
CFLAGS = -Wall -Wextra -pedantic

all: cli2 serv2

cli2: cli2.c
    $(CC) $(CFLAGS) -o Cliente_App_2 Cliente_App_2.c

serv2: serv2.c
    $(CC) $(CFLAGS) -o Servidor_App_2 serv2.c

clean:
    rm -f cli2 serv2
