"""
Задание №1

Напишите фукнцию, которая зполняет файл (добавляет в конец)
случайными парами чисел.

Первое число int, второе - float разделены вертикальной чертой.

Минимальное число -   -1000, максимальное -   +1000.

Количество строк и имя файла передаются как аргументы функции.
"""
from pathlib import Path
from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def fill_nujmbers(count: int, file: str | Path):
    with open(file, 'a', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{randint(MIN_NUM, MAX_NUM)}|'
                    f'{uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    fill_nujmbers(10, Path('numbers.txt'))
