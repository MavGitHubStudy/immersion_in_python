"""
Задание №5

Объедините функции из прошлых задач.

Функцию угадайку задекорируйте:
- декораторам для сохранения параметров
- декоратором контроля значений
- декоратором для многократного запуска

Выберите верный порядок декораторов.
"""
# 01:28:17
import json
from random import randint
from typing import Callable
from pathlib import Path

MIN_NUM = 1
MAX_NUM = 100
MIN_TRY = 1
MAX_TRY = 10


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
        with open(file, 'a', encoding='utf-8') as f_json:
            json.dump(json_file, f_json, indent=2)

        return result

    return wrapper


def count(n: int = 1):

    def deco(func: Callable):
        counts = []

        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
                counts.append(result)

            return counts

        return wrapper

    return deco


def incoming_num(func: Callable):
    _min_num = MIN_NUM
    _max_num = MAX_NUM
    _min_try = MIN_TRY
    _max_try = MAX_TRY

    def wrapper(_num: int, _count: int, *args, **kwargs):
        if _num < _min_num or _num > _max_num:
            _num = randint(_min_num, _max_num)
        if _count < _min_try or _count > _max_try:
            _count = randint(_min_try, _max_try)
        result = func(_num, _count, *args, **kwargs)
        return result

    return wrapper


@count(5)
@incoming_num
@test_func
def guess_num(find_num: int, try_num: int):
    for i in range(1, try_num + 1):
        print(f'Пробуем угадать целое число. Попытка №{i} из {try_num}.',
              end=' ')
        user_num = int(input(f'Введите число от {MIN_NUM} до {MAX_NUM}: '))
        if user_num == find_num:
            print(f'Вы угадали! Искомое число - {find_num}')
            break
        elif user_num < find_num:
            print('Искомое число больше.')
        elif user_num > find_num:
            print('Искомое число меньше.')
    else:
        print(f'Количество попыток исчерпано! '
              f'Искомое число {find_num} не найдено.')


guess_num(50, 3)
# guess_num(120, 13)
