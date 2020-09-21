from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    test_x1, test_y1 = 580, 150
    test_x2, test_y2 = 150, 450
    TEST_WIDTH = 600
    TEST_HEIGHT = 600
    TEST_LEFT_VERT = 150
    TEST_RIGHT_VERT = 450
    TEST_TOP_HORIZ = 150
    TEST_BOTTOM_HORIZ = 450
    test_g = GameController(600, 600)

    test_maze = Maze(TEST_WIDTH, TEST_HEIGHT, TEST_LEFT_VERT,
                     TEST_RIGHT_VERT, TEST_TOP_HORIZ,
                     TEST_BOTTOM_HORIZ, test_g)
    len_rcol = len(test_maze.dots.right_col)
    len_lcol = len(test_maze.dots.left_col)
    len_trow = len(test_maze.dots.top_row)
    len_brow = len(test_maze.dots.bottom_row)

    # Eat top row rightmost half dot and leftmost half dot
    test_maze.eat_dots(test_x1, test_y1)
    assert len(test_maze.dots.top_row) == (len_trow - 2)
    # Eat bottom left intersection dot
    test_maze.eat_dots(test_x2, test_y2)
    assert len(test_maze.dots.left_col) == (len_lcol - 1)
    assert len(test_maze.dots.bottom_row) == (len_brow - 1)
