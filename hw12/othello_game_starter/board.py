from disc import Disc
from game_controller import GameController


class Board:
    """Draws the Othello board & sets up """
    def __init__(self, WINDOW_SIZE, BOARD_SIZE, game_controller):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.TILE_SIZE = self.WINDOW_SIZE//self.BOARD_SIZE
        self.disc_color = 0
        self.game_controller = GameController(WINDOW_SIZE)
        self.discs = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]
        # Initialize the starter discs: 2 black, 2white
        self.discs[(self.BOARD_SIZE/2)-1][(self.BOARD_SIZE/2)-1] = (
            Disc(1, 1, self.TILE_SIZE, 1))
        self.discs[(self.BOARD_SIZE/2)][(self.BOARD_SIZE/2)-1] = (
            Disc(2, 1, self.TILE_SIZE, 0))
        self.discs[(self.BOARD_SIZE/2)][(self.BOARD_SIZE/2)] = (
            Disc(2, 2, self.TILE_SIZE, 1))
        self.discs[(self.BOARD_SIZE/2)-1][(self.BOARD_SIZE/2)] = (
            Disc(1, 2, self.TILE_SIZE, 0))

    def display(self):
        """
        Draws the board grid
        """
        stroke(0)
        strokeWeight(2)
        for row in range(1, self.BOARD_SIZE + 1):
            line(0, self.TILE_SIZE*row,
                 self.WINDOW_SIZE, self.TILE_SIZE*row)
        for column in range(1, self.BOARD_SIZE + 1):
            line(self.TILE_SIZE*column, 0,
                 self.TILE_SIZE*column, self.WINDOW_SIZE)
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.discs[row][column] != 0:
                    self.discs[row][column].display()
        self.game_controller.update()

    def change_tiles(self):
        # Accept coordinates for the move and make the corresponding move
        pass

    def check_board_full(self):
        """
        Check if board is full
        """
        empty_spots = 0
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.discs[row][column] == 0:
                    empty_spots += 1
        if empty_spots == 0:
            self.game_controller.game_over = True
