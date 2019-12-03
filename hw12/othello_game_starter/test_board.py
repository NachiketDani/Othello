from game_controller import GameController
from board import Board


def test_constructor():
    g = GameController(800, 8)
    b = Board(800, 8, g)

    assert b.TILE_SIZE == 100
    assert b.BLACK == 0
    assert b.WHITE == 1
    assert b.no_legal_move_counter == 2
    assert b.game_controller == g
    assert b.player_score == 0
    assert b.ai_score == 0
    assert b.direction_list == [(0, -1), (1, -1), (-1, 0), (1, 0),
                                (-1, 1), (0, 1), (1, 1), (-1, -1)]
    assert b.legal_moveset == {}
    assert len(b.discs) == 8

    blackdisc_count = 0
    whitedisc_count = 0
    for rows in range(8):
        for columns in range(8):
            if b.discs[rows][columns] != 0:
                if b.discs[rows][columns].color == 0:
                    blackdisc_count += 1
                elif b.discs[rows][columns].color == 1:
                    whitedisc_count += 1
    assert blackdisc_count == 2
    assert whitedisc_count == 2

    assert b.discs[3][3].color == 1
    assert b.discs[4][4].color == 1
    assert b.discs[3][4].color == 0
    assert b.discs[4][3].color == 0

    def test_change_tiles():
        g = GameController(800, 8)
        b = Board(800, 8, g)
        