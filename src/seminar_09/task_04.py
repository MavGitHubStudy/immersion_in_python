"""
Задание №4

Создайте декоратор с параметром.

Параметр - целое число, количество запусков декорируемой функции.
"""
from random import randint
from typing import Callable


def count(n: int = 1):

    def deco(func: Callable):
        counts = []

        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
                counts.append(result)


            return counts

        return wrapper

    return deco


@count(10)
def some_func():
    num = randint(1, 100)
    return num


print(some_func())
"""
[13, 8, 87, 55, 89, 59, 78, 10, 67, 67]

Process finished with exit code 0
"""
