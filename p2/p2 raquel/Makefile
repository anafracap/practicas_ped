# Makefile

# Compilador y opciones
CC = python3
CFLAGS = -u

# Objetivo predeterminado
default: cliserv2

# Objetivo para el cliente y el servidor
cliserv2: cliente_servidor_ficheros.py
    $(CC) $(CFLAGS) cliente_servidor_ficheros.py cli2

cli2: cliente_servidor_ficheros.py
    $(CC) $(CFLAGS) cliente_servidor_ficheros.py cli2

serv2: cliente_servidor_ficheros.py
    $(CC) $(CFLAGS) cliente_servidor_ficheros.py serv2

# Limpiar archivos generados
clean:
    rm -f cli2 serv2 cliserv2
