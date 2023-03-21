"""11:54 task_01.py"""
import logging

"""
Задание №1

Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.

Например, отлавливаем ошибку деления на ноль.
"""


def func_div_two(a, b) -> float:
    res = a / b
    return res


def main():
    print(func_div_two(5, 0))


if __name__ == '__main__':
    main()
# 16:00
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_15/task_01.py 
Traceback (most recent call last):
  File "/home/.../immersion_in_python/src/seminar_15/task_01.py", 
  line 24, in <module>
    main()
  File "/home/.../immersion_in_python/src/seminar_15/task_01.py", 
  line 20, in main
    print(func_div_two(5, 0))
  File "/home/.../immersion_in_python/src/seminar_15/task_01.py", 
  line 15, in func_div_two
    res = a / b
ZeroDivisionError: division by zero

Process finished with exit code 1
"""
