from game_controller import GameController
from board import Board
from player import Player


def test_constructor():
    """
    Test the Player class constructor
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    p = Player(b, g)
    assert p.board is b
    assert p.game_controller is g
    assert p.player_color == 0
    assert p.column_index == 0
    assert p.row_index == 0


def test_player_ready():
    # Unable to test as this method
    # Used to display player turn text on the board
    pass


def test_mouse_click():
    """
    Test if player can make legal or illegal moves
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    p = Player(b, g)

    # TEST1: for click on move which is legal
    mouse_x_test1 = 525
    mouse_y_test1 = 455
    # Ensure no disc on space before placing
    assert b.discs[4][5] == 0
    # Create legal moveset dictionary
    b.possible_moveset()
    p.mouse_click(mouse_x_test1, mouse_y_test1)
    assert p.column_index == 5
    assert p.row_index == 4
    # Check if space now has a player disc
    assert b.discs[4][5] != 0
    assert b.discs[4][5].color == 0

    # TEST2: for click on move which is not legal
    mouse_x_test2 = 50
    mouse_y_test2 = 50
    # Ensure no disc on space before click
    assert b.discs[0][0] == 0
    # Create legal moveset dictionary
    b.possible_moveset()
    p.mouse_click(mouse_x_test2, mouse_y_test2)
    assert p.column_index == 0
    assert p.row_index == 0
    # Check if disc space remains empty
    assert b.discs[0][0] == 0
