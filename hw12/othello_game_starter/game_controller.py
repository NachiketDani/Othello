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
        self.TURN_TEXT_TIMER = 60
        self.ASK_NAME_TIMER = 30
        self.ask_name_timer = self.ASK_NAME_TIMER
        self.turn_display_timer = self.TURN_TEXT_TIMER
        self.TEXT_OFFSET = 100

    def update(self):
        """
        Checks if game is completed else it alternates the turns
        and resets the turn display timer
        """
        if self.game_over is False:
            self.player_turn = not self.player_turn
            self.turn_display_timer = self.TURN_TEXT_TIMER

    def display_turn_text(self):
        """
        Prompt who's turn it is in the game
        """
        if self.turn_display_timer > 0:
            self.turn_display_timer -= 1
            if self.turn_display_timer > 0:
                fill(1, 0, 0)
                textSize(self.WINDOW_SIZE//20)
                textAlign(CENTER)
                if self.player_turn is True:
                    game_turn_text = "Player Turn"
                    text(game_turn_text, self.WINDOW_SIZE/2, self.TEXT_OFFSET)
                elif self.player_turn is False:
                    game_turn_text = "OthelloAI Turn"
                    text(game_turn_text, self.WINDOW_SIZE/2, self.TEXT_OFFSET)

    def display_result(self):
        """
        Displays appropriate result: if player or ai wins
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
            text("GAME OVER", self.WINDOW_SIZE/2,
                 self.WINDOW_SIZE/2 - self.TEXT_OFFSET)
            text(end_game_text, self.WINDOW_SIZE/2, self.WINDOW_SIZE/2)
            # Print Scores in different color
            fill(1, 0.8, 0.2)
            textSize(self.WINDOW_SIZE//14)
            (text("Player:" + str(self.game_scores[1]) + "\nOthello AI:" +
                  str(self.game_scores[0]), self.WINDOW_SIZE/2,
                  self.WINDOW_SIZE/2 + self.TEXT_OFFSET))
            if self.ask_name_timer == 0:
                self.get_player_name()
            else:
                self.ask_name_timer -= 1

    def input_name(self, message=""):
        """
        Java method for Text dialog box
        """
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def score_file(self):
        """
        Create or Open score file to store results
        if the user enters name
        """
        try:
            with open("scores.txt", "r") as f1:
                top_score_line = f1.readline()
                other_score_lines = f1.read()
                top_score = re.findall(r"\d+", top_score_line)
            with open("scores.txt", "w+") as f2:
                if int(self.game_scores[1]) > int(top_score[-1]):
                    # Rewrite file contents with new score in top row
                    f2.write(self.name + " " + str(self.game_scores[1]) +
                             "\n" + top_score_line +
                             other_score_lines)
                else:
                    # Rewrite file contents with new score in last row
                    f2.write(top_score_line +
                             other_score_lines +
                             self.name + " " + str(self.game_scores[1]) + "\n")
        except Exception:
            with open("scores.txt", "w+") as f3:
                f3.write(self.name + " " + str(self.game_scores[1]) + "\n")

    def get_player_name(self):
        """
        Pass username from dialog box to write into score file
        """
        if self.name_entered is False:
            self.name = self.input_name("Please enter your name:")
            self.name_entered = True
            self.score_file()
