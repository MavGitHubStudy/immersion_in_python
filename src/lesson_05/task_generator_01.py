a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')
"""
=range(0, 10, 2), type(a)=<class 'range'>, a.__sizeof__()=48, 5
b=range(-1000000, 1000000, 2), type(b)=<class 'range'>, b.__sizeof__()=48, 1000000

Process finished with exit code 0
"""
