from decimal import Decimal


class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'

    """
    In place методы
    
    Объект вызывает свой метод и изменяет своё значение
    """

    def __imod__(self, other):
        """Переопределение метода остатка от деления. Теперь этот метод
        не находит остаток от деления, а добавляет проценты, то есть теперь
        %= является добавление процента к существующему объекту."""
        self.value = self.value * Decimal(1 + other / 100)
        return self


def main():
    m = Money(100)
    print(m)
    m %= 50
    print(m)
    m %= 100
    print(m)


if __name__ == '__main__':
    main()
"""
Money(100.00)
Money(150.00)
Money(300.00)

Process finished with exit code 0
"""
# 01:08:25
