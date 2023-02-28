import time
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result  # Эта строчка обязательна, чтобы не сломать функционал!

    return wrapper


@main
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# control = main(factorial)  # Функция control есть задекорированный факториал,
# # но в Python обычно так не декорируют
# print(f'{control.__name__ = }')
# print(f'{control(1000) = }')

print(f'{factorial(1000) = }')
"""
Запуск функции factorial в 1677574867.8588307
Результат функции factorial: 4023...0000
Завершение функции factorial в 1677574867.8685727
factorial(1000) = 4023...0000
"""
