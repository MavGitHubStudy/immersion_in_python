"""
task_03.py (40:40 - 43:15 - 45:10)
"""
"""
Задание №3

Создайте класс с базовым исключением и дочерние
классы-исключения:
- ошибка уровня,
- ошибка доступа.
"""


class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    pass


class AccessError(ProjectException):
    pass
