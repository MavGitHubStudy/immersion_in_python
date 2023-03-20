import pytest
from task_03 import Student


# from task_03_ex import StudentStringException
# from task_03_ex import StudentAgeException
# from task_03_ex import StudentGradeException
# from task_03_ex import StudentTestException
# from task_03_ex import StudentScoreException

@pytest.fixture
def set_students():
    print('setUp start')
    std_one = Student('Иванов', 'Иван', 'Иванович', 13, 5)
    std_one.add_score('Русский язык', 3)
    std_one.add_score('Русский язык', 5)
    std_one.add_score('Математика', 4)
    std_one.add_score('Математика', 4)
    std_one.add_test('Литература', 30)
    std_one.add_test('Литература', 70)
    std_one.add_test('Литература', 50)
    return std_one


def test_average_score(set_students):
    user1 = set_students
    assert user1.get_average_score() == 4


def test_average_test(set_students):
    user1 = set_students
    assert user1.get_average_test('Литература') == 50


if __name__ == '__main__':
    # pytest.main(['-v'])
    pytest.main(['-v', 'test_03_3.py'])
