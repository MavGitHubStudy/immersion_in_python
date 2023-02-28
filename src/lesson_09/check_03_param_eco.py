import random
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter  # возвращаем не результат работы исходной функции,
            # а видоизменённый результат!
        return wrapper
    return deco


@count(10)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10)}')
print(f'{rnd(1, 100)}')
print(f'{rnd(1, 1000)}')
"""
[1, 9, 9, 6, 2, 4, 7, 7, 2, 1]
[1, 9, 9, 6, 2, 4, 7, 7, 2, 1, 55, 3, 55, 81, 41, 55, 32, 83, 75, 15]
[1, 9, 9, 6, 2, 4, 7, 7, 2, 1, 55, 3, 55, 81, 41, 55, 32, 83, 75, 15,
 873, 128, 899, 71, 593, 656, 548, 686, 649, 353]

Process finished with exit code 0
"""
