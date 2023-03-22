"""26:15 - 35:00 - 40:25 - 41:25 task_02_3
.py"""
import logging
from typing import Callable

"""
Задание №2

На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.

Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""

logging.basicConfig(level=logging.INFO,
                    filename='logs.log',
                    encoding='utf-8')
logger = logging.getLogger(__name__)


def deco_func(func: Callable):
    # нужно модифицировать wrapper !
    def wrapper(*args, **kwargs):
        dct = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dct['result'] = result
        logger.info(dct)
        return result

    return wrapper


@deco_func
def any_name(num: int, *args, **kwargs):
    return num ** 2  # возводим num в квадрат


def main():
    any_name(10, 42, 'Hello', name='Stanislav', x=3, y=True)


if __name__ == '__main__':
    main()
# 41:51
