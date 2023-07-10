import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    # Test for basic cases of addition
    assert calculator.add(2, 3) == 5
    assert calculator.add(-2, 3) == 1
    assert calculator.add(0, 0) == 0

def test_subtract(calculator):
    # Test for basic cases of subtraction
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(3, 5) == -2
    assert calculator.subtract(0, 0) == 0

def test_multiply(calculator):
    # Test for basic cases of multiplication
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 10) == 0

def test_divide(calculator):
    # Test for basic cases of division
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(0, 5) == 0

def test_modulo(calculator):
    # Test for basic cases of modulo operation
    assert calculator.modulo(5, 3) == 2
    assert calculator.modulo(10, 4) == 2
    assert calculator.modulo(7, 7) == 0

def test_exp(calculator):
    # Test for basic cases of exponential operation
    assert calculator.exp(2, 3) == 8
    assert calculator.exp(2, 0) == 1
    assert calculator.exp(0, 5) == 0