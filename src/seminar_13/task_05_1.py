"""
task_05.py  (1:06:05 1:13:54)
"""
import json
from pathlib import Path
from task_04 import User

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


class Project:
    _users = set()

    def read_json(self, file: Path):

        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for lvl, value in data.items():
            for idx, name in value.items():
                self._users.add(User(lvl, idx, name))

        return self._users


def main():
    project = Project()
    res = project.read_json(Path('names.json'))
    print(f'{res = }')


if __name__ == '__main__':
    main()
# 1:20:34
"""
/home/.../.venv/bin/python /home/.../src/seminar_13/task_05_1.py 
res = {<task_04.User object at 0x7f8b2e2dc610>,
 <task_04.User object at 0x7f8b2e2dc5b0>,
  <task_04.User object at 0x7f8b2e2dc9d0>,
   <task_04.User object at 0x7f8b2e2dc970>}

Process finished with exit code 0
"""
