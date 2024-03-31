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