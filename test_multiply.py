from multiply import multiply


def test_ints():
    assert multiply(3, 4) == 12


def test_float():
    assert multiply(2.5, 4) == 10.0


def test_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0


def test_negative():
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12
