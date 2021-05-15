import pytest

from Calculator import Calculator


@pytest.mark.regression
def test_for_positive_numbers():
    calc = Calculator()
    result = calc.multiplication(9, 10)
    assert result == 90


@pytest.mark.regression
def test_for_decimal():
    calc = Calculator()
    result = calc.multiplication(9, 1.1)
    assert result == 9.9


def test_for_zero():
    calc = Calculator()
    result = calc.multiplication(9, 0)
    assert result == 0


@pytest.mark.regression
def test_for_negative_numbers():
    calc = Calculator()
    result = calc.multiplication(-1, 1)
    assert result == -1
