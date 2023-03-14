"""
task_05.py  (1:06:05 1:13:54)
"""
import json
from pathlib import Path

"""
Задание №5

Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:

- загрузка данных (функция из задания 4)

- вход в систему - требует указать имя и id пользователя. Для
  проверки наличия пользователя в множестве используйте
  магический метод проверки на равенство пользователей.
  Если такого пользователя нет, вызывайте исключение доступа.
  А если пользователь есть, получите его уровень из множества
  пользователей.
  
- добавление пользователя. Если уровень пользователя меньше,
  чем ваш уровень, вызывайте исключение уровня доступа.
"""


class User:
    def __init__(self, lvl, idx, name):
        self.lvl = lvl
        self.idx = idx
        self.name = name


class Project:

    # 1:18:20
    def __init__(self):
        self._users = set()

    def read_json(self, file: Path) -> set[User]:
        # users = set()

        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key, value in data.items():
            for idx, name in value.items():
                self._users.add(User(lvl=key, idx=idx, name=name))

        return self._users


def main():
    project = Project()
    res = project.read_json(Path('names.json'))
    print(f'{res = }')


if __name__ == '__main__':
    main()
# 1:20:22
"""
/home/.../.venv/bin/python /home/.../src/seminar_13/task_05_2.py 
res = {<__main__.User object at 0x7f6cc3d7e200>,
 <__main__.User object at 0x7f6cc3d7ea40>,
  <__main__.User object at 0x7f6cc3d7e2c0>,
   <__main__.User object at 0x7f6cc3da5870>}

Process finished with exit code 0
"""
