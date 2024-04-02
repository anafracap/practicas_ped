import unittest
from bolos import Marcador

class TestBolos (unittest.TestCase):
    def test_hay_10_rondas(self):
        rondas_jugadas = [(0,0), (0,0),(0,0), (0,0),(0,0), (0,0),(0,0), (0,0), (0,0)]
        marcador = Marcador()
        self.assertTrue(marcador.numero_de_rondas_correcto(rondas_jugadas)) # cambiarlo para comprobar que se jugaron 10 rondas


if __name__ == '__main__':
    unittest.main()