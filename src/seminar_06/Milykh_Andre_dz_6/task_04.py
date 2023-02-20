"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
варианты и выведите 4 успешных расстановки.
"""
from sys import argv
from chess import random_placement


if __name__ == '__main__':
    # print(len(argv))
    if len(argv) == 1:
        print(random_placement())
