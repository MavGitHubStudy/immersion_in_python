"""1:21:37 test_05.py - файл для написания тестов"""
import unittest
from task_05 import Rectangle


class TestRectangle(unittest.TestCase):

    # готовим тестовую площадку
    def setUp(self) -> None:
        print('setUp start')
        self.r1 = Rectangle(2)
        self.r2 = Rectangle(3, 4)

    def test_equal(self):
        self.assertEqual(self.r1, Rectangle(2, 2))

    def test_perimeter(self):
        self.assertEqual(self.r2.perimeter(), 14)

    def test_add(self):
        self.assertEqual(self.r1 + self.r2, Rectangle(5, 6))

    def test_no_equal(self):
        self.assertNotEqual(self.r1, Rectangle(3, 4))
        self.assertNotEqual(self.r1, self.r2)

    def test_greater(self):
        self.assertGreater(self.r2, self.r1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
