from game_controller import GameController
from othello_ai import OthelloAi
from board import Board


def test_constructor():
    g = GameController(800, 8)
    b = Board(800, 8, g)
    o_ai = OthelloAi(b, g)

    assert o_ai.game_controller is g
    assert o_ai.board is b
    assert o_ai.player_color == 1
    assert o_ai.ai_turn_timer == 45


# def test_make_best_move():
