# https://habr.com/ru/post/448782/
import pytest


def sum_two_num(a, b):
    # return a + b  # 1:06:40
    return f'{a}{b}'  # 1:09:48


def test_sum():
    assert sum_two_num(2, 3) == 5, 'Математика покинула чат'


if __name__ == '__main__':
    # pytest.main()
    pytest.main(['test_pytest_01.py::test_sum'])
    # pytest.main(['-q', '-s', 'test_pytest_01.py::test_sum'])
# 1:06:40
"""
=========================== test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /home/.../immersion_in_python/src/lesson_14
collected 1 item

test_pytest_01.py .                                                      [100%]

============================== 1 passed in 0.02s ===============================

Process finished with exit code 0
"""
# 1:09:48
"""
/home/.../gb/immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_pytest_01.py 
============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /home/novichkov/work/gb/immersion_in_python/src/lesson_14
collected 1 item

test_pytest_01.py F                                                      [100%]

=================================== FAILURES ===================================
___________________________________ test_sum ___________________________________

    def test_sum():
>       assert sum_two_num(2, 3) == 5, 'Математика покинула чат'
E       AssertionError: Математика покинула чат
E       assert '23' == 5
E        +  where '23' = sum_two_num(2, 3)

test_pytest_01.py:11: AssertionError
=========================== short test summary info ============================
FAILED test_pytest_01.py::test_sum - AssertionError: Математика покинула чат
============================== 1 failed in 0.07s ===============================

Process finished with exit code 0
"""
#
"""
Запуск из командной строки:
(.venv) novichkov@linuxhint: ~/work/gb/immersion_in_python/src/lesson_14 
(lesson_14) $ pytest -v test_pytest_01.py

"""
