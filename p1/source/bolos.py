class Partida():
    global contador
    def iniciar_partida(self):
        return None

    def jugar_ronda(self):
        global contador
        if contador == 10:
            raise Exception('NoJuegesMas')
        contador = contador + 1
        return None

    def esta_terminada_la_partida(self):
        global contador
        if contador < 10:
            return False
        if contador == 10: 
            return True


    def __init__(self):
        global contador
        contador = 0
        return None