"""
Задание №3

Напишите функцию, которая сохраняет созданный
в прошлом задании файл в формате CSV.
"""
# 01:28:15 - 01:36:20
import csv
import json
import os.path
from pathlib import Path


def get_from_user(file: Path) -> None:
    # читаем файл в переменную  json_file
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)

    rows = []  # csv - файл является набором строк
    for level, value in json_file.items():
        for id, name in value.items():
            rows.append({'level': level, 'user_id': id, 'name': name})

    # открываем файл .csv для записи
    # newline=''
    with open('out.csv', 'w', newline='', encoding='utf-8') as f:
        print(json_file)
        fieldnames = ['level', 'user_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # две строки, которые
        writer.writerows(rows)  # формируют csv-файл


if __name__ == '__main__':
    get_from_user(Path('./names.json'))
