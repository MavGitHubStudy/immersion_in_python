"""
task_04.py (45:50 - 53:44 - 57:03)
"""
import json
from pathlib import Path

"""
Задание №4

Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный идентификатор
и уровень доступа (от 1 до 7), сохраняя информацию в JSON файл.

- Напишите класс пользователя, который хранит эти данные в
  свойствах экземпляра.
- Отдельно напишите функцию, которая считывает информацию 
  из JSON файла и формирует множество пользователей.
"""


class User:
    def __init__(self, lvl, idx, name):
        self.lvl = lvl
        self.idx = idx
        self.name = name

    def __eq__(self, other):
        return self.idx == other.idx and self.name == other.name
        # if self.idx == other.idx and self.name == other.name:
        #     return True
        # else:
        #     return False

    def __hash__(self):
        return hash((self.idx, self.name))

    def __repr__(self):
        return f'User(lvl={self.lvl}, idx={self.idx}, name={self.name})'


def read_json(file: Path) -> set[User]:  # 1:01:56
    users = set()

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key, value in data.items():
        for idx, name in value.items():
            users.add(User(lvl=key, idx=idx, name=name))
    return users  # 1:01:56


def main():
    res = read_json(Path('names.json'))
    print(f'{res = }')


if __name__ == '__main__':
    main()
# 1:04:05
"""
home/.../.venv/bin/python /home/.../src/seminar_13/task_04.py 
res = {<__main__.User object at 0x7f8069676410>, 
 <__main__.User object at 0x7f8069676bc0>,
  <__main__.User object at 0x7f80696761a0>,
   <__main__.User object at 0x7f8069677040>}

Process finished with exit code 0
"""
