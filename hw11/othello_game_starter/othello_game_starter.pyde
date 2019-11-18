from board import Board
from disc import Disc
from game_controller import GameController

WINDOW_SIZE = 800
BOARD_SIZE = 4

game_controller = GameController(WINDOW_SIZE)
board = Board(WINDOW_SIZE, BOARD_SIZE, game_controller)


def setup():
    size(WINDOW_SIZE, WINDOW_SIZE)
    colorMode(RGB, 1)


def draw():
    background(0, 0.5, 0)
    board.display()


def mousePressed():
    if mousePressed:
        board.mouse_click(mouseX, mouseY)
