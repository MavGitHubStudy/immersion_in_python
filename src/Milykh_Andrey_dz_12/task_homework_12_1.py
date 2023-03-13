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
import csv
import math
# from custom_validators import OneOf
from custom_validators import Number
from custom_validators import String

MIN_AGE_STUDENT_IN_RUSSIA = 9  # Алиса Теплякова, МГУ
MAX_AGE_STUDENT_IN_RUSSIA = 72  # Марк Гольдман, ГУ "Высшая школа экономики"
MIN_GRADE = 1
MAX_GRADE = 11
MIN_SCORE = 2
MAX_SCORE = 5
MIN_TEST_RESULT = 0
MAX_TEST_RESULT = 100


class Student:

    # добавляем валидаторы
    surname = String(minsize=3, maxsize=15, predicate1=str.isalpha,
                     predicate2=str.istitle)
    name = String(minsize=3, maxsize=15, predicate1=str.isalpha,
                  predicate2=str.istitle)
    patronymic = String(minsize=3, maxsize=15, predicate1=str.isalpha,
                        predicate2=str.istitle)
    age = Number(minvalue=MIN_AGE_STUDENT_IN_RUSSIA,
                 maxvalue=MAX_AGE_STUDENT_IN_RUSSIA),
    grade = Number(minvalue=MIN_GRADE, maxvalue=MAX_GRADE)

    def __init__(self, surname: str, name: str, patronymic: str, age: int,
                 grade: int):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.grade = grade

        self.subjects = []
        self.subject_scores = {}  # словарь для хранения оценок по предметам
        self.subject_tests = {}  # словарь для хранения результатов тестов
        # по предметам

        self.load_subjects()

    def __repr__(self):
        return (f'Student(surname={self.surname}, name={self.name}, '
                f'patronymic={self.patronymic}, age={self.age}, '
                f'grade={self.grade}')

    def load_subjects(self):
        with open(f'grade-{self.grade}.csv', 'r', encoding='utf-8',
                  newline='') as f_csv:
            csv_read = csv.reader(f_csv)
            for i, line in enumerate(csv_read):
                if i != 0:
                    self.subjects.append(line[1])

        # инициализация словарей оценок и тестов по предметам
        for _subject in self.subjects:
            self.subject_scores[_subject] = []
            self.subject_tests[_subject] = []

    def check_subject(self, subject: str) -> bool:
        return True if subject in self.subjects else False

    @staticmethod
    def check_score(score: int) -> bool:
        return True if MIN_SCORE <= score <= MAX_SCORE else False

    @staticmethod
    def check_test(test: int) -> bool:
        return True if MIN_TEST_RESULT <= test <= MAX_TEST_RESULT else False

    def add_score(self, subject: str, score: int) -> None:
        if not self.check_subject(subject):
            raise ValueError(f'Invalid name of the subject: {subject}')
        if not self.check_score(score):
            raise ValueError(f'Invalid value of the score: {score}')
        self.subject_scores[f'{subject}'].append(score)

    def add_test(self, subject: str, test: int) -> None:
        if not self.check_subject(subject):
            raise ValueError(f'Invalid name of the subject: {subject}')
        if not self.check_test(test):
            raise ValueError(f'Invalid value of the test: {test}')
        self.subject_tests[f'{subject}'].append(test)

    def get_average_test(self, subject: str) -> int:
        """Функция возвращает средний балл по тестам для каждого предмета"""
        if not self.check_subject(subject):
            raise ValueError(f'Invalid name of the subject: {subject}')
        return math.ceil(sum(self.subject_tests[f'{subject}']) / len(
            self.subject_tests[f'{subject}']))

    def get_average_score(self) -> int:
        """Функция возвращает средний балл по оценкам для всех предметов"""
        sum_score = 0
        num_score = 0
        for subject in self.subjects:
            sum_score += sum(self.subject_scores[f'{subject}'])
            num_score += len(self.subject_scores[f'{subject}'])
        return math.ceil(sum_score / num_score)


if __name__ == '__main__':
    std_one = Student('Иванов', 'Иван', 'Иванович', 13, 5)
    # print(f'{std_one = }')
    # print(f'{std_one.__dict__= }')

    # вводим оценки (по предметам)
    std_one.add_score('Русский язык', 2)
    std_one.add_score('Русский язык', 4)
    std_one.add_score('Русский язык', 4)

    std_one.add_score('Литература', 2)
    std_one.add_score('Литература', 4)
    std_one.add_score('Литература', 5)

    std_one.add_score('Математика', 4)
    std_one.add_score('Математика', 5)
    std_one.add_score('Математика', 3)

    # вводим результаты тестов (по предметам)
    std_one.add_test('Русский язык', 65)
    std_one.add_test('Русский язык', 80)
    std_one.add_test('Русский язык', 73)

    std_one.add_test('Литература', 30)
    std_one.add_test('Литература', 70)
    std_one.add_test('Литература', 50)

    std_one.add_test('Математика', 64)
    std_one.add_test('Математика', 75)
    std_one.add_test('Математика', 92)

    # проверяем ввод
    print(std_one.subject_scores)
    print(std_one.subject_tests)

    # средний балл тестов по Литературе
    _filter = 'Литература'
    print(f"{_filter} - cредний балл тестов: "
          f"{std_one.get_average_test(_filter)}")

    # средний бал оценок по всем предмета
    print(f"Средний балл по оценкам для всех "
          f"предметов: {std_one.get_average_score()}")
    