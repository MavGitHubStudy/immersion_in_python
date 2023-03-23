""" task_01.py """
import argparse
import os.path
import logging
from task_01_ex import RectangleLengthException, RectangleWidthException

"""
- Напишите классы исключения с выводом подробной 
  информации.
  
- Поднимайте исключения внутри основного кода. Например, 
  нельзя создавать прямоугольник со сторонами отрицательной
  длины.
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


class Rectangle:

    def __init__(self, length, width=None):
        py_logger.info(f"start of rectangle creation...")
        if self._check_size(length):
            self._length = length
            py_logger.info(f"rectangle length: {length}")
        else:
            py_logger.error(f"rectangle not created - invalid length: {length}")
            raise RectangleLengthException(length)

        if width is None:
            self._width = self.length
            py_logger.info(f"rectangle width: {length}")
        else:
            if self._check_size(width):
                self._width = width
                py_logger.info(f"rectangle width: {width}")
                py_logger.info(f"rectangle created successfully")
            else:
                py_logger.error(f"rectangle not created - invalid width: "
                                f"{width}")
                raise RectangleWidthException(width)

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    @staticmethod
    def _check_size(rect_size) -> bool:
        return rect_size > 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length_value):
        if not self._check_size(length_value):

            py_logger.error(f"rectangle {self.__name__}length not changed - "
                            f"invalid "
                            f"value: {length_value}")
            raise RectangleLengthException(length_value)
        self._length = length_value
        py_logger.info(f"rectangle length changed - new "
                       f"length: {length_value}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_value):
        if not self._check_size(width_value):
            py_logger.error(f"rectangle width not changed - invalid "
                            f"value: {width_value}")
            raise RectangleWidthException(width_value)
        self._width = width_value
        py_logger.info(f"rectangle width changed - new "
                       f"width: {width_value}")


def parser_func():
    parser = argparse.ArgumentParser('Вычисляем периметр и площадь '
                                     'прямоугольника, получив его длину и '
                                     'ширину, как параметры.')
    parser.add_argument('-l', '--length', default='1')
    parser.add_argument('-w', '--width', default='1')
    args = parser.parse_args()

    # print(args)
    length = float(args.length)
    width = float(args.width)
    try:
        r1 = Rectangle(length, width)
    except (RectangleLengthException, RectangleWidthException) as e:
        return f'{e} Программа завершена.'
    result = (f'Rectangle with length={length} and width={width} '
              f'have perimeter={r1.perimeter()} and area={r1.area()}'
              )
    py_logger.info(result)
    return result


def main():
    try:
        r1 = Rectangle(-4)
    except RectangleLengthException as e:
        print(e)

    r1 = Rectangle(2, 2)
    if isinstance(r1, Rectangle):
        py_logger.info(f"perimeter of a rectangle with length={r1.length} "
                       f"and width={r1.width} equal to {r1.perimeter()}")

    r2 = Rectangle(3)
    if isinstance(r2, Rectangle):
        try:
            r2.width = -3
        except RectangleWidthException as e:
            print(e)

    if isinstance(r2, Rectangle):
        py_logger.info(f"area of a rectangle with length={r2.length} "
                       f"and width={r2.width} equal to {r2.area()}")

    py_logger.info(f"Shutting down the script "
                   f" {script_name}... ")


def con():
    try:
        print(parser_func())
    except SystemExit:
        py_logger.error("Starting in the help mode or Incorrect script launch.")
        print("Starting in the help mode or Incorrect script launch.")
    finally:
        py_logger.info(f"Shutting down the script "
                       f" {script_name}... ")


if __name__ == '__main__':
    py_logger.info(f"Starting the script "
                   f" {script_name}... ")
    # main()
    con()
