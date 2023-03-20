"""1:21:37 test_05.py - файл для написания тестов"""
import unittest
from task_01 import Rectangle


class TestRectangle(unittest.TestCase):

    # готовим тестовую площадку
    def setUp(self) -> None:
        print('setUp start')
        self.r1 = Rectangle(2)
        self.r2 = Rectangle(3, 4)

    def test_equal(self):
        self.assertEqual(self.r1.length, 2)
        self.assertEqual(self.r1.width, 2)

    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter(), 8)

    def test_area(self):
        self.assertEqual(self.r2.area(), 12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
