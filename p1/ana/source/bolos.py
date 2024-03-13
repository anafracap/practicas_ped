class Partida():
    def iniciar_partida(self):
        return None

    def jugar_ronda(self, turno1, turno2 = None, turno3 = None):
        ronda = self._num_ronda
        if self.esta_terminada_la_partida():
            raise Exception('NoJuegesMas')
        self._tirar_ronda(turno1)
        if turno2 != None:
            if turno2 == '/':
                turno2 = 10 - turno1
                self._ronda_semi(turno2)
            elif isinstance(turno1, int) and (turno1 + turno2) > 10:
                raise Exception('DemasiadosBolos')
            else:
                self._tirar_ronda(turno2)
        if turno3 != None:
            if isinstance(turno2, int) and (turno2 + turno3) > 10:
                raise Exception('DemasiadosBolos')
            self._tirar_ronda(turno3)
        self._num_ronda = ronda + 1
       

    def _tirar_ronda(self, turno):
        print('tiradas: ', self._tiradas_a_sumar)
        print('----------------resultado: ', turno, self._contador)
        if self._tiradas_a_sumar > 0 or self._tirada_bonus_2 > 0:
            t = turno
            if t == 'X':
                t = 10
            self._sumar_bonus(t)
        if isinstance(turno, str):
            self._calcular_tiradas_raras(turno)
        else:
            self._contador = self._contador + turno

    def _ronda_semi(self, turno):
        if self._tiradas_a_sumar > 0 or self._tirada_bonus_2 > 0:
            self._sumar_bonus(turno)
        self._calcular_tiradas_raras(turno)

    def _sumar_bonus(self, turno):
        if self._tiradas_a_sumar > 0:
            self._tiradas_a_sumar = self._tiradas_a_sumar - 1   
            self._contador = self._contador + turno    
        if self._tirada_bonus_2 > 0:
            self._tirada_bonus_2 = self._tirada_bonus_2 - 1
            self._contador = self._contador + turno

    def _calcular_tiradas_raras(self, turno):
        if turno == 'X':
            if self._tiradas_a_sumar > 0:
                self._tirada_bonus_2 = self._tirada_bonus_2 +2
            else:
                self._tiradas_a_sumar = self._tiradas_a_sumar + 2
            self._contador = self._contador + 10
        elif isinstance(turno, int):
            self._tiradas_a_sumar = self._tiradas_a_sumar + 1
            self._contador = self._contador + turno

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
        self._tirada_bonus_2 = 0