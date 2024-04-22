file=ejemplo.txt
port=1235

all: ervidor cliente
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

servidor:
	@python3 servidor_ap1.py $(port)

cliente:
	@python3 cliente_ap1.py $(file) $(port)
