

class Player:
    """
    Player class
    """
    def __init__(self, board, game_controller):
        self.player_color = 0
        self.board = board
        self.game_controller = game_controller

    def player_ready(self):
        """
        Ready game to accept player click co-ordinates
        """
        if self.game_controller.player_turn is True:
            self.board.possible_moveset()
            self.game_controller.display_turn_text()

    def mouse_click(self, x, y):
        """
        Identifies mouse click location and if legal
        passes the move chosen to the board
        """
        print("Game initiated, mouse clicked")
        column_index = (x//self.board.TILE_SIZE)
        row_index = (y//self.board.TILE_SIZE)
        # Check if legal
        if self.game_controller.player_turn is True:
            if (row_index, column_index) in self.board.legal_moveset.keys():
                # Make move
                self.board.change_tiles(self.board.legal_moveset
                                        [(row_index, column_index)],
                                        self.player_color)
