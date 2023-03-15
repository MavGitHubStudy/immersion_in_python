"""
task_06.py  (1:27:00 - 1:30:15)
"""
import json
from pathlib import Path

from task_03 import AccessError
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
                self._users.add(User(int(lvl), int(idx), name))
                # self._users.add(User(lvl, idx, name))
                """
                1:40:55
                 File "/home/.../src/seminar_13/task_06_1.py", 
                 line 37, in read_json
                    self._users.add(User(lvl, idx, name))
                TypeError: unhashable type: 'User'
                """
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
    # print(project.sign_in("john", 456))
    print(project.sign_in("nick", 12345))


if __name__ == '__main__':
    main()
# 1:41:54
"""
/home/.../.venv/bin/python /home/.../src/seminar_13/task_05_1.py 
res = {<task_04.User object at 0x7f8b2e2dc610>,
 <task_04.User object at 0x7f8b2e2dc5b0>,
  <task_04.User object at 0x7f8b2e2dc9d0>,
   <task_04.User object at 0x7f8b2e2dc970>}

Process finished with exit code 0
"""
