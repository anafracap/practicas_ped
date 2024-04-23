address=192.168.56.29
port=1234

all: servidor cliente
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

servidor:
	python3 servidor_hora.py $(address) $(port)

cliente:
	python3 cliente_hora.py $(address) $(port)
