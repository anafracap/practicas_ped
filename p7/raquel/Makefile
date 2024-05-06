# Makefile para compilar y ejecutar el servidor y el cliente

# Nombre de los archivos de servidor y cliente
SERVER_FILE = serv7.py
CLIENT_FILE = cli7.py

# Comando para ejecutar el servidor
SERVER_CMD = python $(SERVER_FILE)

# Comando para ejecutar el cliente
CLIENT_CMD = python $(CLIENT_FILE)

.PHONY: server client

# Regla para ejecutar el servidor
server:
	@echo "Ejecutando el servidor..."
	$(SERVER_CMD)

# Regla para ejecutar el cliente
client:
	@echo "Ejecutando el cliente..."
	$(CLIENT_CMD)
