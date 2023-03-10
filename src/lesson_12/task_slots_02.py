from math import sqrt


class Triangle:
    __slots__ = ('_a', '_b', '_c')

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
# print(triangle.__dict__)  # AttributeError: 'Triangle' object has no
# # attribute '__dict__'. Did you mean: '__dir__'?
print(Triangle.__dict__)
"""
Треугольник со сторонами: 3, 4, 5
Traceback (most recent call last):
  File "/home/.../lesson_12/task_slots_02.py", line 35, in <module>
    print(triangle.__dict__)  # AttributeError: 'Triangle' object has no
AttributeError: 'Triangle' object has no attribute '__dict__'. 
Did you mean: '__dir__'?

Process finished with exit code 1
"""
# 1:16:11
"""
Треугольник со сторонами: 3, 4, 5
{'__module__': '__main__', '__slots__': ('_a', '_b', '_c'), 
'__init__': <function Triangle.__init__ at 0x7f5ac6874af0>, 
'__str__': <function Triangle.__str__ at 0x7f5ac68743a0>, 
'__repr__': <function Triangle.__repr__ at 0x7f5ac6874b80>, 
'__eq__': <function Triangle.__eq__ at 0x7f5ac6874c10>, 
'area': <function Triangle.area at 0x7f5ac6874ca0>, 
'__lt__': <function Triangle.__lt__ at 0x7f5ac6874d30>,
'__hash__': <function Triangle.__hash__ at 0x7f5ac6874dc0>, 
'_a': <member '_a' of 'Triangle' objects>, 
'_b': <member '_b' of 'Triangle' objects>,
 '_c': <member '_c' of 'Triangle' objects>, '__doc__': None}

Process finished with exit code 0
"""
# 1:19:10
