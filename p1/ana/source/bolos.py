class Partida():
    def jugar_ronda(self, turno1 = None, turno2 = None, turno3 = None):
        ronda = self._num_ronda
        if self.esta_terminada_la_partida():
            raise Exception('NoJuegesMas')
        elif not isinstance(turno1, int) and turno1 != '/' and turno1 != 'X':
            if turno2 == None and turno3 == None:
                raise Exception('LanceUnaBola')
            else:
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
        self._procesar_turno_2(turno1, turno2)
        self._procesar_turno_3(turno2, turno3)
        
        self._num_ronda = ronda + 1
       
    def _procesar_turno_2(self, turno1, turno2):
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

    def _procesar_turno_3(self, turno2, turno3):
        if turno3 != None:
            if turno2 == None:
                raise Exception('NomenclaturaIncorrecta')
            elif turno3 == '/':
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


    def __init__(self, jugador = None):
        self._num_ronda = 0
        self._contador = 0
        self._tiradas_a_sumar = 0
        self._tirada_bonus_2 = 0
        self._esperando_bonus_pleno = 0
        self._esperando_bonus_semi = 0
        self._jugador = jugador

class Juego():
    def ver_jugadores(self):
        return self._jugadores

    def jugar_ronda(self, jugador, turno1, turno2):
        if not jugador in self._jugadores:
            raise Exception('NoEstasEnLaPartida')
        else:
            index = self._jugadores.index(jugador)
            if index != self._a_quien_le_toca:
                raise Exception('NoEsTuTurno')
            else:
                if self._a_quien_le_toca < len(self._jugadores) - 1:
                    self._a_quien_le_toca = self._a_quien_le_toca + 1
                else:
                    self._a_quien_le_toca = 0
                return self._partidas[index].jugar_ronda(turno1, turno2)
    
    def ver_contador(self, jugadores):
        contadores = []
        if isinstance(jugadores, str):
            index = self._jugadores.index(jugadores)
            contadores.append(self._partidas[index].ver_contador())
        else:
            for jugador in jugadores:
                index = self._jugadores.index(jugador)
                contadores.append(self._partidas[index].ver_contador())
        return contadores

    def esta_terminada_la_partida(self, jugadores):
        if isinstance(jugadores, str):
            index = self._jugadores.index(jugadores)
            return self._partidas[index].esta_terminada_la_partida()
        else:
            for jugador in jugadores:
                index = self._jugadores.index(jugador)
                return self._partidas[index].esta_terminada_la_partida()

    def __init__(self, jugadores):
        if not jugadores:
            raise Exception('NecesitoJugadores')
        self._jugadores = jugadores
        self._partidas = []
        for jugador in jugadores:
            partida = Partida(jugador)
            self._partidas.append(partida)
        self._a_quien_le_toca = 0