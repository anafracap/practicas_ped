file=ejemplo.txt
socket=/tmp/ped4_p4_ap1_server

servidor:
	@python3 servidor_ap1.py $(socket)

cliente:
	@python3 cliente_ap1.py $(file) $(socket)

inf:
	while true; do python3 cliente_ap1.py $(file) $(socket); done