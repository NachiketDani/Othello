# Die Class file
import random


class Die:
    """
    Class for Single die
    """
    def __init__(self):
        """Initializing attribute; dice not rolled"""
        self.current_value = 0

    def roll(self):
        """Roll a die to get random value from 1 to 6"""
        self.current_value = random.randint(1, 6)
