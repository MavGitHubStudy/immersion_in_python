"""11:54 task_01.py"""
import logging

"""
Задание №1

Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.

Например, отлавливаем ошибку деления на ноль.
"""

logging.basicConfig(level=logging.ERROR,
                    filename='ZeroDivisionError_1.log',
                    encoding='utf-8')
logger = logging.getLogger(__name__)


def func_div_two(a, b) -> float:
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(f'Ошибка деления числа  {a} на число {b}')
        return float('inf')  # возвращаем бесконечность
    return res


def main():
    print(func_div_two(5, 0))


if __name__ == '__main__':
    main()
# 21:34 - появился файл ZeroDivisionError.log
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_15/task_01_1.py 
inf

Process finished with exit code 0
"""
