from game_controller import GameController


class Player:
    def __init__(self):
        self.player_color = 0

    def mouse_click(self, x, y):
        """
        Identifies mouse click location and changes+alternates disc color
        """
        column_index = (x//self.TILE_SIZE)
        row_index = (y//self.TILE_SIZE)
        if self.game_controller.player_turn is True:
            # Check if legal
            # if self.discs[row_index][column_index] == LEGAL
                self.discs[row_index][column_index] = (
                 Disc(row_index, column_index, self.TILE_SIZE, self.disc_color))
                
                # self.game_controller.player_score += 1
                self.game_controller.player_turn = False
                self.color = 1
        self.check_board_full()
