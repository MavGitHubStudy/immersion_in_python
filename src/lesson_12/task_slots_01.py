from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'

    def __repr__(self):
        return f'Trianlge({self._a}, {self._b}, {self._c}'

    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))

    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

    def __hash__(self):
        return hash((self._a, self._b, self._c))


triangle = Triangle(3, 4, 5)
print(triangle)
print(triangle.__dict__)
print(Triangle.__dict__)
"""
Треугольник со сторонами: 3, 4, 5
{'_a': 3, '_b': 4, '_c': 5}
{'__module__': '__main__', 
'__init__': <function Triangle.__init__ at 0x7f8204d4caf0>,
 '__str__': <function Triangle.__str__ at 0x7f8204d4c3a0>, 
 '__repr__': <function Triangle.__repr__ at 0x7f8204d4cb80>, 
 '__eq__': <function Triangle.__eq__ at 0x7f8204d4cc10>, 
 'area': <function Triangle.area at 0x7f8204d4cca0>, 
 '__lt__': <function Triangle.__lt__ at 0x7f8204d4cd30>, 
 '__hash__': <function Triangle.__hash__ at 0x7f8204d4cdc0>, 
 '__dict__': <attribute '__dict__' of 'Triangle' objects>, 
 '__weakref__': <attribute '__weakref__' of 'Triangle' objects>, 
 '__doc__': None}

Process finished with exit code 0
"""
# 1:16:11
