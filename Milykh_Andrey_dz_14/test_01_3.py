"""1:21:37 test_05.py - файл для написания тестов"""
import pytest
from task_01 import Rectangle


@pytest.fixture
def set_rectangles():
    r1 = Rectangle(2)
    r2 = Rectangle(3, 4)
    return r1, r2


def test_equal(set_rectangles):
    r1 = set_rectangles[0]
    assert r1.length == 2
    assert r1.width == 2


def test_perimeter(set_rectangles):
    r1 = set_rectangles[0]
    assert r1.perimeter() == 8


def test_area(set_rectangles):
    r2 = set_rectangles[1]
    assert r2.area() == 12


if __name__ == '__main__':
    # pytest.main(['-v'])
    pytest.main(['-v', 'test_01_3.py'])
