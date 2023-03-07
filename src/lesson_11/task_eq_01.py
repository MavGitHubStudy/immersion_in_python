class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'


def main():
    one = Triangle(3, 4, 5)
    two = one
    three = Triangle(3, 4, 5)
    print(one == two)
    print(one == three)


if __name__ == '__main__':
    main()
"""
True
False

Process finished with exit code 0
"""
# 01:14:48
