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
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second


def main():
    one = Triangle(3, 4, 5)
    two = one
    three = Triangle(3, 4, 5)
    four = Triangle(4, 3, 5)
    print(f'{one == two   = }')
    print(f'{one == three = }')
    print(f'{one == four  = }')
    print(f'{one != one   = }')


if __name__ == '__main__':
    main()
"""
one == two   = True
one == three = True
one == four  = True
one != one   = False

Process finished with exit code 0
"""
# 01:20:10
