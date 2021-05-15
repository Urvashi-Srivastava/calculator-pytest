import pytest

from Calculator import Calculator


def test_for_positive_numbers():
    calc = Calculator()
    result = calc.substraction(9, 10)
    assert result == -1


def test_for_decimal():
    calc = Calculator()
    result = calc.substraction(9, 1.1)
    assert result == 7.9


def test_for_zero():
    calc = Calculator()
    result = calc.substraction(9, 0)
    assert result == 9


def test_for_mixed_numbers():
    calc = Calculator()
    result = calc.substraction(-1, 1)
    assert result == -2


def test_for_negative_numbers():
    calc = Calculator()
    result = calc.substraction(-1, -1)
    assert result == 0
