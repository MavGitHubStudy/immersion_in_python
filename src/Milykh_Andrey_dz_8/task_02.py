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


def show_comparison(message_: str, result_: bool):
    if result_:
        print(f"{message_} equal.")
    else:
        print(f"{message_} not equal.")


if __name__ == '__main__':
    # получаем текущий рабочий каталог
    work_path = os.getcwd()

    # рекурсивно обходим директорию и сохраняем результат в переменной
    res_list = dl.dir2list(work_path)

    # сохраняем переменную в файлах формата json, csv, pickle
    dl.save2json(res_list, Path('file_in.json'))
    dl.save2csv(res_list, Path('file_in.csv'))
    dl.save2pickle(res_list, Path('file_in.pickle'))

    # загружаем поочерёдно содержимое файлов в тестовую
    # переменную res_ и сравниваем её с исходной переменной res_list
    pickle_list = dl.load4pickle(Path('file_in.pickle'))
    res_ = dl.list_comparison(pickle_list, res_list)
    show_comparison("Lists res_list and pickle_list are", res_)

    csv_list = dl.load4csv(Path('file_in.csv'))
    res_ = dl.list_comparison(csv_list, res_list)
    show_comparison("Lists res_list and csv_list are", res_)

    json_list = dl.load4json(Path('file_in.json'))
    res_ = dl.list_comparison(csv_list, res_list)
    show_comparison("Lists res_list and csv_list are", res_)
