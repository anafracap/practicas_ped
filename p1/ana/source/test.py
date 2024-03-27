import unittest, pytest
from bolos import Partida

class TestClass(unittest.TestCase):
    def test_hay_10_rondas(self):
        partida = Partida()
        for i in range(10):
            partida.jugar_ronda(0,0)
        self.assertTrue(partida.esta_terminada_la_partida())

    def test_partida_no_terminada(self):
        partida = Partida()
        partida.jugar_ronda(0,0)
        partida.jugar_ronda(0,0)
        self.assertFalse(partida.esta_terminada_la_partida())

    def test_te_has_pasado_de_rondas(self):
        partida = Partida()
        for i in range(10):
            partida.jugar_ronda(0,0)
        with pytest.raises(Exception, match='NoJuegesMas'):
            partida.jugar_ronda(0,0)

    def test_contador_ronda_abierta(self):
        partida = Partida()
        for i in range(10):
            partida.jugar_ronda(0,1)
        self.assertEqual(partida.ver_contador(), 10)

    def test_contador_ronda_abierta_mejor(self):
        partida = Partida()
        for i in range(10):
            partida.jugar_ronda(2,0)
        self.assertEqual(partida.ver_contador(), 20)

    def test_pleno_primera_tirada(self):
        partida = Partida()
        partida.jugar_ronda('X')
        for i in range(9):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 10)

    def test_pleno_mas_ronda_abierta(self):
        partida = Partida()
        partida.jugar_ronda('X')
        partida.jugar_ronda(1,2)
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 16)
    
    def test_pleno_tras_otro_pleno(self):
        partida = Partida()
        partida.jugar_ronda('X') #10+10
        partida.jugar_ronda('X') #10
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 30)

    def test_pleno_pleno_ronda_abierta(self):
        partida = Partida()
        partida.jugar_ronda('X') # 10+10+5
        partida.jugar_ronda('X') # 10+5
        partida.jugar_ronda(5,0) # 5
        for i in range(7):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 45)

    def test_tres_plenos_seguidos(self):
        partida = Partida()
        partida.jugar_ronda('X') # 10A+10B+10C
        partida.jugar_ronda('X') # 10B+10C+1D
        partida.jugar_ronda('X') # 10+1+4
        partida.jugar_ronda(1,4) # 1+4
        for i in range(6):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 71)

    def test_semiplepleno_primera_ronda(self):
        partida = Partida()
        partida.jugar_ronda(0, '/')
        for i in range(9):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 10)

    def test_semiplepleno_bolos_repartidos(self):
        partida = Partida()
        partida.jugar_ronda(3, '/')
        for i in range(9):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 10)

    def test_semiplepleno_y_ronda_abierta(self):
        partida = Partida()
        partida.jugar_ronda(3, '/')
        partida.jugar_ronda(1,0)
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 12)

    def test_semi_tras_otro_semi(self):
        partida = Partida()
        partida.jugar_ronda(3, '/') #10+3
        partida.jugar_ronda(3, '/') #10
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 23)

    def test_semi_semi_ronda_abierta(self):
        partida = Partida()
        partida.jugar_ronda(3, '/') #10 + 3
        partida.jugar_ronda(3, '/') #10 + 3
        partida.jugar_ronda(3, 0) # 3
        for i in range(7):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 29)

    def test_pleno_y_semi(self):
        partida = Partida()
        partida.jugar_ronda('X') # 10 +10 
        partida.jugar_ronda(3, '/') #10
        for i in range(8):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 30)

    def test_pleno_semi_ronda_abierta(self):
        partida = Partida()
        partida.jugar_ronda('X') # 10 +10 
        partida.jugar_ronda(3, '/') #10 +3
        partida.jugar_ronda(3, 0) # 3
        for i in range(7):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 36)

    def test_semi_pleno_semi(self):
        partida = Partida()
        partida.jugar_ronda(3, '/') # 10 +10
        partida.jugar_ronda('X') # 10 + 10 
        partida.jugar_ronda(3, '/') #10 +3
        partida.jugar_ronda(3, 0) # 3
        for i in range(6):
            partida.jugar_ronda(0,0)
        self.assertEqual(partida.ver_contador(), 56)

    def test_pleno_ronda_10_son_3_turnos(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        partida.jugar_ronda('X', 7, 2) # 10 + 9 + 9
        self.assertEqual(partida.ver_contador(), 28)

    def test_pleno_ronda_10_son_3_turnos_otro_pleno(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        partida.jugar_ronda('X', 'X', 9) # 10 + 10 + 9, +9
        self.assertEqual(partida.ver_contador(), 38)

    def test_semi_ronda_10_son_3_turnos(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        partida.jugar_ronda(7, '/', 2) # 10 + 2  +2
        self.assertEqual(partida.ver_contador(), 14)
    
    def test_no_puedes_tirar_mas_de_10_bolos_por_ronda_normal(self):
        partida = Partida()
        with pytest.raises(Exception, match='DemasiadosBolos'):
            partida.jugar_ronda(9,2)

    # Se asume que no se renuevan los bolos en caso de rondas de bonus       
    def test_no_puedes_tirar_mas_de_10_bolos_turno2_3(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        with pytest.raises(Exception, match='DemasiadosBolos'):
            partida.jugar_ronda('X', 9, 2)

    def test_no_puedes_tirar_mas_de_10_bolos_turno3_ronda_1_a_9(self):
        partida = Partida()
        with pytest.raises(Exception, match='DemasiadasBolasLanzadas'):
            partida.jugar_ronda(1, 2, 3)

    def test_no_puedes_tirar_pleno_segundo_tiro_en_ronda_1_a_9(self):
        partida = Partida()
        with pytest.raises(Exception, match='PlenoExtraviado'):
            partida.jugar_ronda(1, 'X')

    def test_no_puedes_tirar_semi_primer_tiro(self):
        partida = Partida()
        with pytest.raises(Exception, match='SemiExtraviado'):
            partida.jugar_ronda('/', 1)

    def test_no_puedes_tirar_menos_de_0_bolos_por_ronda_tiro1(self):
        partida = Partida()
        with pytest.raises(Exception, match='NoTrampasNegativas'):
            partida.jugar_ronda(-1, 1)

    def test_no_puedes_tirar_menos_de_0_bolos_por_ronda_tiro2(self):
        partida = Partida()
        with pytest.raises(Exception, match='NoTrampasNegativas'):
            partida.jugar_ronda(1, -1)

    def test_no_puedes_tirar_menos_de_0_bolos_por_ronda_tiro3(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        with pytest.raises(Exception, match='NoTrampasNegativas'):
            partida.jugar_ronda('X', 1, -1)

    def test_no_puedes_tirar_semi_tras_pleno(self):
        partida = Partida()
        with pytest.raises(Exception, match='SemiExtraviado'):
            partida.jugar_ronda('X', '/')

    def test_partida_no_terminada_2(self):
        partida = Partida()
        partida.jugar_ronda(1,3)
        partida.jugar_ronda(2,1)
        self.assertEqual(partida.ver_contador(), 7)

    def test_partida_no_terminada_pleno_esperando_bonus(self):
        partida = Partida()
        partida.jugar_ronda(1,3)
        partida.jugar_ronda('X') # No se debería saber la puntuación
        self.assertEqual(partida.ver_contador(), "Todavía no se sabe")

    def test_partida_no_terminada_semi_esperando_bonus(self):
        partida = Partida()
        partida.jugar_ronda(1,3)
        partida.jugar_ronda(1,'/') # No se debería saber la puntuación
        self.assertEqual(partida.ver_contador(), "Todavía no se sabe")

    # Se asume que no se renuevan los bolos en caso de rondas de bonus       
    def test_partida_termina_en_semi(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        partida.jugar_ronda('X', 9, '/')
        self.assertEqual(partida.ver_contador(), 30)
   
    # Se asume que no se renuevan los bolos en caso de rondas de bonus       
    def test_partida_ideal(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda('X') # 9*30 = 270
        partida.jugar_ronda('X', 'X', 'X') # 10 +10 +10 , 10+10
        self.assertEqual(partida.ver_contador(), 300)

    def test_pleno_tras_bola_uno_diferente_a_pleno(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        with pytest.raises(Exception, match='PlenoExtraviado'):
            partida.jugar_ronda(9, 'X')

    # test_bolos_solo_int_o_X_o_/
    def test_bolos_no_letras_raras_turno1(self):
        partida = Partida()
        with pytest.raises(Exception, match='NomenclaturaIncorrecta'):
            partida.jugar_ronda('a',0)
    
    # test_bolos_solo_int_o_X_o_/
    def test_bolos_no_letras_raras_turno2(self):
        partida = Partida()
        with pytest.raises(Exception, match='NomenclaturaIncorrecta'):
            partida.jugar_ronda(0,'a')

    # test_bolos_solo_int_o_X_o_/
    def test_bolos_no_letras_raras_turno3(self):
        partida = Partida()
        for i in range(9):
            partida.jugar_ronda(0,0)
        with pytest.raises(Exception, match='NomenclaturaIncorrecta'):
            partida.jugar_ronda(9, '/', 'a')

    # test_bolos_solo_int_o_X_o_/
    def test_bolos_no_letras_raras_turno1_none(self):
        partida = Partida()
        with pytest.raises(Exception, match='NomenclaturaIncorrecta'):
            partida.jugar_ronda(None,0)
           
    def test_bolos_menos_10_una_sola_bola(selfs):
        partida = Partida()
        with pytest.raises(Exception, match='NoUnaBolaSuelta'):
            partida.jugar_ronda(9)

    def test_bolos_mas_10_una_sola_bola(selfs):
        partida = Partida()
        with pytest.raises(Exception, match='NomenclaturaIncorrecta'):
            partida.jugar_ronda(0, 10)

    #def test_pleno_con_otra_bola_detras (self)
    
    
    #TEST PARA OTRO ARCHIVO:    def test_partida_varios_jugadores
    