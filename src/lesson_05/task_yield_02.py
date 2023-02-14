# 1:02:00


def factorial(n):
    number = 1
    for i_ in range(1, n + 1):
        number *= i_
        yield number


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')
"""
! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800

Process finished with exit code 0
"""