import pytest

from Calculator import Calculator


def test_for_positive_numbers():
    calc = Calculator()
    result = calc.addition(9, 10)
    assert result == 19


def test_for_decimal():
    calc = Calculator()
    result = calc.addition(9, 1.1)
    assert result == 10.1


def test_for_zero():
    calc = Calculator()
    result = calc.addition(9, 0)
    assert result == 9


@pytest.mark.smoke
def test_for_mixed_numbers():
    calc = Calculator()
    result = calc.addition(-1, 1)
    assert result == 0


def test_for_negative_numbers():
    calc = Calculator()
    result = calc.addition(-1, -1)
    assert result == -2


