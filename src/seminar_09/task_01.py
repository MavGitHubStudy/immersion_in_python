"""
Задание №1

Создайте функцию-замыкание, которая запрашивает два целых числа:
- от 1 до 100 для загадывания
- от 1 до 10 для количества попыток

Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
# 15:30
from random import randint
from typing import Callable

MIN_NUM = 1
MAX_NUM = 100
MIN_TRY = 1
MAX_TRY = 10


def incoming_num(find_num: int, try_num: int) -> Callable[[], None]:
    def guess_num():
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

    return guess_num


# print(incoming_num(10, 5))
"""
<function incoming_num.<locals>.guess_num at 0x7f2251d8caf0>

Process finished with exit code 0
"""
game = incoming_num(randint(MIN_NUM, MAX_NUM), randint(MIN_TRY, MAX_TRY))
print(game)
game()
