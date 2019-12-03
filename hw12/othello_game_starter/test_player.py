from game_controller import GameController
from board import Board
from player import Player


def test_constructor():
    g = GameController(800, 8)
    b = Board(800, 8, g)
    p = Player(b, g)

    assert p.game_controller is g
    assert p.board is b
    assert p.player_color == 0


def test_player_ready():
    pass


def test_mouse_click():
    g = GameController(800, 8)
    b = Board(800, 8, g)
    p = Player(b, g)
    mouse_x_test = 525
    mouse_y_test = 325
    p.mouse_click(mouse_x_test, mouse_y_test)

    assert p.column_index == 5
    assert p.row_index == 3
    b.legal_moveset = {(0,0):{()}}