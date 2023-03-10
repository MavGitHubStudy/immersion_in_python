# 48:48
"""
Задание № 3

Напишите функцию, которая открывает на чтение созданные в прошлых
задачах файлы с числами и именами.

Перемножьте пары чисел. В новый файл сохраните имя и произведение:

- если результат умножения отрицательный, сохраните имя записанное
  строчными буквами и произведение по модулю

- если результат умножения положительный, сохраните имя прописными
  буквами и произведение округлённое до целого.

В результирующем файле должно быть столько же строк, сколько в более
длинном файле.

При достижении конца более короткого файла, возвращайтесь в его начало.
"""
# 55:45
from pathlib import Path
from typing import TextIO


def read_or_begin(fd: TextIO) -> str:
    while(line := fd.readline()) == '':
        fd.seek(0)  # в начало файла
    return line[:-1]  # возвращаем строку без последнего символа \n


# def read_or_begin(fd: TextIO) -> str:
#     line = fd.readline()
#     if line == '':
#         fd.seek(0)  # в начало файла
#         return read_or_begin(fd)  # избавились от дублирования строк через
#         # рекурсивный вызов
#     return line[:-1]  # возвращаем строку без последнего символа \n


def unification_file(numbers: Path, strings: Path, result: Path) -> None:
    with (
      open(numbers, 'r', encoding='utf-8') as f_num,
      open(strings, 'r', encoding='utf-8') as f_str,
      open(result, 'w', encoding='utf-8') as f_res
    ):
        len_str = sum(1 for _ in f_str)  # сколько строк в этом файле
        len_num = sum(1 for _ in f_num)  #
        for _ in range(max(len_str, len_num)):
            name = read_or_begin(f_str)
            two_num = read_or_begin(f_num)
            num_i, num_f = two_num.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_res.write(f'{name.lower()} {-mult}\n')
            elif mult > 0:
                f_res.write(f'{name.upper()} {int(mult)}\n')


if __name__ == '__main__':
    unification_file(Path('numbers.txt'), Path('strings.txt'),
                     Path('result.txt'))
