class Partida():
    def iniciar_partida(self):
        return None

    def jugar_ronda(self, turno1 = None, turno2 = None):
        ronda = self._num_ronda
        if ronda == 10:
            raise Exception('NoJuegesMas')
        self._num_ronda = ronda + 1
        return None

    def esta_terminada_la_partida(self):
        self._num_ronda
        if self._num_ronda < 10:
            return False
        if self._num_ronda == 10: 
            return True

    def ver_contador(self):
        return 10


    def __init__(self):
        self._num_ronda = 0
        self._contador = 0