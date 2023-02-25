"""
Задание №1

Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдоименами и произведением чисел.

Напишите функцию, которая создаёт из созданного ранее файла
новый с данными в формате JSON.

Имена пишите с большой буквы.

Каждую пару сохраняйте с новой строки.
"""
import json
from pathlib import Path


def convert_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()  # по пробелу
            file_data[name.capitalize()] = float(number)
    print(file_data)
    # 23:00
    with open(file.stem + '.json', 'w', encoding='utf-8') as f:
        # json.dump(file_data, f)
        json.dump(file_data, f, indent=2)


if __name__ == '__main__':
    convert_json(Path('../seminar_07/result.txt'))
