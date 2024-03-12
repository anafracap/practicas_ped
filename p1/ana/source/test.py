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

    def test_pleno_mas_ronda_abierta(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda('X')
        partida.jugar_ronda(1,2)
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 16)
    
    def test_pleno_tras_otro_pleno(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda('X') #10+10
        partida.jugar_ronda('X') #10
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 30)

    def test_pleno_pleno_ronda_abierta(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda('X') # 10+10+5
        partida.jugar_ronda('X') # 10+5
        partida.jugar_ronda(5,0) # 5
        for i in range(7):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 45)

    def test_tres_plenos_seguidos(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda('X') # 10A+10B+10C
        partida.jugar_ronda('X') # 10B+10C+1D
        partida.jugar_ronda('X') # 10+1+4
        partida.jugar_ronda(1,4) # 1+4
        for i in range(6):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 71)

    def test_semiplepleno_primera_ronda(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda(0, '/')
        for i in range(9):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 10)

    def test_semiplepleno_bolos_repartidos(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda(3, '/')
        for i in range(9):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 10)

    def test_semiplepleno_y_ronda_abierta(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda(3, '/')
        partida.jugar_ronda(1,0)
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 12)

    def test_semi_tras_otro_semi(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda(3, '/') #10+3
        partida.jugar_ronda(3, '/') #10
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 23)

    def test_semi_semi_ronda_abierta(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda(3, '/') #10 + 3
        partida.jugar_ronda(3, '/') #10 + 3
        partida.jugar_ronda(3, 0) # 3
        for i in range(7):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 29)

    def test_pleno_y_semi(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda('X') # 10 +10 
        partida.jugar_ronda(3, '/') #10
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 30)

    def test_pleno_semi_ronda_abierta(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda('X') # 10 +10 
        partida.jugar_ronda(3, '/') #10 +3
        partida.jugar_ronda(3, 0) # 3
        for i in range(7):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 36)

    def test_semi_pleno_semi(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.jugar_ronda(3, '/') # 10 +10
        partida.jugar_ronda('X') # 10 + 10 
        partida.jugar_ronda(3, '/') #10 +3
        partida.jugar_ronda(3, 0) # 3
        for i in range(6):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 56)

    def test_pleno_ronda_10_son_3_turnos(self):
        partida = Partida()
        partida.iniciar_partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        partida.jugar_ronda('X', 7, 2) # 10 + 9 + 9
        self.assertTrue(partida.ver_contador(), 28)



    #def test_no_puedes_tirar_mas_de_10_bolos_por_ronda(self):
    #def test_no_puedes_tirar_pleno_segundo_tiro(self):
    #def test_no_puedes_tirar_semi_primer_tiro(self):
    #def test_no_puedes_tirar_menos_de_0_bolos_por_ronda(self):
    #def test_no_puedes_tirar_pleno_y_semi_misma_ronda(self):