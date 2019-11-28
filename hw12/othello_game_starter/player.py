

class Player:
    def __init__(self, board, game_controller):
        self.player_color = 0
        self.board = board
        self.game_controller = game_controller

    def mouse_click(self, x, y):
        """
        Identifies mouse click location and changes+alternates disc color
        """
        print("Game initiated, mouse clicked")
        column_index = (x//self.board.TILE_SIZE)
        row_index = (y//self.board.TILE_SIZE)
        if self.game_controller.player_turn is True:
            self.board.possible_moveset()
            print(self.board.legal_moveset, "current legal moveset")
            # Check if legal
            if (row_index, column_index) in self.board.legal_moveset.keys():
                # Make move
                self.board.change_tiles(self.board.legal_moveset
                                        [(row_index, column_index)],
                                        self.player_color)
