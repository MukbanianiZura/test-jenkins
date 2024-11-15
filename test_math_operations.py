import pytest
from math_operations import addition, subtraction, multiplication, division


def test_addition():
    assert addition(3, 2) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(-5, -3) == -8


def test_subtraction():
    assert subtraction(3, 2) == 1
    assert subtraction(5, 8) == -3
    assert subtraction(0, 0) == 0
    assert subtraction(-5, -3) == -2


def test_multiplication():
    assert multiplication(3, 2) == 6
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 5) == 0
    assert multiplication(-4, -5) == 20


def test_division():
    assert division(6, 2) == 3
    assert division(9, 3) == 3
    assert division(-6, 2) == -3
    assert division(5, 2) == 2.5

    with pytest.raises(ZeroDivisionError):
        division(1, 0)
