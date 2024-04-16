import unittest
from bolos import Marcador

class TestBolos (unittest.TestCase):
    def test_hay_10_rondas(self):
        rondas_jugadas = [(0,0), (0,0),(0,0), (0,0),(0,0), (0,0),(0,0), (0,0), (0,0)]
        marcador = Marcador()
        self.assertTrue(marcador.numero_de_rondas_correcto(rondas_jugadas)) # cambiarlo para comprobar que se jugaron 10 rondas


if __name__ == '__main__':
    unittest.main()

    def score(self):
        total_score = 0
        roll_index = 0
        for frame in range(10):  # 10 frames in a game
            if self._is_strike(roll_index):
                total_score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total_score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self._sum_of_balls_in_frame(roll_index)
                roll_index += 2
        return total_score
    
    import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def test_strike(self):
        game = BowlingGame()
        game.roll(10)  # strike
        self.assertEqual(game.score(), 10)

    def test_spare(self):
        game = BowlingGame()
        game.roll(5)
        game.roll(5)  # spare
        game.roll(3)
        self.assertEqual(game.score(), 16)  # 5 + 5 + 3 + 3 (bonus for spare)

    def test_open_frame(self):
        game = BowlingGame()
        game.roll(3)
        game.roll(4)
        self.assertEqual(game.score(), 7)

    def test_multiple_strikes(self):
        game = BowlingGame()
        game.roll(10)
        game.roll(10)
        game.roll(10)
        self.assertEqual(game.score(), 30)  # 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10

    def test_multiple_spares(self):
        game = BowlingGame()
        game.roll(5)
        game.roll(5)  # spare
        game.roll(6)
        game.roll(4)  # spare
        game.roll(3)
        self.assertEqual(game.score(), 32)  # 5 + 5 + 6 + 6 + 3 + 3 + 3 + 3 (bonus for spares)

    def test_open_frames(self):
        game = BowlingGame()
        game.roll(3)
        game.roll(4)
        game.roll(7)
        game.roll(1)
        game.roll(2)
        game.roll(5)
        self.assertEqual(game.score(), 22)  # 3 + 4 + 7 + 1 + 2 + 5