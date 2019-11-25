
class Disc:
    """A disc"""
    def __init__(self, rows, columns, tile_size, color):
        self.rows = rows
        self.columns = columns
        self.tile_size = tile_size
        self.color = color

    def display(self):
        DISC_TOLERANCE = 10
        fill(self.color)
        ellipse((self.columns * self.tile_size + self.tile_size//2),
                (self.rows * self.tile_size + self.tile_size//2),
                (self.tile_size-DISC_TOLERANCE),
                (self.tile_size-DISC_TOLERANCE))
