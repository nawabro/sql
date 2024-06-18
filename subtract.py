import pytest
def subtract(a,b):
    return a-b

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(3, 3) == 0
    assert subtract(4, 3) == 1