# 25:00
"""
Задание №2

Напишите функцию, которая генерирует псевдоимена.

Имя должно начинаться с заглавной буквы, состоять из 4-7
букв, среди которых обязательно должны быть гласные.

Полученные имена сохраните в файл.
"""
# 34:20

# import string
from random import choice, randint
from pathlib import Path

CONSONANTS = 'bcdfghjklmnpqrstvwxz'
VOWELS = 'aeiouy'


def fill_strings(count_strings: int,
                 str_len_min: int,
                 str_len_max: int,
                 file_1: Path):
    # letters = string.ascii_uppercase
    with open(file_1, 'a', encoding='utf-8') as f_1:
        for _ in range(count_strings):
            rand_string = ''.join(choice(VOWELS) if i % 3 == 0 else choice(
                CONSONANTS) for i in range(
                randint(str_len_min, str_len_max)))
            f_1.write(f'{rand_string.capitalize()}\n')


if __name__ == '__main__':
    fill_strings(10, 4, 7, Path('strings.txt'))
