"""
Задание №6

- Изменяем класс прямоугольника.
- Заменяем пару декораторов проверяющих длину и ширину
  на дескриптор с валидацией размеров.

Задание №5

- Доработаем прямоугольник и добавим экономию памяти
  для сохранения свойств экземпляра без словаря __dict__.
"""


# 1:43:51 - 1:50:45 - 1:51:54
class TrueValue:
    """Верхний дескриптор на контроль значения"""

    def __init__(self, limit):
        self.limit = limit

    def __set_name__(self, owner, name):
        self.param_name = '_' + name  # без подчёркивания возникал конфликт
        # имён!

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.is_true(value)
        setattr(instance, self.param_name, value)

    def is_true(self, value):
        if value <= self.limit:
            raise ValueError(f'Сторона должна быть > {self.limit}')


class Rectangle:
    # __slots__ = ('_length', '_width')
    length = TrueValue(10)  # 1:57:52 - задаём верхний предел вместо 0 - 10!
    width = TrueValue(10)

    def __init__(self, length, width=None):
        self._length = length
        self._width = width if width is None else length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    # @property
    # def length(self):
    #     return self._length
    #
    # @length.setter
    # def length(self, length_value):
    #     if length_value > 0:
    #         self._length = length_value
    #     else:
    #         raise ValueError(f'Длина должна быть больше нуля. '
    #                          f'Передано{length_value}')
    #
    # @property
    # def width(self):
    #     return self._width
    #
    # @width.setter
    # def width(self, width_value):
    #     if width_value > 0:
    #         self._width = width_value
    #     else:
    #         raise ValueError(f'Ширина должна быть больше нуля. '
    #                          f'Передано{width_value}')


def main():
    r = Rectangle(2, 2)
    print(r.width, r.length)
    print(r.perimeter())
    r.length = 15  # 5 вызовет ошибку !
    r.width = 12
    print(r.width, r.length)
    print(r.perimeter())
    # r.new_value = 42  # финт на Python
    # print(r.__dict__)
    # print(r.__slots__)


if __name__ == '__main__':
    main()
# Первоначальный вызов 1:53:00 не ругается!
"""
/home/.../.venv/bin/python /home/.../src/seminar_12/task_04.py 
2 2
8
12 5
34

Process finished with exit code 0
"""
# 12:32:55
