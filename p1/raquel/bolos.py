class Marcador:
    def numero_de_rondas_correcto(self, rondas_jugadas):
        return True
    class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

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

    def _is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def _sum_of_balls_in_frame(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]

    def _strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def _spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def _bonus_for_tenth_frame(self):
        if len(self.rolls) >= 19:  # check if there are at least 19 rolls
            if self.rolls[-3] == 10:  # last frame was a strike
                return self.rolls[-2] + self.rolls[-1]
            elif self.rolls[-3] + self.rolls[-2] == 10:  # last frame was a spare
                return self.rolls[-1]
        return 0