

class GameController:
    """
    Controls game flow and maintains state of the game
    """
    def __init__(self, WINDOW_SIZE, BOARD_SIZE):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.player_turn = True
        self.game_over = False
        self.game_winner = ""

    def update(self):
        """
        Checks if game is completed else it alternates the turns
        """
        if self.game_over is True:
            self.display_result()
            # self.player_turn = None
        else:
            self.player_turn = not self.player_turn

    def display_result(self):
        """
        Carries out necessary actions if player or ai wins
        """
        fill(0.89, 0.26, 0.20)
        textSize(self.WINDOW_SIZE//10)
        textAlign(CENTER)
        # Print result of the game
        if self.game_winner[0] < self.game_winner[1]:
            end_game_text = "Player Wins!"
        elif self.game_winner[0] > self.game_winner[1]:
            end_game_text = "AI Wins!"
        elif self.game_winner[0] == self.game_winner[1]:
            end_game_text = "Its a Tie!"
        text("GAME OVER", self.WINDOW_SIZE/2, self.WINDOW_SIZE/2 - 100)
        text(end_game_text, self.WINDOW_SIZE/2, self.WINDOW_SIZE/2)
        # Print Scores in different color
        fill(1, 0.8, 0.2)
        textSize(self.WINDOW_SIZE//14)
        (text("Player:" + str(self.game_winner[1]) + "\nOthello AI:" +
         str(self.game_winner[0]), self.WINDOW_SIZE/2, self.WINDOW_SIZE/2 + 100))
