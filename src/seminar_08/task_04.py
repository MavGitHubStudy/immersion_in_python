"""
Задание №4

Прочитайте созданный в прошлом задании csv файл без
использования scs.DictReader.

Дополните id до 10 цифр незначащими нулями.

В именах первую букву сделайте прописной.

Добавьте поле хеш на основе имени и идентификатора.

Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.

Имя исходного и конченого файлов передавайте как аргументы
функции.
"""
# 01:47:00 - 01:56:30
import csv
import json
from pathlib import Path


def csv2json(file_out: Path, file_in: Path) -> None:
    json_list = []
    with open(file_out, 'r', encoding='utf-8') as csv_f:
        reader = csv.reader(csv_f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            json_dict = {}
            level, user_id, name = row  # строка - это список из 3-х значений
            json_dict['level'] = int(level)
            json_dict['id'] = user_id.zfill(10)
            json_dict['name'] = name.title()
            json_dict['hash'] = hash(f'{user_id}{name}')
            json_list.append(json_dict)

    with open(file_in, 'w', encoding='utf-8') as json_f:
        json.dump(json_list, json_f, indent=2)


if __name__ == '__main__':
    csv2json(Path('out.csv'), Path('json_in.json'))
