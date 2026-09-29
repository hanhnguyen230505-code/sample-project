import pytest
from calculator import add, subtract, multiply, is_positive

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_is_positive_true():
    assert is_positive(5) is True

def test_is_positive_zero():
    with pytest.raises(ValueError):
        is_positive(0)