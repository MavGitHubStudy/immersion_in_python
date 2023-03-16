""" task_01.py """
from task_01_ex import RectangleLengthException, RectangleWidthException

"""
- Напишите классы исключения с выводом подробной 
  информации.
  
- Поднимайте исключения внутри основного кода. Например, 
  нельзя создавать прямоугольник со сторонами отрицательной
  длины.
"""


class Rectangle:

    def __init__(self, length, width=None):
        if self._check_size(length):
            self._length = length
        else:
            raise RectangleLengthException(length)

        if width is None:
            self._width = self.length
        else:
            if self._check_size(width):
                self._width = width
            else:
                raise RectangleWidthException(width)

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    @staticmethod
    def _check_size(rect_size) -> bool:
        return rect_size > 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length_value):
        if not self._check_size(length_value):
            raise RectangleLengthException(length_value)
        self._length = length_value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_value):
        if not self._check_size(width_value):
            raise RectangleWidthException(width_value)
        self._width = width_value


def main():
    try:
        r1 = Rectangle(2, 2)
        # r1 = Rectangle(2)
        print(r1.width, r1.length)
        print(r1.perimeter())
        r1.length = 5
        r1.width = 6
        print(r1.width, r1.length)
        print(r1.perimeter())
    except (RectangleLengthException, RectangleWidthException) as e:
        print(e)


if __name__ == '__main__':
    main()
