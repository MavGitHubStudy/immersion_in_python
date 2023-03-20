"""1:21:37 test_05.py - файл для написания тестов"""
import unittest
from task_02 import Triangle
from task_02_ex import TriangleSideException, TriangleExistException


class TestTriangle(unittest.TestCase):

    def setUp(self) -> None:
        # print('setUp start')
        self.t3 = Triangle(6, 2, 5)

    def test_equal(self):
        with self.assertRaises(TriangleSideException) as ex:
            self.t1 = Triangle(4, -9, 5)
        print('t1=Triangle(4, -9, 5)')
        print(f'{ex.exception.__module__}.{ex.exception.__class__.__name__}: '
              f'{ex.exception.__str__()}')

        self.assertEqual(ex.exception.__str__(),
                         (f'Недопустимое значение стороны треугольника: -9. '
                          f'Сторона треугольника должна быть больше нуля.'))

        with self.assertRaises(TriangleExistException) as ex:
            self.t2 = Triangle(4, 9, 5)
        print('t1=Triangle(4, 9, 5)')
        print(f'{ex.exception.__module__}.{ex.exception.__class__.__name__}: '
              f'{ex.exception.__str__()}')

        self.assertEqual(ex.exception.__str__(),
                         'Треугольника нет. b >= суммы других.')

    def test_area(self):
        self.assertEqual(self.t3.area(), 4.683748498798798)
        print('t3=Triangle(6, 2, 5)')
        print(f't3.area()={self.t3.area()}')
        # self.assertEqual(self.r3.area(), 4.68374849879879)


if __name__ == '__main__':
    unittest.main(verbosity=2)
