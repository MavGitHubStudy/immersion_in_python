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
from math import sqrt


class Triangle:
    __hash__ = None  # Перед нами изменяемы объект! Мы не можем его хешировать!

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f' Triangle({self.a}, {self.b}, {self.c}'

    # def __eq__(self, other):
    #     first = sorted((self.a, self.b, self.c))
    #     second = sorted((other.a, other.b, other.c))
    #     return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()


def main():
    triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
                    Triangle(3, 5, 3)}
    print(triangle_set)
    print(', '.join(f'{item.area():.3f}' for item in triangle_set))
    # Если TypeError: unhashable type: 'Triangle', закомментировать __eq__


if __name__ == '__main__':
    main()
"""
{raceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_11/task_eq_06.py", line 53, in <module>
    main()
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_11/task_eq_06.py", line 45, in main
    triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
TypeError: unhashable type: 'Triangle'

Process finished with exit code 1
"""
# 01:30:40
# 01:28:28 - обязательно для изучения !!!
