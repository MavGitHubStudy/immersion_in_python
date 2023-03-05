# 23:59
"""
Задание №2

Создайте класс прямоугольник.

Класс должен принимать длину и ширину при создании
экземпляра.

У класса должно быть два метода, возвращающие периметр
и площадь.

Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:  # 30:02

    def __init__(self, length, width=None):
        self.length = length
        # self.width = width if width else length
        self.width = width if width is not None else length  # 35:37
        # self.width = length if width is None else width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.area())
    print(r1.perimeter())
