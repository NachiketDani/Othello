from board import Board
from disc import Disc
from game_controller import GameController
from player import Player
from othello_ai import OthelloAi

WINDOW_SIZE = 800
BOARD_SIZE = 4

game_controller = GameController(WINDOW_SIZE, BOARD_SIZE)
board = Board(WINDOW_SIZE, BOARD_SIZE, game_controller)
player = Player(board, game_controller)
othello_ai = OthelloAi(board, game_controller)


def setup():
    size(WINDOW_SIZE, WINDOW_SIZE)
    colorMode(RGB, 1)


def draw():
    background(0, 0.5, 0)
    board.display()
    player.player_ready()
    othello_ai.make_best_move()
    game_controller.display_result()


def mousePressed():
    if mousePressed:
        player.mouse_click(mouseX, mouseY)
