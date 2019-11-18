from disc import Disc
from game_controller import GameController


class Board:
    """Draws the Othello board"""
    def __init__(self, WINDOW_SIZE, BOARD_SIZE, game_controller):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.TILE_SIZE = self.WINDOW_SIZE//self.BOARD_SIZE
        self.color = 0
        self.game_controller = GameController(WINDOW_SIZE)
        self.discs = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]
        self.discs[1][1] = Disc(1, 1, self.TILE_SIZE, 1)
        self.discs[2][1] = Disc(2, 1, self.TILE_SIZE, 0)
        self.discs[2][2] = Disc(2, 2, self.TILE_SIZE, 1)
        self.discs[1][2] = Disc(1, 2, self.TILE_SIZE, 0)

    def display(self):
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

    def mouse_click(self, x, y):
        column_index = (x//self.TILE_SIZE)
        row_index = (y//self.TILE_SIZE)
        if self.game_controller.player_turn is True:
            if self.discs[row_index][column_index] == 0:
                self.discs[row_index][column_index] = (Disc(row_index, column_index, self.TILE_SIZE, self.color))
                self.game_controller.player_score += 1
                self.game_controller.player_turn = False
                self.color = 1
        elif self.game_controller.player_turn is False:
            if self.discs[row_index][column_index] == 0:
                self.discs[row_index][column_index] = (Disc(row_index, column_index, self.TILE_SIZE, self.color))
                self.game_controller.ai_score += 1
                self.game_controller.player_turn = True
                self.color = 0
        self.check_board_full()

    def check_board_full(self):
        empty_spots = 0
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.discs[row][column] == 0:
                    empty_spots += 1
        if empty_spots == 0:
            self.game_controller.game_over = True

