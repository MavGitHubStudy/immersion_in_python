"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import sys
import os

LINUX = '/'
WINDOWS = '\\'


def file_info(absolute_path: str):
    """ Для ОС Linux и WINDOWS"""
    ch = LINUX if os.name == 'posix' else WINDOWS
    idx_path = absolute_path.rfind(ch)
    idx_name = absolute_path.rfind('.')
    file_path = absolute_path[:idx_path]
    file_name = absolute_path[idx_path + 1: idx_name]
    file_extension = absolute_path[idx_name + 1:]
    return file_path, file_name, file_extension


# Получение абсолютного пути выполняемого скрипта
script_name = sys.argv[0]
abspath = os.path.abspath(script_name)

# Вызов нашей функции
path_, file_, extension_ = file_info(abspath)
print(f"путь = {path_}, имя файла = {file_}, расширение = {extension_}")
