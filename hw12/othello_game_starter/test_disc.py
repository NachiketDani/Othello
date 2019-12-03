from disc import Disc


def test_constructor():
    d = Disc(0, 0, 100, 1)
    assert d.rows == 0
    assert d.columns == 0
    assert d.color == 1
