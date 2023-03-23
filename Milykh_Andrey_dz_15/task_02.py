"""task_02.py"""
import argparse
import os.path
import logging
from math import sqrt
from task_02_ex import TriangleSideException
from task_02_ex import TriangleExistException

"""
Сравнение экземпляров класса

Python поддерживает определение шести основных операций
сравнения экземпляров
__eq__    - равно, ==
__ne__    - не равно, !=
__gt__    - больше, >
__ge__    - не больше, меньше или равно, <=
__lt__    - меньше, <
__le__    - не меньше, больше или равно, >=
"""


# только имя файла
script_name = os.path.basename(__file__)

# получение пользовательского логгера и установка уровня логирования
py_logger = logging.getLogger(script_name)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"{script_name}.log", mode='w')
py_formatter = logging.Formatter("{name} - {levelname} - {asctime} - {msg}",
                                 style='{')

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)


class Triangle:
    def __init__(self, a, b, c):

        self.flag = ''

        if not self._check_side(a):
            py_logger.error(f"triangle not created - invalid size"
                            f" side a: {a}")
            raise TriangleSideException(a)
        if not self._check_side(b):
            py_logger.error(f"triangle not created - invalid size"
                            f" side b: {b}")
            raise TriangleSideException(b)
        if not self._check_side(c):
            py_logger.error(f"triangle not created - invalid size"
                            f" side c: {c}")
            raise TriangleSideException(c)

        if not self._triangle_exist(a, b, c):
            py_logger.error(f"triangle not created - invalid size"
                            f" side {self.flag}: >= than other two")
            raise TriangleExistException(self.flag)
        else:
            self.a = a
            self.b = b
            self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

    def __hash__(self):
        """Пытаемся вычислить хэш от нашего экземпляра"""
        return hash((self.a, self.b, self.c))

    @staticmethod
    def _check_side(side) -> bool:
        return side > 0

    def _triangle_exist(self, a, b, c):
        if a + b > c:
            if a + c > b:
                if b + c > a:
                    pass
                else:
                    self.flag = 'a'
            else:
                self.flag = 'b'
        else:
            self.flag = 'c'

        return False if self.flag != '' else True


def parser_func():
    parser = argparse.ArgumentParser('Вычисляем площадь и хэш '
                                     'треугольника, получив размеры '
                                     'его сторон, как параметры.')
    parser.add_argument('-a', '--side_a', default='1')
    parser.add_argument('-b', '--side_b', default='1')
    parser.add_argument('-c', '--side_c', default='1')
    args = parser.parse_args()

    # print(args)
    side_a = float(args.side_a)
    side_b = float(args.side_b)
    side_c = float(args.side_c)

    try:
        t1 = Triangle(side_a, side_b, side_c)
    except (TriangleSideException, TriangleSideException) as e:
        return f'{e} Программа завершена.'
    result = (f'Triangle with sides a={side_a}, b={side_b}, c={side_c} have '
              f'area={t1.area():.3f} and hase={t1.__hash__()}')
    py_logger.info(result)
    return result


def main():
    try:
        triangle_set = {Triangle(4, 8, 5), Triangle(6, 2, 5),
                        Triangle(4, 4, 4), Triangle(3, 5, 3)}
        print(f"triangle_set = {triangle_set}")
        py_logger.info(f"triangle_set created = {triangle_set}")
        areas = ', '.join(f'{item.area():.3f}' for item in triangle_set)
        print(f"areas of triangles from the set: {areas}")
        py_logger.info(f"areas of triangles from the set: {areas}")
        hashes = ', '.join(f'{item.__hash__()}' for item in triangle_set)
        print(f"heshes of triangles from the set: {hashes}")
        py_logger.info(f"heshes of triangles from the set: {hashes}")
    except (TriangleSideException, TriangleExistException) as e:
        py_logger.error(f"triangle_set not created - {e}")
        print(e)
    py_logger.info(f"Shutting down the script "
                   f" {script_name}... ")


def con():
    try:
        print(parser_func())
    except SystemExit:
        py_logger.error("Starting in the help mode or Incorrect script launch.")
        print("Starting in the help mode or Incorrect script launch")
    finally:
        py_logger.info(f"Shutting down the script "
                       f" {script_name}... ")


if __name__ == '__main__':
    py_logger.info(f"Starting the script "
                   f" {script_name}... ")
    # main()
    con()
