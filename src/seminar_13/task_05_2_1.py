"""
task_05.py  (1:06:05 1:13:54)
"""
import json
from pathlib import Path

from task_03 import AccessError

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

    # 1:34:37
    def __eq__(self, other):
        return self.idx == other.idx and self.name == other.name

    def __hash__(self):
        return hash((self.idx, self.name))

    def __repr__(self):
        return f'User(lvl={self.lvl}, idx={self.idx}, name={self.name})'


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
                self._users.add(User(lvl=int(key), idx=int(idx), name=name))

        return self._users

    def sign_in(self, name, idx):
        # Временный пользователь
        spam_user = User(name=name, idx=idx, lvl=0)
        # if spam_user in self._users:  # поиск на основе hash
        #     print('Совпало')  # 1:38:46
        # else:
        #     raise AccessError('Отказано в доступе')
        if spam_user not in self._users:  # 1:51:49
            raise AccessError('Отказано в доступе')
        print('Совпало')
        for user in self._users:
            if user == spam_user:
                return user


def main():
    project = Project()
    res = project.read_json(Path('names.json'))
    print(f'{res = }')
    # 1:45:15
    # project.sign_in("john", 456)
    # 1:54:44
    print(project.sign_in("john", 456))


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
