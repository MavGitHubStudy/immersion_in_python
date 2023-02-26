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
__all__ = ['dir2list', 'save2json', 'save2csv']
import os
import json
import csv
import pickle
from pathlib import Path
from typing import List


def dir2list(crawl_path: str) -> List:
    json_list = list()
    for root, dirs, files in os.walk(crawl_path):
        for _dir in dirs:
            json_dict = dict()
            json_dict['name'] = _dir
            json_dict['parent'] = root
            json_dict['is_dir'] = True
            json_dict['size'] = Path(os.path.join(root, _dir)).stat().st_size
            json_list.append(json_dict)
        for _file in files:
            json_dict = dict()
            json_dict['name'] = _file
            json_dict['parent'] = root
            json_dict['is_dir'] = False
            json_dict['size'] = Path(os.path.join(root, _file)).stat().st_size
            json_list.append(json_dict)

    return json_list
    # print(json_list)
    # for item in json_list:
    #     print(item)


def save2json(crawl_list: List, file_name: Path) -> None:
    with open(file_name, 'w', encoding='utf-8') as json_f:
        json.dump(crawl_list, json_f, indent=2)


def save2csv(crawl_list: List, file_name: Path) -> None:
    # открываем файл .csv для записи, newline=''
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_f:
        fieldnames = ['name', 'parent', 'is_dir', 'size']
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
        writer.writeheader()  # две строки, которые
        writer.writerows(crawl_list)  # формируют csv-файл


def save2pickle(crawl_list: List, file_name: Path) -> None:
    # открываем файл .pickle для записи
    with open(file_name, 'wb') as pickle_f:
        pickle.dump(crawl_list, pickle_f)


def load4pickle(file_name: Path) -> List:
    # открываем файл .pickle для чтения
    with open(file_name, 'rb') as pickle_f:
        return pickle.load(pickle_f)


if __name__ == '__main__':
    #  получаем текущий рабочий каталог
    work_path = os.getcwd()
    # print(work_path)
    res_list = dir2list(work_path)
    print(res_list)
