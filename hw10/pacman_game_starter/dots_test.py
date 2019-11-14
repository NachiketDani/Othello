from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    test_x1, test_y1 = 450, 450
    test_x2, test_y2 = 150, 2
    TEST_WIDTH = 600
    TEST_HEIGHT = 600
    TEST_LEFT_VERT = 150
    TEST_RIGHT_VERT = 450
    TEST_TOP_HORIZ = 150
    TEST_BOTTOM_HORIZ = 450
    test_dots = Dots(TEST_WIDTH, TEST_HEIGHT,
                     TEST_LEFT_VERT, TEST_RIGHT_VERT,
                     TEST_TOP_HORIZ, TEST_BOTTOM_HORIZ)
    len_rcol = len(test_dots.right_col)
    len_lcol = len(test_dots.left_col)
    len_trow = len(test_dots.top_row)
    len_brow = len(test_dots.bottom_row)
    # Eat bottom right intersection dot
    test_dots.eat(test_x1, test_y1)
    assert len(test_dots.right_col) == (len_rcol - 1)
    assert len(test_dots.bottom_row) == (len_brow - 1)
    # Eat left column topmost half dot and bottom half dot
    test_dots.eat(test_x2, test_y2)
    assert len(test_dots.left_col) == (len_lcol - 2)


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)
