# 01:24:00
"""
Задание №4

Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:

- расширение

- минимальная длина случайно сгенерированного имени, по умолчанию 6

- максимальная длина случайно сгенерированного имени, по умолчанию 30

- минимальное число случайных байт, записанных в файл, по умолчанию 256

- максимальное число случайных байт, записанных в файл, по умолчанию 4096

- количество файлов, по умолчанию 42

Имя файла и его размер должны быть в рамках переданного диапазона.
"""
# 01:30:10
from random import choices, randint  # choices !!!
from string import ascii_letters, digits  # маленькие и большие букувы и цифры
from task_02 import fill_strings


def make_files(extension: str,
               min_name: int = 6,
               max_name: int = 30,
               min_size: int = 256,
               max_size: int = 4096,
               count: int = 42):
    for _ in range(count):
        name = ''.join(choices(
            ascii_letters+digits, k=randint(min_name, max_name)))
        # print(name)
        data = bytes(randint(0, 255) for _ in range(randint(min_size,
                                                            max_size)))
        # байт может быть числом в диапазоне от 0 до 255 !!!
        # print(data)
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    # make_files('bin', count=1)  # заготовка
    print('*' * 80)
    make_files('bin', count=10)  # заготовка