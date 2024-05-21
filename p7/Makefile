address=127.0.0.1
port=1234

all: servidor cliente
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

servidor:
	@python3 servidor.py $(port)

cliente:
	@python3 cliente.py $(address) $(port)

test:
	@python3 test_server.py
