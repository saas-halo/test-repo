from subtract import subtract


def test_basic():
    assert subtract(5, 3) == 2


def test_negative_result():
    assert subtract(3, 5) == -2


def test_float():
    assert subtract(5.5, 2.0) == 3.5


def test_zero():
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
