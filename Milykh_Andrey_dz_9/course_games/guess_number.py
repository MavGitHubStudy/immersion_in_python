"""
 Задача №2

 Дорабатываем задачу № 1.

 Превратите внешнюю функцию в декоратор.

 Он должен проверять, входят ли переданные в функцию-угадайку
 числа в диапазоны [1, 100] и [1, 10].

 Если не входят, вызывать функцию со случайными числами
 из диапазонов.
"""
__all__ = ['guess_num']
from random import randint
from typing import Callable

MIN_NUM = 1
MAX_NUM = 100
MIN_TRY = 1
MAX_TRY = 10


def incoming_num(func: Callable):
    _min_num = MIN_NUM
    _max_num = MAX_NUM
    _min_try = MIN_TRY
    _max_try = MAX_TRY

    def wrapper(num: int, count: int, *args, **kwargs):
        if num < _min_num or num > _max_num:
            num = randint(_min_num, _max_num)
        if count < _min_try or count > _max_try:
            count = randint(_min_try, _max_try)
        result = func(num, count, *args, **kwargs)
        return result

    return wrapper


@incoming_num
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


if __name__ == '__main__':
    guess_num(54, 7)
    guess_num(120, 13)
