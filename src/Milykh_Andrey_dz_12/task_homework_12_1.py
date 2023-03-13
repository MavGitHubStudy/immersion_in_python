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
from custom_validators import OneOf
from custom_validators import Number
from custom_validators import String

MIN_AGE_STUDENT_IN_RUSSIA = 9  # Алиса Теплякова, МГУ
MAX_AGE_STUDENT_IN_RUSSIA = 72  # Марк Гольдман, ГУ "Высшая школа экономики"


class Student:
    # добавляем валидаторы
    surname = String(minsize=3, maxsize=15, predicate=str.isalpha)
    name = String(minsize=3, maxsize=15, predicate=str.isalpha)
    patronymic = String(minsize=3, maxsize=15, predicate=str.isalpha)
    age = Number(minvalue=MIN_AGE_STUDENT_IN_RUSSIA,
                 maxvalue=MAX_AGE_STUDENT_IN_RUSSIA)

    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def __repr__(self):
        return (f'Student(surname={self.surname}, name={self.name}, '
                f'patronymic={self.patronymic}, age={self.age} ')


if __name__ == '__main__':
    std_one = Student('и1анов', 'Иван', 'Иванович', 9)
    print(f'{std_one = }')
    print(f'{std_one.__dict__ = }')
