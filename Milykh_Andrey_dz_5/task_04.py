"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fibonacci(num: int):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


print(*fibonacci(10))
