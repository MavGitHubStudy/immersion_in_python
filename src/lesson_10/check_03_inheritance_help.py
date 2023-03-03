class A:
    name = 'A'
    def call(self):
        print(f'I am {self.name}')


class B:
    name = 'B'
    def call(self):
        print(f'I am {self.name}')


class C:
    name = 'C'
    def call(self):
        print(f'I am {self.name}')


class D(C, A):
    pass


class E(D, B):
    pass

print(*E.mro(), sep='\n')

e = E()
e.call()
"""
class '__main__.E'>
<class '__main__.D'>
<class '__main__.C'>
<class '__main__.A'>
<class '__main__.B'>
<class 'object'>
I am C

Process finished with exit code 0
"""
# 01:29:30
