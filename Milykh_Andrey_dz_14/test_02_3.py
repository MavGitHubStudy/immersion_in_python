"""1:21:37 test_05.py - файл для написания тестов"""
import pytest
from task_02 import Triangle
from task_02_ex import TriangleSideException, TriangleExistException


@pytest.fixture
def set_triangles():
    t3 = Triangle(6, 2, 5)
    return t3


def test_equal():
    # with pytest.raises(TriangleSideException) as ex:
    with pytest.raises(TriangleSideException) as ex:
        Triangle(4, -9, 5)
        # t1 = Triangle(4, 6, 5)

    assert str(ex.value) == (f'Недопустимое значение стороны треугольника: -9. '
                             f'Сторона треугольника должна быть больше нуля.')

    with pytest.raises(TriangleExistException) as ex:
        Triangle(4, 9, 5)
        # t2 = Triangle(4, 6, 5)

    assert str(ex.value) == 'Треугольника нет. b >= суммы других.'


def test_area(set_triangles):
    t3 = set_triangles
    assert t3.area() == 4.683748498798798


if __name__ == '__main__':
    # pytest.main(['-v'])
    pytest.main(['-v', 'test_02_3.py'])
