import pytest

from HW1.simple_math import SimpleMath


@pytest.fixture
def simplemath():
    return SimpleMath()

def test_square(simplemath):
    assert simplemath.square(-2) == 4

def test_cube(simplemath):
    assert simplemath.cube(0) == 0