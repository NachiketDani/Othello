from game_controller import GameController
from board import Board
from disc import Disc


def test_constructor():
    """
    Test the board class constructor
    """
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


# def test_display():
    # Unable to test method that constructs the
    # board to display in Processing


def test_change_tiles():
    """
    Test method that changes tiles on the board
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    test_tiles = [(0, 0), (1, 1)]
    test_color = 1
    b.change_tiles(test_tiles, 1)
    for i in range(2):
        assert b.discs[i][i] != 0
    assert b.discs[0][0].color == 1
    assert b.discs[1][1].color == 1


def test_check_board_full():
    """
    Test method that checks if the board has empty spaces
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    for row in range(8):
        for column in range(8):
            # Fill with Player Discs
            b.discs[row][column] = Disc(row, column, 100, 1)
    b.check_board_full()
    assert g.game_over is True


def test_possible_moveset():
    """
    Test method that creates a dictionary of legal moves
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    b.possible_moveset()
    assert b.legal_moveset == {(2, 3): {(2, 3), (3, 3)},
                               (3, 2): {(3, 2), (3, 3)},
                               (5, 4): {(5, 4), (4, 4)},
                               (4, 5): {(4, 5), (4, 4)}}
    assert b.no_legal_move_counter == 2


def test_possible_moveset_exit_condition():
    """
    Test method that validates if direction of traversal
    for legal move algorithm is a valid set OR
    if the method exited due to incorrect condition
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    # Exit the legal move traverse as it has gone beyond board limit
    result1 = b.possible_moveset_exit_condition(10, 10, 1)
    assert result1 is False
    # Correct exit to legal move traversal
    opponent_color = 0
    result2 = b.possible_moveset_exit_condition(3, 4, 1)
    assert result2 is True
    # Exited the legal move traverse as it encountered only opponent color
    result3 = b.possible_moveset_exit_condition(0, 0, 0)
    assert result3 is False


def test_count_score():
    """
    Test method that counts the score on the board
    """
    g = GameController(800, 8)
    b = Board(800, 8, g)
    b.count_score()
    assert b.player_score == 2
    assert b.ai_score == 2
    assert g.game_scores == (2, 2)