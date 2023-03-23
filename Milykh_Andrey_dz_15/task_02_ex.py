class TriangleException(Exception):
    pass


class TriangleSideException(TriangleException):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return (f'Недопустимое значение стороны треугольника: {self.side}. '
                f'Сторона треугольника должна быть больше нуля.')


class TriangleExistException(TriangleException):
    def __init__(self, flag):
        self.flag = flag

    def __str__(self):
        return f'Треугольника нет. {self.flag} >= суммы других.'
