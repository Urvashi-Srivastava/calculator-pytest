import pytest
from Calculator import Calculator


@pytest.fixture()
def calculator_obj():
    calc = Calculator()
    return calc


@pytest.fixture(params=[(-3, -2, -5), (-9, -1, -10)])
def send_negative_numbers(request):
    return request.param


def test_for_positive_numbers(calculator_obj):
    result = calculator_obj.addition(9, 10)
    assert result == 19


def test_for_negative_numbers(calculator_obj):
    result = calculator_obj.multiplication(-1, 1)
    assert result == -1


def test_addition_for_negative_number(calculator_obj, send_negative_numbers):
    result = calculator_obj.addition(send_negative_numbers[0], send_negative_numbers[1])
    assert result == send_negative_numbers[2]

