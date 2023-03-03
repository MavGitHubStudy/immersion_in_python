class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

    def say(self):
        print('Метод say() класса А')
        print(f'{self.data_b = }')


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()


class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()


class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()


class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


print(*Z.mro(), sep='\n')
z = Z()
z.say()

a = A()
a.say()   # AttributeError: 'A' object has no attribute 'data_b'. Did you
# mean: 'data_a' ?
"""
<class '__main__.Z'>
<class '__main__.X1'>
<class '__main__.X2'>
<class '__main__.B'>
<class '__main__.X3'>
<class '__main__.A'>
<class '__main__.C'>
<class '__main__.D'>
<class 'object'>
Init class Z
Init class X1
Init class X2
Init class B
Метод say() класса А
self.data_b = 'B'
Init class A
Метод say() класса А
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_inheritance_07.py", line 58, in <module>
    a.say()   # AttributeError: 'A' object has no attribute 'data_b'. Did you
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_inheritance_07.py", line 8, in say
    print(f'{self.data_b = }')
AttributeError: 'A' object has no attribute 'data_b'. Did you mean: 'data_a'?

Process finished with exit code 1
"""
# 01:23:05
