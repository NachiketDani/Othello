from board import Board
from disc import Disc
from player import Player
from othello_ai import OthelloAi


class GameController:
    """
    Controls game flow and maintains state of the game
    """
    def __init__(self, WINDOW_SIZE, BOARD_SIZE):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.player_score = 2
        self.ai_score = 2
        self.player_turn = True
        self.game_over = False
        self.direction_list = [(-1, -1), (0, -1), (1, -1),
                               (-1, 0), (1, 0),
                               (-1, 1), (0, 1), (1, 1)]
        self.legal_moveset = {}

    def update(self):
        """
        Checks if board is full and alternates the turns
        """
        if self.game_over is True:
            self.display_result()
        # else:
        # Continue the player turn
        #     player_turn = 

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
        (text("Player:" + str(self.player_score) + "\nOthello AI:" +
         str(self.ai_score), self.WINDOW_SIZE/2, self.WINDOW_SIZE/2 + 100))

    def possible_moveset(self):
        """
        Returns the legal moveset for the turn
        """
        # Code to check opponent colors for that turn
        opponent_color = -1
        if self.player_turn is True:
            opponent_color = 1
        else:
            opponent_color = 0
        move_tilelist = []
        # Code to find legal moveset and tiles to flip
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                # If the location is blank
                if self.discs[row][column] == 0:
                    # Loop through surrounding 8 directions
                    # to find an opposite color disc
                    move_tilelist.append(self.discs[row][column])
                    for directions in self.direction_list:
                        row += directions[0]
                        column += directions[1]
                        if self.discs[row][column] != 0 and self.discs[row][column].color == opponent_color:
                            while self.discs[row][column].color != opponent_color:
                                row += directions[0]
                                column += directions[1]
                                move_tilelist.append(self.discs[row][column])
                            
