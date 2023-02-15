"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os

LINUX = '/'
WINDOWS = '\\'


def file_info(absolute_path: str):
    ch = LINUX if os.name == 'posix' else WINDOWS
    idx_path = absolute_path.rfind(ch)
    idx_name = absolute_path.rfind('.')
    file_path = absolute_path[:idx_path]
    file_name = absolute_path[idx_path + 1: idx_name]
    file_extension = absolute_path[idx_name + 1:]
    return file_path, file_name, file_extension


# Получение абсолютного пути выполняемого скрипта
file_absolute = __file__
print(file_info(file_absolute))
