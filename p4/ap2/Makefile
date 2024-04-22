socket=/tmp/ped4_p4_ap2_server.sock

all: servidor cliente
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

servidor:
	python3 servidor_hora.py $(socket)

cliente:
	python3 cliente_hora.py $(socket)
