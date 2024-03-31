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