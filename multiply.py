import pytest 

def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(3, 3) == 9
    assert multiply(4, 3) == 12
