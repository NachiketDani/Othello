import random


class Die:
    """
    Class for Single die
    """
    def __init__(self):
        """Initializing attribute; dice not rolled"""
        self.current_value = 0

    def roll(self):
        self.current_value = random.randint(1, 6)
