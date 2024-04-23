address=127.0.0.1
port=1234

all: servidor cliente
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

servidor:
	python3 servidor_hora.py $(port)

cliente:
	python3 cliente_hora.py $(address) $(port)
