class Partida():
    global contador
    contador = 0
    def iniciar_partida(self):
        return None

    def jugar_ronda(self):
        global contador
        contador = contador + 1
        return None

    def esta_terminada_la_partida(self):
        global contador
        if contador < 10:
            return False
        if contador == 10: 
            return True


    def __init__(self):
        return None