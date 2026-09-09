import pytest
from hello import divide


def test_divide_basic():
    assert divide(6, 3) == 2


def test_divide_float():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)
