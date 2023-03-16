"""task_03.py"""
import csv
import math
from task_03_ex import StudentAgeException
from task_03_ex import StudentGradeException
from task_03_ex import StudentScoreException
from task_03_ex import StudentTestException
from task_03_ex import StudentStringException
"""
Создайте класс студента.

- Используя исключения проверяйте ФИО на первую заглавную букву и
  наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании
  экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
  тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого
  предмета и по оценкам всех предметов вместе взятых.
"""


MIN_AGE_STUDENT_IN_RUSSIA = 9  # Алиса Теплякова, МГУ
MAX_AGE_STUDENT_IN_RUSSIA = 72  # Марк Гольдман, ГУ "Высшая школа экономики"
MIN_GRADE = 1
MAX_GRADE = 11
MIN_SCORE = 2
MAX_SCORE = 5
MIN_TEST_RESULT = 0
MAX_TEST_RESULT = 100


class Student:

    def __init__(self, surname: str, name: str, patronymic: str, age: int,
                 grade: int):

        if self._check_str(surname):
            self._surname = surname
        else:
            raise StudentStringException(surname)

        if self._check_str(name):
            self._name = name
        else:
            raise StudentStringException(name)

        if self._check_str(patronymic):
            self._patronymic = patronymic
        else:
            raise StudentStringException(patronymic)

        self._patronymic = patronymic

        if self._check_age(age):
            self._age = age
        else:
            raise StudentAgeException(age,  MIN_AGE_STUDENT_IN_RUSSIA,
                                      MAX_AGE_STUDENT_IN_RUSSIA)

        if self._check_grade(grade):
            self._grade = grade
        else:
            raise StudentGradeException(grade, MIN_GRADE, MAX_GRADE)

        self.subjects = []
        self.subject_scores = {}  # словарь для хранения оценок по предметам
        self.subject_tests = {}  # словарь для хранения результатов тестов
        # по предметам

        self.load_subjects()

    def __repr__(self):
        return (f'Student(surname={self._surname}, name={self._name}, '
                f'patronymic={self._patronymic}, age={self._age}, '
                f'grade={self._grade}')

    @staticmethod
    def _check_str(in_value) -> bool:
        if not isinstance(in_value, str):
            return False
        if not str.isalpha(in_value):
            return False
        if not str.istitle(in_value):
            return False
        return True

    @staticmethod
    def _check_age(age) -> bool:
        return MIN_AGE_STUDENT_IN_RUSSIA < age < MAX_AGE_STUDENT_IN_RUSSIA

    @staticmethod
    def _check_grade(grade) -> bool:
        return MIN_GRADE < grade < MAX_GRADE

    def load_subjects(self):
        with open(f'grade-{self._grade}.csv', 'r', encoding='utf-8',
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
    def _check_score(score: int) -> bool:
        return True if MIN_SCORE <= score <= MAX_SCORE else False

    @staticmethod
    def _check_test(test: int) -> bool:
        return True if MIN_TEST_RESULT <= test <= MAX_TEST_RESULT else False

    def add_score(self, subject: str, score: int) -> None:
        if not self.check_subject(subject):
            raise ValueError(f'Invalid name of the subject: {subject}')
        if not self._check_score(score):
            raise StudentScoreException(score, MIN_SCORE, MAX_SCORE)
        self.subject_scores[f'{subject}'].append(score)

    def add_test(self, subject: str, test: int) -> None:
        if not self.check_subject(subject):
            raise ValueError(f'Invalid name of the subject: {subject}')
        if not self._check_test(test):
            raise StudentTestException(test, MIN_TEST_RESULT, MAX_TEST_RESULT)
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
    std_one = Student('Иванов', 'И13ван', 'Иванович', 13, 5)

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

    