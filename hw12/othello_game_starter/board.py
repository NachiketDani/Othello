from disc import Disc
from game_controller import GameController


class Board:
    """Draws the Othello board & sets up """
    def __init__(self, WINDOW_SIZE, BOARD_SIZE, game_controller):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.TILE_SIZE = self.WINDOW_SIZE//self.BOARD_SIZE
        self.BLACK = 0
        self.WHITE = 1
        self.PAUSE_LENGTH = 60
        self.no_legal_move_counter = 2
        self.game_controller = game_controller
        self.player_score = 0
        self.ai_score = 0
        self.counter = self.PAUSE_LENGTH
        self.direction_list = [(0, -1), (1, -1),
                               (-1, 0), (1, 0),
                               (-1, 1), (0, 1), (1, 1), (-1, -1)]
        self.legal_moveset = {}
        self.discs = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]
        # Initialize the starter discs: 2 black, 2white
        self.discs[(self.BOARD_SIZE/2)-1][(self.BOARD_SIZE/2)-1] = (
            Disc(1, 1, self.TILE_SIZE, self.WHITE))
        self.discs[(self.BOARD_SIZE/2)][(self.BOARD_SIZE/2)-1] = (
            Disc(2, 1, self.TILE_SIZE, self.BLACK))
        self.discs[(self.BOARD_SIZE/2)][(self.BOARD_SIZE/2)] = (
            Disc(2, 2, self.TILE_SIZE, self.WHITE))
        self.discs[(self.BOARD_SIZE/2)-1][(self.BOARD_SIZE/2)] = (
            Disc(1, 2, self.TILE_SIZE, self.BLACK))

    def display(self):
        """
        Draws the board grid
        """
        stroke(0)
        strokeWeight(2)
        # Draw horizontal lines
        for row in range(1, self.BOARD_SIZE + 1):
            line(0, self.TILE_SIZE*row,
                 self.WINDOW_SIZE, self.TILE_SIZE*row)
        # Draw vertical lines
        for column in range(1, self.BOARD_SIZE + 1):
            line(self.TILE_SIZE*column, 0,
                 self.TILE_SIZE*column, self.WINDOW_SIZE)
        # Loop through the board, if there is a disc, display it
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.discs[row][column] != 0:
                    self.discs[row][column].display()

    def change_tiles(self, set_of_discs, disc_color):
        """
        Accept coordinates for the move and make the corresponding move
        """
        for elements in set_of_discs:
            self.discs[elements[0]][elements[1]] = Disc(elements[0],
                                                        elements[1],
                                                        self.TILE_SIZE,
                                                        disc_color)
        if self.game_controller.player_turn is True:
            self.counter = 60
        self.check_board_full()

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
            if self.game_controller.game_over is False:
                self.count_score()
                self.game_controller.game_over = True
        self.game_controller.update()

    def possible_moveset(self):
        """
        Returns the legal moveset for the turn
        """
        # Code to check opponent colors for that turn
        opponent_color = -1
        if self.game_controller.player_turn is True:
            opponent_color = 1
        else:
            opponent_color = 0
        # Code to find legal moveset and tiles to flip
        self.legal_moveset = {}
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                # If the location is blank
                if self.discs[i][j] == 0:
                    # Loop through surrounding 8 directions
                    # to find an opposite color disc
                    for directions in self.direction_list:
                        row, column = i, j
                        move_tilelist = [(row, column)]
                        row += directions[0]
                        column += directions[1]
                        # For the direction check make sure its not empty
                        # and has the opponent color discs
                        while (((row >= 0 and row < self.BOARD_SIZE) and
                               (column >= 0 and column < self.BOARD_SIZE)) and
                               (self.discs[row][column] != 0) and
                               (self.discs[row][column].color ==
                               opponent_color)):
                            move_tilelist.append((row, column))
                            row += directions[0]
                            column += directions[1]
                            # print(row, column, move_tilelist)
                        valid = (self.possible_moveset_exit_condition
                                 (row, column, opponent_color))
                        # print(valid)
                        if valid and len(move_tilelist) > 1:
                            if move_tilelist[0] in self.legal_moveset.keys():
                                for disc_tuple in move_tilelist:
                                    (self.legal_moveset[move_tilelist[0]].
                                     add(disc_tuple))
                            else:
                                self.legal_moveset[move_tilelist[0]] = set()
                                for disc_tuple in move_tilelist:
                                    (self.legal_moveset[move_tilelist[0]].
                                     add
                                     (disc_tuple))
        if len(self.legal_moveset) == 0:
            if self.no_legal_move_counter > 0:
                self.no_legal_move_counter -= 1
                self.game_controller.update()
            elif self.no_legal_move_counter == 0:
                self.count_score()
                self.game_controller.game_over = True
                self.game_controller.update()
        else:
            self.no_legal_move_counter = 2

    def possible_moveset_exit_condition(self, row, column, opponent_color):
        # Add to Dictionary of legal moves if exit condition is correct
        if ((row < self.BOARD_SIZE) and
            (column < self.BOARD_SIZE) and
            (row >= 0) and
           (column >= 0)):
            if self.discs[row][column] != 0:
                if self.discs[row][column].color != opponent_color:
                    return True
        return False

    def count_score(self):
        self.ai_score = 0
        self.player_score = 0
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.discs[row][column] != 0:
                    if self.discs[row][column].color == 1:
                        self.ai_score += 1
                    elif self.discs[row][column].color == 0:
                        self.player_score += 1
        self.game_controller.game_scores = (self.ai_score, self.player_score)
