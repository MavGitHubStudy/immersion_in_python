"""
Задание №2

Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).

После каждого ввода добавляйте новую информацию
в JSON файл.

Пользователи группируются по уровню доступа.

Идентификатор пользователя выступает ключом для имени.

Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.

При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
# 28:00 - 36:25
import json
import os.path
from pathlib import Path


def get_fom_user(file: Path) -> None:
    unique_id = set()
    result = {str(i): {} for i in range(1, 7 + 1)}
    if file.is_file() and os.path.getsize(file) > 0:
        with open(file, 'r', encoding='utf-8') as js:
            result = json.load(js)
            for value in result.values():
                unique_id.update(value.keys())
            # unique_id.update(
            # *((value.keys()) for key, value in result.items()))
    print(unique_id)
    while True:
        value, user_id, name = input('>>> ').split()
        if user_id in unique_id:
            print("Такой id уже есть.")
            continue
        else:
            # print(value, user_id, name)
            result[value].update({int(user_id): name})
            with open(file, 'w', encoding='utf-8') as f:
                print(result)
                json.dump(result, f, indent=2)


if __name__ == '__main__':
    get_fom_user(Path('names.json'))
