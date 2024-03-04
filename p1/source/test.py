import unittest, pytest
from bolos import Partida

class TestClass(unittest.TestCase):
    def test_hay_10_rondas(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(10):
            partida.jugar_ronda()
        self.assertTrue(partida.esta_terminada_la_partida())

    def test_partida_no_terminada(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda()
        partida.jugar_ronda()
        self.assertFalse(partida.esta_terminada_la_partida())

    def test_te_has_pasado_de_rondas(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(10):
            partida.jugar_ronda()
        with pytest.raises(Exception, match='NoJuegesMas'):
            partida.jugar_ronda()

    def test_contador_ronda_abierta(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(10):
            partida.jugar_ronda(0,1)
        self.assertEqual(partida.ver_contador(), 10)

