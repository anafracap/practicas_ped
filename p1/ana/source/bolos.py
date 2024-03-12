class Partida():
    def iniciar_partida(self):
        return None

    def jugar_ronda(self, turno1, turno2 = None):
        ronda = self._num_ronda
        if ronda == 10:
            raise Exception('NoJuegesMas')
        self._tirar_ronda(turno1)
        if turno2 != None:
            self._tirar_ronda(turno2)
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
            print('-------------------------------------------------HOLA')
            self._contador = self._contador + 10
            return None
        elif turno == '/':
            self._tiradas_a_sumar = self._tiradas_a_sumar + 1
            self._contador = self._contador + 10
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
        self._tirada_bonus_2 = 0