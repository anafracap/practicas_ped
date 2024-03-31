import unittest, pytest
from bolos import Juego

class TestClass(unittest.TestCase):
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
        self.assertEqual(juego.ver_contador('Pepe'), 0)

    def test_segunda_partida_un_jugador_contador (self):
        jugadores = ['Pepe']
        juego = Juego(jugadores)
        for i in range(10):
            juego.jugar_ronda('Pepe', 1, 0)
        self.assertEqual(juego.ver_contador('Pepe'), 10)