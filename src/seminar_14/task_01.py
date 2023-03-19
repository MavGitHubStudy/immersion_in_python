"""13:00-15:00 task_01.py"""
from string import ascii_letters

"""
Задание №1

Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.

Возвращается строка в нижнем регистре.
"""


def text_filter(s: str) -> str:
    # заготовка
    # result = ''.join(c for c in s if c.isascii())  # 20:35
    # result = ''.join(c for c in s if c.isalpha() or c.isspace())  # 21:28
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))  # 24:23

    return result.lower()  # в нижнем регистре


if __name__ == '__main__':
    # 20:35
    print(text_filter('rew23qweqf 1324sdg325 ывпвfgjы'))
"""
# 20:35
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_14/task_01.py 
rew23qweqf 1324sdg325 fgj

Process finished with exit code 0
"""
"""
# 21:28
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_14/task_01.py 
rewqweqf sdg ывпвfgjы

Process finished with exit code 0
"""
"""
# 25:00
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_14/task_01.py 
rewqweqf sdg fgj

Process finished with exit code 0
"""
