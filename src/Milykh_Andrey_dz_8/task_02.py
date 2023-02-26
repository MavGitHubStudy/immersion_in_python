"""
task_02.py

Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните
в файлы json, csv и pickle.

- Для дочерних объектов указывайте родительскую директорию.

- Для каждого объекта укажите файл это или директория.

- Для файлов сохраните его размер в байтах, а для директорий
  размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
from pathlib import Path
from package_for_serialization import dir2list as dl


if __name__ == '__main__':
    # получаем текущий рабочий каталог
    work_path = os.getcwd()
    res_list = dl.dir2list(work_path)
    # сохраняем результаты в файлах
    dl.save2json(res_list, Path('file_in.json'))
    dl.save2csv(res_list, Path('file_in.csv'))
    dl.save2pickle(res_list, Path('file_in.pickle'))

    pickle_list = dl.load4pickle(Path('file_in.pickle'))

    res = [x for x in res_list +
           pickle_list if x not in res_list or x not in pickle_list]

    # print(res)
    if not res:
        print("Lists res_list and pickle_list are equal")
    else:
        print("Lists res_list and pickle_list are not equal")
