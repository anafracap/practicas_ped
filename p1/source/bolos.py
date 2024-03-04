class Partida():
    def iniciar_partida(self):
        return None

    def jugar_ronda(self):
        global num_ronda
        if num_ronda == 10:
            raise Exception('NoJuegesMas')
        num_ronda = num_ronda + 1
        return None

    def esta_terminada_la_partida(self):
        global num_ronda
        if num_ronda < 10:
            return False
        if num_ronda == 10: 
            return True


    def __init__(self):
        global num_ronda
        num_ronda = 0
        return None