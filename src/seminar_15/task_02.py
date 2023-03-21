"""26:15 task_02.py"""
# import logging
import json
from pathlib import Path
from typing import Callable

"""
Задание №2

На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.

Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""


def test_func(func: Callable):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def wrapper(*args, **kwargs):
        dct = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dct['result'] = result
        json_file.append(dct)
        with open(file, 'a', encoding='utf-8') as j_f:
            json.dump(json_file, j_f)

        return result

    return wrapper


@test_func
def any_name(num: int, *args, **kwargs):
    return num


def main():
    any_name(10, name='Stanislav', x=3)


if __name__ == '__main__':
    main()
