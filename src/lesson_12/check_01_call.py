class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'MyClass(a={self.a}, b={self.b})'

    def __call__(self, *args, **kwargs):
        self.a.append(args)
        self.b.update(kwargs)
        return True


x = MyClass([42], {73: True})
y = x(3.14, 100, 500, start=1)
x(y=y)
print(x)
"""
MyClass(a=[42, (3.14, 100, 500), ()], b={73: True, 'start': 1, 'y': True})

Process finished with exit code 0
"""
# 13:15
