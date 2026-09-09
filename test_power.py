from power import power


def test_square():
    assert power(2, 3) == 8


def test_zero_exponent():
    assert power(5, 0) == 1


def test_negative_exponent():
    assert power(2, -2) == 0.25


def test_float_base():
    assert power(2.5, 2) == 6.25
