class Partida():
    def iniciar_partida(self):
        return None

    def jugar_ronda(self, turno1, turno2 = None):
        ronda = self._num_ronda
        if ronda == 10:
            raise Exception('NoJuegesMas')
        if self._tiradas_a_sumar > 0:
            self._tiradas_a_sumar = self._tiradas_a_sumar - 1
            self._contador = self._contador + turno1
        if self._tiradas_a_sumar > 0:
            self._tiradas_a_sumar = self._tiradas_a_sumar - 1
            self._contador = self._contador + turno2
        if isinstance(turno1, str):
            if turno1 == 'X':
                self._tiradas_a_sumar = 2
                self._contador = self._contador + 10
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
        self._tiradas_a_sumar = 0