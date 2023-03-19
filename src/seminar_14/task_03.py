"""52:34 task_03.py"""
import unittest
from string import ascii_letters

"""
Задание №3

Напишите для задачи 1 тесты unittest. Проверьте
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


class TestTextFilter(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(text_filter('hello world'), 'hello world')

    def test_upper_lower(self):
        self.assertEqual(text_filter('Hello World'), 'hello world')

    def test_without_punctuation(self):
        self.assertEqual(text_filter('hello, world!'), 'hello world')

    def test_english_only(self):
        self.assertEqual(text_filter('hello Мир world'), 'hello  world')

    def test_all_filters(self):
        self.assertEqual(text_filter('Hello123, World(Мир)!'), 'hello world')


if __name__ == '__main__':
    # print(text_filter('rew23qweqf 1324sdg325 ывпвfgjы'))
    unittest.main(verbosity=2)
# 59:00
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_14/task_03.py 
test_no_change (__main__.TestTextFilter) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

Process finished with exit code 0
"""
