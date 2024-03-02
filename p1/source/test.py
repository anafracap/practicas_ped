import unittest, pytest
from bolos import Partida

class TestClass(unittest.TestCase):
    def test_hay_10_rondas(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        partida.jugar_ronda()
        self.assertTrue(partida.esta_terminada_la_partida())

    def test_partida_no_terminada(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda()
        partida.jugar_ronda()
        self.assertFalse(partida.esta_terminada_la_partida())

