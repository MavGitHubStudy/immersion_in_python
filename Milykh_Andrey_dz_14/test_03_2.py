import unittest
from task_03 import Student


# from task_03_ex import StudentStringException
# from task_03_ex import StudentAgeException
# from task_03_ex import StudentGradeException
# from task_03_ex import StudentTestException
# from task_03_ex import StudentScoreException


class TestStudent(unittest.TestCase):

    # готовим тестовую площадку
    def setUp(self):
        print('setUp start')
        self.std_one = Student('Иванов', 'Иван', 'Иванович', 13, 5)
        self.std_one.add_score('Русский язык', 3)
        self.std_one.add_score('Русский язык', 5)
        self.std_one.add_score('Математика', 4)
        self.std_one.add_score('Математика', 4)
        self.std_one.add_test('Литература', 30)
        self.std_one.add_test('Литература', 70)
        self.std_one.add_test('Литература', 50)

    def test_average_score(self):
        self.assertEqual(self.std_one.get_average_score(), 4)

    def test_average_test(self):
        self.assertEqual(self.std_one.get_average_test('Литература'), 50)


if __name__ == '__main__':
    unittest.main(verbosity=2)
