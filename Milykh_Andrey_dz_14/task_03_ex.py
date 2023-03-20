class StudentException(Exception):
    pass


class StudentAgeException(StudentException):
    def __init__(self, age, min_age, max_age):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        return (f'Недопустимое значение возраста: {self.age}. '
                f'Возраст должен быть в диапазоне от {self.min_age} '
                f'до {self.max_age}')


class StudentGradeException(StudentException):
    def __init__(self, grade, min_grade, max_grade):
        self.grade = grade
        self.min_grade = min_grade
        self.max_grad = max_grade

    def __str__(self):
        return (f'Недопустимое значение уровня: {self.grade}. '
                f'Уровень должен быть в диапазоне от {self.min_grade} '
                f'до {self.max_grad}')


class StudentScoreException(StudentException):
    def __init__(self, score, min_score, max_score):
        self.score = score
        self.min_score = min_score
        self.max_score = max_score

    def __str__(self):
        return (f'Недопустимое значение оценки: {self.score}. '
                f'Оценка должен быть в диапазоне от {self.min_score} '
                f'до {self.max_score}')


class StudentTestException(StudentException):
    def __init__(self, test, min_test, max_test):
        self.test = test
        self.min_test = min_test
        self.max_test = max_test

    def __str__(self):
        return (f'Недопустимое значение результата теста: {self.test}. '
                f'Результат теста должен быть в диапазоне от'
                f' {self.min_test} до {self.max_test}')


class StudentStringException(StudentException):
    def __init__(self, err_str):
        self.err_str = err_str

    def __str__(self):
        return (f'Недопустимое значение \"{self.err_str}\".\n'
                f'Строка должна содержать только буквы и начинаться '
                f'с заглавной буквы!')
