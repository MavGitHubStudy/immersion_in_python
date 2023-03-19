"""1:18:13 task_05.py"""
"""
Задание №5

На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющий периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
(lesson_11/task_6.py)

Напишите 3-7 тестов unittest для данного класса.
"""


class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None else width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

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
    print(r1.area())
