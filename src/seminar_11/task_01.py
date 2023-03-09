"""
Задание №1

Создайте класс Моя Строка, где:
- будут доступны все возможности str
- дополнительно хранятся имя автора строки и время создания
  (time.time)
"""
from time import time


class MyStr(str):
    """Здесь str - фабричная функция, которая возвращает экземпляр
    соответствующего класса"""

    def __new__(cls, value, author):
        """Работает в момент создания класса, в отличие от init, который
        работает в момент создания экземпляра класса"""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance

    # def __str__(self):
    #     return f'Строка {self} написана автором {self.author}'


def main():
    s = MyStr('Hello world!', 'prepod')
    print(s)
    print(s.author)
    print(s.time)

    s2 = MyStr('Hi', 'student')
    print(s2.upper())
    print(s2.author)
    print(s2.time)


if __name__ == '__main__':
    main()
"""
Hello world!
prepod
1678311713.4834607
HI
student
1678311713.48351

Process finished with exit code 0
"""
# 22:50
