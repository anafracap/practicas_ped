class Partida():
    def iniciar_partida(self):
        return None

    def jugar_ronda(self, turno1, turno2 = None):
        ronda = self._num_ronda
        if ronda == 10:
            raise Exception('NoJuegesMas')
        elif isinstance(turno1, str):
            self._contador = 10
            return None
        else:
            self._num_ronda = ronda + 1
            self._contador = self._contador + turno1 + turno2
            return None

    def esta_terminada_la_partida(self):
        if self._num_ronda < 10:
            return False
        if self._num_ronda == 10: 
            return True

    def ver_contador(self):
        return self._contador


    def __init__(self):
        self._num_ronda = 0
        self._contador = 0