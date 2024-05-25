all: servidor cliente clean



servidor:
	python3 serv3.py &

cliente: 
	python3 cli3.py

clean:
	rm -f /tmp/fifo_cliente_grupo3 /tmp/fifo_servidor_grupo3
