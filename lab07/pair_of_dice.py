from die import Die


class PairofDice:
    """Pair of dice"""
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        return die1.current_value + die2.current_value
