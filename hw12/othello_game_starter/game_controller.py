import re


class GameController:
    """
    Controls game flow and maintains state of the game
    """
    def __init__(self, WINDOW_SIZE, BOARD_SIZE):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.player_turn = True
        self.game_over = False
        self.game_scores = None
        self.name = None
        self.name_entered = False
        self.timer = 60

    def update(self):
        """
        Checks if game is completed else it alternates the turns
        """
        if self.game_over is False:
            self.player_turn = not self.player_turn

    def display_result(self):
        """
        Carries out necessary actions if player or ai wins
        """
        if self.game_over is True:
            fill(0.89, 0.26, 0.20)
            textSize(self.WINDOW_SIZE//10)
            textAlign(CENTER)
            # Print result of the game
            if self.game_scores[0] < self.game_scores[1]:
                end_game_text = "Player Wins!"
            elif self.game_scores[0] > self.game_scores[1]:
                end_game_text = "AI Wins!"
            elif self.game_scores[0] == self.game_scores[1]:
                end_game_text = "Its a Tie!"
            text("GAME OVER", self.WINDOW_SIZE/2, self.WINDOW_SIZE/2 - 100)
            text(end_game_text, self.WINDOW_SIZE/2, self.WINDOW_SIZE/2)
            # Print Scores in different color
            fill(1, 0.8, 0.2)
            textSize(self.WINDOW_SIZE//14)
            (text("Player:" + str(self.game_scores[1]) + "\nOthello AI:" +
                  str(self.game_scores[0]), self.WINDOW_SIZE/2,
                  self.WINDOW_SIZE/2 + 100))
            if self.timer == 0:
                self.get_player_name()
            else:
                self.timer -= 1

    def input_name(self, message=""):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def score_file(self):
        try:
            with open("scores.txt", "r") as f1:
                top_score_line = f1.readline()
                other_score_lines = f1.read()
                top_score = re.findall(r"\d+", top_score_line)
            with open("scores.txt", "w+") as f2:
                if int(self.game_scores[1]) > int(top_score[0]):
                    # Rewrite file contents with new score in top row
                    f2.write(self.name + " " + str(self.game_scores[1]) +
                             "\n" + top_score_line +
                             other_score_lines)
                else:
                    # Rewrite file contents with new score in last row
                    f2.write(top_score_line +
                             other_score_lines +
                             self.name + " " + str(self.game_scores[1]))
        except Exception:
            with open("scores.txt", "w+") as f3:
                f3.write(self.name + " " + str(self.game_scores[1]) + "\n")

    def get_player_name(self):
        if self.name_entered is False:
            self.name = self.input_name("Please enter your name:")
            self.name_entered = True
            self.score_file()
