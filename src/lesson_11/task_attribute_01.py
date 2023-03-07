class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


def main():
    a = Vector(2, 4)
    print(a)


if __name__ == '__main__':
    main()
"""
Vector(2, 4)

Process finished with exit code 0
"""
# 01:38:20
