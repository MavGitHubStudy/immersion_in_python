"""task_02.py"""
from math import sqrt
from task_02_ex import TriangleSideException
from task_02_ex import TriangleExistException
"""
Сравнение экземпляров класса

Python поддерживает определение шести основных операций
сравнения экземпляров
__eq__    - равно, ==
__ne__    - не равно, !=
__gt__    - больше, >
__ge__    - не больше, меньше или равно, <=
__lt__    - меньше, <
__le__    - не меньше, больше или равно, >=
"""


class Triangle:
    def __init__(self, a, b, c):

        self.flag = ''

        if not self._check_side(a):
            raise TriangleSideException(a)
        if not self._check_side(b):
            raise TriangleSideException(b)
        if not self._check_side(c):
            raise TriangleSideException(c)

        if not self._triangle_exist(a, b, c):
            raise TriangleExistException(self.flag)
        else:
            self.a = a
            self.b = b
            self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

    def __hash__(self):
        """Пытаемся вычислить хэш от нашего экземпляра"""
        return hash((self.a, self.b, self.c))

    @staticmethod
    def _check_side(side) -> bool:
        return side > 0

    def _triangle_exist(self, a, b, c):
        if a + b > c:
            if a + c > b:
                if b + c > a:
                    pass
                else:
                    self.flag = 'a'
            else:
                self.flag = 'b'
        else:
            self.flag = 'c'

        return False if self.flag != '' else True


def main():
    triangle_set = {Triangle(4, -9, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
                    Triangle(3, 5, 3)}
    print(triangle_set)
    print(', '.join(f'{item.area():.3f}' for item in triangle_set))
    print(', '.join(f'{item.__hash__()}' for item in triangle_set))


if __name__ == '__main__':
    main()
