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
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f' Triangle({self.a}, {self.b}, {self.c}'

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


def main():
    one = Triangle(3, 4, 5)
    two = Triangle(5, 5, 5)
    print(f'{one} имеет площадь {one.area():.3f} у.е. ²')
    print(f'{two} имеет площадь {two.area():.3f} у.е. ²')
    print(f'{one > two = }\n{one < two = }')

    data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
            Triangle(3, 5, 3)]
    result = sorted(data)
    print(result)
    print(', '.join(f'{item.area():.3f}' for item in result))


if __name__ == '__main__':
    main()
"""
Треугольник со сторонами 3, 4, 5 имеет площадь 6.000 у.е. ²
Треугольник со сторонами 5, 5, 5 имеет площадь 10.825 у.е. ²
one > two = False
one < two = True
[ Triangle(3, 5, 3,  Triangle(6, 2, 5,  Triangle(3, 4, 5,  Triangle(4, 4, 4]
4.146, 4.684, 6.000, 6.928

Process finished with exit code 0
"""
# 01:20:10
