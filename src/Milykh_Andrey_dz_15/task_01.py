""" task_01.py """
import logging
from task_01_ex import RectangleLengthException, RectangleWidthException

"""
- Напишите классы исключения с выводом подробной 
  информации.
  
- Поднимайте исключения внутри основного кода. Например, 
  нельзя создавать прямоугольник со сторонами отрицательной
  длины.
"""

FORMAT = '{levelname} - {asctime} - {funcName} - {lineno} - {msg}'
# FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
# FORMAT = '{levelname} - {asctime} - {msg}'
# logging.basicConfig(level=logging.INFO,
#                     # filename='logs_3.log',
#                     encoding='utf-8',
#                     format=FORMAT,
#                     style='{')

# получение пользовательского логгера и установка уровня логирования
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("{name} - {levelname} - {asctime} - {msg}",
                                 style='{')

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)

py_logger.info(f"Testing the custom logger for module {__name__}... ")


class Rectangle:

    def __init__(self, length, width=None):
        if self._check_size(length):
            self._length = length
            py_logger.info(f"rectangle {self.__name__} length: {length}")
        else:
            raise RectangleLengthException(length)
            py_logger.info(f"rectangle invalid length: {length}")

        if width is None:
            self._width = self.length
            py_logger.info(f"rectangle width: {length}")
        else:
            if self._check_size(width):
                self._width = width
                py_logger.info(f"rectangle width: {width}")
            else:
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
            raise RectangleLengthException(length_value)
        self._length = length_value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_value):
        if not self._check_size(width_value):
            raise RectangleWidthException(width_value)
        self._width = width_value


def main():
    try:
        r1 = Rectangle(2, 2)
        # r1 = Rectangle(2)
        print(r1.width, r1.length)
        print(r1.perimeter())
        r1.length = 5
        r1.width = 6
        print(r1.width, r1.length)
        print(r1.perimeter())
        r2 = Rectangle(-3)
        print(r2.perimeter())
    except (RectangleLengthException, RectangleWidthException) as e:
        # print(e)
        logging.exception("invalid sides of the rectangle")


if __name__ == '__main__':
    main()
