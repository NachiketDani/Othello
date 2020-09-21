from game_controller import GameController
from othello_ai import OthelloAi
from board import Board
from disc import Disc


def test_constructor():
    """
    Test Othello AI Class Constructor
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    o_ai = OthelloAi(b, g)
    assert o_ai.game_controller is g
    assert o_ai.board is b
    assert o_ai.player_color == 1
    assert o_ai.TURN_TIMER_LENGTH == 35
    assert o_ai.ai_turn_timer == 35
    assert o_ai.best_move == set()


def test_make_best_move():
    """
    Test if Othello AI can make
    a best move from a set of legal moves
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    o_ai = OthelloAi(b, g)
    # Force AI turn
    g.player_turn = False
    # Turn off turn display
    g.turn_display_timer = -1
    # Add black disc to simulate if board is able to choose that legal move
    b.discs[5][3] = Disc(5, 3, 100, 0)
    o_ai.make_best_move()
    # Run method to create legal moveset for scenario
    b.possible_moveset()
    assert o_ai.best_move == {(4, 3), (5, 3), (6, 3)}
