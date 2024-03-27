class Partida():
    def jugar_ronda(self, turno1, turno2 = None, turno3 = None):
        ronda = self._num_ronda
        if self.esta_terminada_la_partida():
            raise Exception('NoJuegesMas')
        elif not isinstance(turno1, int) and turno1 != '/' and turno1 != 'X':
            raise Exception('NomenclaturaIncorrecta')
        elif isinstance(turno1, int) and turno2 == None and turno3 == None:
            raise Exception('NoUnaBolaSuelta')
        elif isinstance(turno1, int) and turno1 > 9:
            raise Exception('NomenclaturaIncorrecta')
        elif ronda < 9:  # Excepciones normales
            if turno3:
                raise Exception('DemasiadasBolasLanzadas')
            elif turno1 == '/':
                raise Exception('SemiExtraviado')
            elif turno2 == 'X':
                raise Exception('PlenoExtraviado')
            elif turno1 == 'X' and isinstance(turno2, int):
                raise Exception('BolosExtraviados')
        self._tirar_ronda(turno1)
        if turno2 != None:
            if turno2 == '/':
                if turno1 == 'X':
                    raise Exception('SemiExtraviado')
                turno2 = 10 - turno1
                self._ronda_semi(turno2)
            elif turno2 == 'X':
                if isinstance(turno1, int):
                    raise Exception('PlenoExtraviado')
                self._sumar_bonus(10)
            elif not isinstance(turno2, int):
                raise Exception('NomenclaturaIncorrecta')
            elif isinstance(turno1, int) and (turno1 + turno2) > 10:
                raise Exception('DemasiadosBolos')
            elif turno2 > 9:
                raise Exception('NomenclaturaIncorrecta')
            else:
                self._tirar_ronda(turno2)
        if turno3 != None:
            if turno3 == '/':
                turno3 = 10 - turno2
                self._ronda_semi(turno3)
            elif turno3 == 'X':
                self._sumar_bonus(10)
            elif not isinstance(turno3, int):
                raise Exception('NomenclaturaIncorrecta')
            elif isinstance(turno2, int) and (turno2 + turno3) > 10:
                raise Exception('DemasiadosBolos')
            elif turno3 > 9:
                raise Exception('NomenclaturaIncorrecta')
            else: self._tirar_ronda(turno3)
        self._num_ronda = ronda + 1
       

    def _tirar_ronda(self, turno):
        if self._tiradas_a_sumar > 0 or self._tirada_bonus_2 > 0:
            t = turno
            if t == 'X':
                t = 10
            self._sumar_bonus(t)
        if isinstance(turno, str):
            self._calcular_tiradas_raras(turno)
        elif turno < 0:
            raise Exception('NoTrampasNegativas')
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
        self._esperando_bonus_pleno = self._esperando_bonus_pleno - 1
        self._esperando_bonus_semi = self._esperando_bonus_semi - 1

    def _calcular_tiradas_raras(self, turno):
        if turno == 'X':
            if self._tiradas_a_sumar > 0:
                self._tirada_bonus_2 = self._tirada_bonus_2 +2
            else:
                self._tiradas_a_sumar = self._tiradas_a_sumar + 2
            self._esperando_bonus_pleno = 2
            self._contador = self._contador + 10
        elif isinstance(turno, int):
            self._tiradas_a_sumar = self._tiradas_a_sumar + 1
            self._contador = self._contador + turno
            self._esperando_bonus_semi = 1

    def esta_terminada_la_partida(self):
        if self._num_ronda < 10:
            return False
        if self._num_ronda == 10: 
            return True

    def ver_contador(self):
        if self._esperando_bonus_pleno < 1 and self._esperando_bonus_semi < 1:
            return self._contador
        elif self._num_ronda < 10:
            return "Todavía no se sabe"
        else: return self._contador


    def __init__(self):
        self._num_ronda = 0
        self._contador = 0
        self._tiradas_a_sumar = 0
        self._tirada_bonus_2 = 0
        self._esperando_bonus_pleno = 0
        self._esperando_bonus_semi = 0