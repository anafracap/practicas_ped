import unittest, pytest
from bolos import Partida

class TestClass(unittest.TestCase):
    def test_hay_10_rondas(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(10):
            partida.jugar_ronda(0,0)
        self.assertTrue(partida.esta_terminada_la_partida())

    def test_partida_no_terminada(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda(0,0)
        partida.jugar_ronda(0,0)
        self.assertFalse(partida.esta_terminada_la_partida())

    def test_te_has_pasado_de_rondas(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(10):
            partida.jugar_ronda(0,0)
        with pytest.raises(Exception, match='NoJuegesMas'):
            partida.jugar_ronda(0,0)

    def test_contador_ronda_abierta(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(10):
            partida.jugar_ronda(0,1)
        self.assertEqual(partida.ver_contador(), 10)

    def test_contador_ronda_abierta_mejor(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(10):
            partida.jugar_ronda(2,0)
        self.assertEqual(partida.ver_contador(), 20)

    def test_pleno_primera_tirada(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda('X')
        for i in range(9):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 10)

