"""
Задание №6

Доработайте прошлую задачу.

Добавьте сравнение прямоугольников по площади.

Должны работать все шесть операций сравнения.
"""
from functools import total_ordering


@total_ordering
class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        # self.width = width if width else length
        self.width = width if width is not None else length  # 35:37
        # self.width = length if width is None else width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_length, new_width)

    # def __sub__(self, other):
    #     new_perimeter = self.perimeter() - other.perimeter()
    #     if new_perimeter < 0:
    #         new_perimeter = 0
    #     new_width = self.width + other.width
    #     new_length = new_perimeter / 2 - new_width
    #     return Rectangle(new_length, new_width)
    def __sub__(self, other):
        # if self.perimeter() < other.perimeter():
        #     self.perimeter, other.perimeter = other.perimeter, self.perimeter
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        return self.area() == other.area()

    # def __ne__(self, other):
    #     return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    # def __lt__(self, other):
    #     return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    # def __le__(self, other):
    #     return self.area() <= other.area()


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.perimeter())
    r2 = Rectangle(4, 5)
    print(r2.perimeter())
    # r3 = r1 + r2
    # r3 = r1 - r2
    r3 = r2 - r1
    print(f'{r1 = }')
    print(f'{r3 = }')
    print(r3.perimeter())
    print(f'{r3.length = }, {r3.width = }')
    # print(r1 - r2)

    print(r1 == r2)

    print()
    print(r1 == Rectangle(1, 4))
    print(r1 != Rectangle(1, 4))
    print(r1 > Rectangle(1, 4))
    print(r1 < Rectangle(1, 4))
    print(r1 >= Rectangle(1, 4))
    print(r1 <= Rectangle(1, 4))
"""
8
18
r1 = <__main__.Rectangle object at 0x7f4fb7de3fd0>
r3 = <__main__.Rectangle object at 0x7f4fb7de3d60>
10.0
r3.length = 2.0, r3.width = 3
False

True
False
False
False
True
True

Process finished with exit code 0
"""
# 2:01:44
