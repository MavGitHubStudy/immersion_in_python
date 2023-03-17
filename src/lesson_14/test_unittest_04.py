import unittest


class TestSample(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [2, 3, 5, 7]
        print('Выполнил setUp')  # Только для демонстрации работы метода

    def test_append(self):
        self.data.append(11)
        self.assertEqual(self.data, [2, 3, 5, 7, 11])

    def test_remove(self):
        self.data.remove(5)
        self.assertEqual(self.data, [2, 3, 7])

    def test_pop(self):
        self.data.pop()
        self.assertEqual(self.data, [2, 3, 5])


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_14/test_unittest_04.py 
Выполнил setUp
Выполнил setUp
Выполнил setUp
test_append (__main__.TestSample) ... ok
test_pop (__main__.TestSample) ... ok
test_remove (__main__.TestSample) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

Process finished with exit code 0
"""
