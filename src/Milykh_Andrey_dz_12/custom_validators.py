from validator import Validator


class OneOf(Validator):
    """Класс OneOf проверяет, является ли значение одним из ограниченного
    набора параметров."""

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(
                f'Expected {value!r} to be one of {self.options!r}')


class Number(Validator):
    """Класс Number проверяет, является ли значение либо целым числом, либо
    числом с плавающей запятой. При необходимости он проверяет, находится ли
    значение между заданным минимумом или максимумом."""

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )


class String(Validator):
    """Класс String проверяет, что значение является строкой. При желании он
    проверяет заданную минимальную или максимальную длину. Он также может
    проверять определяемый пользователем предикат."""

    def __init__(self, minsize=None, maxsize=None,
                 predicate1=None, predicate2=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate1 = predicate1
        self.predicate2 = predicate2

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} bo be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate1 is not None and not self.predicate1(value):
            raise ValueError(
                f'Expected {self.predicate1} to be true for {value!r}'
            )
        if self.predicate2 is not None and not self.predicate2(value):
            raise ValueError(
                f'Expected {self.predicate2} to be true for {value!r}'
            )
