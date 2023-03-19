"""1:07:17 task_04.py"""
import pytest
from string import ascii_letters

"""
Задание №4

Напишите для задачи 1 тесты pytest. Проверьте
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
    # """
    # >>> text_filter('hello world')
    # 'hello world'
    # >>> text_filter('Hello World')
    # 'hello world'
    # >>> text_filter('hello, world')
    # 'hello world'
    # >>> text_filter('hello Мир world')
    # 'hello  world'
    # >>> text_filter('Hello123, World(Мир)!')
    # 'hello world'
    # """
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()  # в нижнем регистре


def test_no_change():
    assert text_filter('hello world') == 'hello world'


def test_upper_lower():
    assert text_filter('Hello World') == 'hello world'


def test_without_punctuation():
    assert text_filter('hello, world!') == 'hello world'


def test_english_only():
    assert text_filter('hello Мир world') == 'hello  world'


def test_all_filters():
    assert text_filter('Hello123, World(Мир)!') == 'hello world'


if __name__ == '__main__':
    # print(text_filter('rew23qweqf 1324sdg325 ывпвfgjы'))
    pytest.main(['-vv'])
