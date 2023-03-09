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


def main():
    a = Vector(2, 4)
    # print(a.z)  # AttributeError: У нас вектор на плоскости, а не в пространстве
    print(f'{a = }')


if __name__ == '__main__':
    main()
"""
# File "/.../task_attribute_02.py", line 16, in __getattribute__
#     raise AttributeError(
# AttributeError: У нас вектор на плоскости, а не в пространстве
# 
# Process finished with exit code 1

a = Vector(2, 4)

Process finished with exit code 0
"""
# 01:38:20
