# 14: 10
"""
Задание №1

Создайте класс окружность.

Класс должен принимать радиус окружности при создании
экземпляра.

У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
from cmath import pi


class Circumference:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    c1 = Circumference(10)
    print(c1.area())
    print(c1.perimeter())  # 23:31
"""
314.1592653589793
62.83185307179586

Process finished with exit code 0
"""
