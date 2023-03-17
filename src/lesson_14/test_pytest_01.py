# https://habr.com/ru/post/448782/
import pytest


def sum_two_num(a, b):
    return a + b
    # return f'{a}{b}


def test_sum():
    assert sum_two_num(2, 3) == 5, 'Математика покинула чат'


if __name__ == '__main__':
    pytest.main()
# 1:06:40
