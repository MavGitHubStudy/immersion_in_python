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

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError(
                'У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError(
                'У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return None

    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)


def main():
    a = Vector(2, 4)
    a.s = 73
    print(f'{a = }, {a.s = }')
    del a.x
    del a.s
    print(f'{a = }, {a.s = }')


if __name__ == '__main__':
    main()
"""
a = Vector(2, 4), a.s = 73
a = Vector(0, 4), a.s = None

Process finished with exit code 0
"""
# 01:48:01
