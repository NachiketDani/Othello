

class GameController:
    """
    Maintains state of the game
    """
    def __init__(self, WINDOW_SIZE):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.player_score = 2
        self.ai_score = 2
        self.player_turn = True
        self.game_over = False

    def update(self):
        """
        Checks if board is full and alternates the turns
        """
        if self.game_over is True:
            self.display_result()
        # else:
        #     player_turn

    def display_result(self):
        """
        Carries out necessary actions if player or ai wins
        """
        fill(0.89, 0.26, 0.20)
        textSize(self.WINDOW_SIZE//10)
        textAlign(CENTER)
        # Print result of the game
        if self.player_score > self.ai_score:
            end_game_text = "Player Wins!"
        elif self.player_score < self.ai_score:
            end_game_text = "AI Wins!"
        else:
            end_game_text = "Its a Tie!"
        text("GAME OVER", self.WINDOW_SIZE/2, self.WINDOW_SIZE/2 - 100)
        text(end_game_text, self.WINDOW_SIZE/2, self.WINDOW_SIZE/2)
        # Print Scores in different color
        fill(1, 0.8, 0.2)
        textSize(self.WINDOW_SIZE//14)
        text("Player:" + str(self.player_score) + "\nOthello AI:" + str(self.ai_score), self.WINDOW_SIZE/2, self.WINDOW_SIZE/2 + 100)

    # def turn_control(self):
