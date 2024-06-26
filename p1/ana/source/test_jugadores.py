import unittest, pytest
from bolos import Juego

class TestClassJugadores(unittest.TestCase):
    def test_partida_un_jugador (self):
        jugadores = ['Pepe']
        juego = Juego(jugadores)
        self.assertEqual(juego.ver_jugadores(), jugadores)
    
    def test_partida_varios_jugadores (self):
        jugadores = ['Pepe', 'Paco']
        juego = Juego(jugadores)
        self.assertEqual(juego.ver_jugadores(), jugadores)

    def test_partida_sin_jugadores (self):
        jugadores = []
        with pytest.raises(Exception, match='NecesitoJugadores'):
            juego = Juego(jugadores)

    def test_partida_no_terminada_un_jugador (self):
        jugadores = ['Pepe']
        juego = Juego(jugadores)
        self.assertFalse(juego.esta_terminada_la_partida('Pepe'))

    def test_primera_partida_un_jugador_todo_0 (self):
        jugadores = ['Pepe']
        juego = Juego(jugadores)
        for i in range(10):
            juego.jugar_ronda('Pepe', 0, 0)
        self.assertTrue(juego.esta_terminada_la_partida('Pepe'))

    def test_primera_partida_un_jugador_todo_0_contador (self):
        jugadores = ['Pepe']
        juego = Juego(jugadores)
        for i in range(10):
            juego.jugar_ronda('Pepe', 0, 0)
        self.assertEqual(juego.ver_contador('Pepe'), [0])

    def test_segunda_partida_un_jugador_contador (self):
        jugadores = ['Pepe']
        juego = Juego(jugadores)
        for i in range(10):
            juego.jugar_ronda('Pepe', 1, 0)
        self.assertEqual(juego.ver_contador('Pepe'), [10])

    def test_partida_varios_jugadores_contador_diferente (self):
        jugadores = ['Pepe', 'Paco']
        juego = Juego(jugadores)
        for i in range(10):
            juego.jugar_ronda('Pepe', 1, 0)
            juego.jugar_ronda('Paco', 0, 0)
        self.assertEqual(juego.ver_contador(jugadores), [10,0])

    def test_partida_varios_jugadores_un_solo_contador (self):
        jugadores = ['Pepe', 'Paco']
        juego = Juego(jugadores)
        for i in range(10):
            juego.jugar_ronda('Pepe', 1, 0)
            juego.jugar_ronda('Paco', 0, 0)
        self.assertEqual(juego.ver_contador('Paco'), [0])

    def test_manterner_el_orden_de_jugadas (self):
        jugadores = ['Pepe', 'Paco']
        juego = Juego(jugadores)
        with pytest.raises(Exception, match='NoEsTuTurno'):
            juego.jugar_ronda('Paco', 0, 0)

    def test_manterner_el_orden_de_jugadas_en_medio_de_la_partida (self):
        jugadores = ['Pepe', 'Paco']
        juego = Juego(jugadores)
        for i in range(5):
            juego.jugar_ronda('Pepe', 1, 0)
            juego.jugar_ronda('Paco', 0, 0)
        with pytest.raises(Exception, match='NoEsTuTurno'):
            juego.jugar_ronda('Paco', 0, 0)
        
    def test_jugador_no_en_partida (self):
        jugadores = ['Pepe', 'Paco']
        juego = Juego(jugadores)
        with pytest.raises(Exception, match='NoEstasEnLaPartida'):
            juego.jugar_ronda('Pedro', 0, 0)