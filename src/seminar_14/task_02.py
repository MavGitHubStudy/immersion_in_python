"""25:50-31:35-32:40 task_02.py"""
from string import ascii_letters

"""
Задание №2

Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:

- возврат строки без изменений

- возврат строки с преобразованием регистра без потери
  символов
  
- возврат строки с удалением знаков пунктуации

- возврат строки с удалением букв других алфавитов

- возврат строки с учётом всех вышеперечисленных пунктов
  (кроме п. 1)
"""


def text_filter(s: str) -> str:
    """
    >>> text_filter('hello world')
    'hello world'
    >>> text_filter('Hello World')
    'hello world'
    >>> text_filter('hello, world')
    'hello world'
    >>> text_filter('hello Мир world')
    'hello  world'
    >>> text_filter('Hello123, World(Мир)!')
    'hello world'
    """
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()  # в нижнем регистре


if __name__ == '__main__':
    # print(text_filter('rew23qweqf 1324sdg325 ывпвfgjы'))
    import doctest  # импортируем здесь, т.к. он нужен только для тестирования

    doctest.testmod(verbose=True)

# 33:51
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_14/task_02.py 
2 items had no tests:
    __main__
    __main__.text_filter
0 tests in 2 items.
0 passed and 0 failed.
Test passed.

Process finished with exit code 0
"""
