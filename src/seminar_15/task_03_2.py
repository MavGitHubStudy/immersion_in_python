"""44:15 - 49:15 - 50:50 task_03_2.py"""
import logging
from functools import wraps
from typing import Callable

"""
Задание №3

Доработаем задачу №2

Сохраняйте в лог файл раздельно:
- уровень логирования,
- дату события,
- имя функции (не декоратора),
- аргументы вызова, 
- результат
"""

# FORMAT = '{levelname} - {asctime} - {funcName} - {lineno} - {msg}'
# 53:00
# FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
# 57:44
FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO,
                    filename='logs_3.log',
                    encoding='utf-8',
                    format=FORMAT,
                    style='{')
logger = logging.getLogger(__name__)


def deco_func(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        dct = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        print(func.__name__)  # 56:50
        # dct['result'] = result
        logger.info(f'func: {func.__name__} - {dct} - "result": {result}')  #
        # 58:15

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
