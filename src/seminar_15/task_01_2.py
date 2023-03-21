"""11:54 task_01.py"""
import logging

"""
Задание №1

Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.

Например, отлавливаем ошибку деления на ноль.
"""

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.ERROR,
                    filename='ZeroDivisionError_2.log',
                    encoding='utf-8',
                    format=FORMAT,
                    style='{')
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
# 24:07
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_15/task_01_2.py 
Traceback (most recent call last):
  File "/home/.../immersion_in_python/src/seminar_15/task_01_2.py", line 14, 
  in <module>
    logging.basicConfig(level=logging.ERROR,
  File "/usr/lib/python3.10/logging/__init__.py", line 2052, in basicConfig
    fmt = Formatter(fs, dfs, style)
  File "/usr/lib/python3.10/logging/__init__.py", line 589, in __init__
    self._style.validate()
  File "/usr/lib/python3.10/logging/__init__.py", line 429, in validate
    raise ValueError("Invalid format '%s' for '%s' style" % (self._fmt, 
    self.default_format[0]))
ValueError: Invalid format '{asctime} {levelname} {funcName}->{lineno}: {msg}' 
for '%' style

Process finished with exit code 1
"""
# Для устранения добавляем параметр
# style='{'
