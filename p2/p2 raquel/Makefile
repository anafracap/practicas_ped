CC = gcc
CFLAGS = -Wall -Wextra -pedantic

all: cli2 serv2

cli2: cli2.c
    $(CC) $(CFLAGS) -o cli2 cli2.c

serv2: serv2.c
    $(CC) $(CFLAGS) -o serv2 serv2.c

clean:
    rm -f cli2 serv2
