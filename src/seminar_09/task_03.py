"""
Задание №3

Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и возвращаемый ею результат.
При повторном вызове файл должен расширяться,
а не перезаписываться.

Каждый ключевой параметр сохраните как отельный ключ
json словаря.

Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.

Имя файла должно совпадать с именем декорируемой функции.
"""
# 01:04:00
import json
from typing import Callable
from pathlib import Path


def test_func(func: Callable):
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def wrapper(*args, **kwargs):
        _dict = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        _dict['result'] = result
        json_file.append(_dict)
        with open(file, 'a', encoding='utf-8') as f:
            json.dump(json_file, f, indent=2)

        return result

    return wrapper


@test_func
def any_name(num: int, *args, **kwargs):
    return num


# any_name(10)
any_name(10, name='Stanislav', x=3, )