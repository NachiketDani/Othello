# Class file for a pair of Dice
from die import Die


class PairofDice:
    """
    2 dice
    """
    def __init__(self):
        """Create 2 dice using Die class"""
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        """Create Roll attribute for 2 dice"""
        self.die1.roll()
        self.die2.roll()

    def current_sum(self):
        """Return sum of 2 dice"""
        return self.die1.current_value + self.die2.current_value
