"""
Задание №4

- Доработайте класс прямоугольник из прошлых семинаров.
- Добавьте возможность изменять длину и ширину прямоугольника и встройте
  контроль недопустимых значений (отрицательных).
- Используйте декораторы свойств.
"""


# 1:10:12 - 1:17:22 - 1:21:21


class Rectangle:

    def __init__(self, length, width=None):
        self._length = length
        self._width = width if width is None else length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    # def __add__(self, other):
    #     return self.perimeter() + other.perimeter()
    #
    # def __sub__(self, other):
    #     if self.perimeter() < other.perimeter():
    #         self.perimeter, other.perimeter = other.perimeter, self.perimeter
    #     return self.perimeter() - other.perimeter()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length_value):
        if length_value > 0:
            self._length = length_value
        else:
            raise ValueError(f'Длина должна быть больше нуля. '
                             f'Передано{length_value}')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_value):
        if width_value > 0:
            self._width = width_value
        else:
            raise ValueError(f'Ширина должна быть больше нуля. '
                             f'Передано{width_value}')


def main():
    r = Rectangle(2, 2)
    print(r.width, r.length)
    print(r.perimeter())
    r.length = 5
    r.width = 12
    print(r.width, r.length)
    print(r.perimeter())


if __name__ == '__main__':
    main()
# Первоначальная заготовка
"""
/home/.../.venv/bin/python /home/.../src/seminar_12/task_04.py 
2 2
8
12 5
34

Process finished with exit code 0
"""
# 12:32:55
