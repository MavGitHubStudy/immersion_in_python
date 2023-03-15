class RectangleException(Exception):
    pass


class RectangleLengthException(RectangleException):
    def __init__(self, length):
        self.length = length if length else None

    def __str__(self):
        return (f'Недопустимое значение длины: {self.length}. '
                f'Длина должна быть больше нуля.')


class RectangleWidthException(RectangleException):
    def __init__(self, width):
        self.width = width if width else None

    def __str__(self):
        return (f'Недопустимое значение ширины: {self.width}. '
                f'Ширина должна быть больше нуля.')

