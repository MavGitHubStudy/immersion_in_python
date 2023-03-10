"""
Задание
I. Решить задачи, которые не успели решить на семинаре.
II. Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и
  наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании
  экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
  тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого
  предмета и по оценкам всех предметов вместе взятых.
"""


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше '
                             f'или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше '
                             f'{self.max_value}')


class Student:
    age = Range(3, 103)
    grade = Range(1, 11 + 1)
    office = Range(3, 42 + 1)

    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return (f'Student(name={self.name}, age={self.age} '
                f'grade={self.grade}, office={self.office}')


if __name__ == '__main__':
    std_one = Student('Архимед', 12, 4, 29)
    # std_other = Student('Аристотель', 2406, 5, 17)  # ValueError: Значение 2406
    # # должно быть меньше 103
    print(f'{std_one = }')
    std_one.age = 15
    print(f'{std_one = }')
    # std_one.grade = 11.0  # TypeError: Значение 11.0 должно быть целым числом
    # std_one.office = 73  # ValueError: Значение 73 должно быть меньше 42
    # del std_one.age  # AttributeError: Свойство "_age" нельзя удалять
    print(f'{std_one.__dict__ = }')
"""
Traceback (most recent call last):
  File "/home/.../lesson_12/task_descriptor_03.py", line 48, in <module>
    std_other = Student('Аристотель', 2406, 5, 17)  # ValueError: Значение 2406
  File "/home/.../lesson_12/task_descriptor_03.py", line 37, in __init__
    self.age = age
  File "/home/.../lesson_12/task_descriptor_03.py", line 13, in __set__
    self.validate(value)
  File "/home/.../work/gb/immersion_in_python/src/lesson_12/task_descriptor_03.py", line 26, in validate
    raise ValueError(f'Значение {value} должно быть меньше '
ValueError: Значение 2406 должно быть меньше 103

Process finished with exit code 1
"""
# 1:02:37
