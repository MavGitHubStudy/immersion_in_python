"""1:41:53 task_06.py"""
from pathlib import Path

import pytest

from task_06 import LevelError, AccessError, User, Project

"""
Задание №6

На семинаре 13 был создан проект по работе с 
пользователями (имя, id, уровень).

Напишите 3-7 тестов pytest для данного проекта.

Используйте текстуры.
"""


# from pathlib import Path
# from ..seminar_13.task_03 import LevelError, AccessError
# from ..seminar_13.task_04 import User
# from ..seminar_13.task_05_1 import Project
#
#
@pytest.fixture
def set_users():
    data = {
        # User(name="qwerty", idx="987", lvl="1"),
        # User(name="nick", idx="123", lvl="1"),
        # User(name="john", idx="456", lvl="5"),
        # User(name="smit", idx="123", lvl="7"),
        User(name="qwerty", idx=987, lvl=1),
        User(name="nick", idx=123, lvl=1),
        User(name="john", idx=456, lvl=5),
        User(name="smit", idx=123, lvl=7),
    }
    return data
    # 1:52:05


# set_users  -  имя фикстуры
def test_read_json(set_users):
    project = Project()
    # res = project.read_json(Path('names.json'))
    res = project.read_json(Path('names.json'))
    assert res == set_users


if __name__ == '__main__':
    pytest.main(['-vv'])
"""
Разобраться с путями файлов!!!
"""
