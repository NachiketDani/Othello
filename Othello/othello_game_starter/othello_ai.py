

class OthelloAi:
    """
    Othello AI class
    """
    def __init__(self, board, game_controller):
        self.game_controller = game_controller
        self.board = board
        self.player_color = 1
        self.TURN_TIMER_LENGTH = 35
        self.ai_turn_timer = self.TURN_TIMER_LENGTH
        self.best_move = set()

    def make_best_move(self):
        """
        Chose best move from set of legal moves
        Best move is the move that changes most number of discs
        """
        # Compare lengths of the move options and make best move
        # pass move coordinates to board
        if self.game_controller.player_turn is False:
            self.best_move = set()
            self.game_controller.display_turn_text()
            self.board.possible_moveset()
            if len(self.board.legal_moveset) > 0:
                for key in self.board.legal_moveset.keys():
                    if len(self.board.legal_moveset[key]) > len(self.best_move):
                        self.best_move = self.board.legal_moveset[key]
                # Make move
                if self.ai_turn_timer > 0:
                    self.ai_turn_timer -= 1
                if self.ai_turn_timer == 0:
                    self.board.change_tiles(self.best_move, self.player_color)
                    self.ai_turn_timer = self.TURN_TIMER_LENGTH
