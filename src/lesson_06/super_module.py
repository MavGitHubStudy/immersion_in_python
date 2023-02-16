from random import randint

# __all__
__all__ = ['func', '_secret']

# глобальная константа
SIZE = 100
# глобальные переменные
_secret = 'qwerty'  # защищённая переменная
__top_secret = '1q2w3e4r5t6y'  # приватная переменная


# глобальные функции
def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z


# глобальная переменная result
result = func(1, 6)
