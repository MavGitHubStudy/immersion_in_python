import time
from typing import Callable
from functools import wraps
# 53:30

"""
1-й уровень для приёма параметров декоратора (функции deco)
2-й уровень для приёма функции, которую мы декорируем
3-й уровень - это сама работа декоратора, которая добавляет
    какой-то функционал до и после вызова декорируемой функции
"""


def count(num: int = 1):  # num - параметр, который передаём в декоратор
    def deco(func: Callable):
        @wraps(func)  # декоратор @ wraps позволяет сохранить строку
        # документации и имя декорируемой функции, а не имя обёртки,
        # которую используем для декорирования
        def wrapper(*args, **kwargs):  # функция wrapper принимает аргументы
            # чтобы передать их в функцию func
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result  # результат работы функции func c параметрами
            # *args и **kwargs

        return wrapper  # фанкция deco возвращает нам wrapper - обёртку
        # (без скобок, т.е. возвращает, а не вызывает)

    return deco  # функция count возвращает функцию deco


@count(3)
def factorial(n: int) -> int:
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')
help(factorial)
"""
Результаты замеров [0.00658312899986413, 0.0006145600000309059, 0.0005726540002797265]
factorial(1000) = 4023872600770937735437...0000
factorial.__name__ = 'factorial'
Help on function factorial in module __main__:

factorial(n: int) -> int
    Returns the factorial of the number n.
    
Process finished with exit code 0   
"""