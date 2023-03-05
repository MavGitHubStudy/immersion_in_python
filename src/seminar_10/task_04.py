# 51:50
"""
Задание №4

Создайте класс Сотрудник.

Воспользуйтесь классом Человек из прошлого задания.

У сотрудника должен быть:

- шестизначный идентификационный номер

- уровень доступа вычисляемый, как остаток от деления
  суммы цифр id на семь.
"""
from random import randint


class Person:
    def __init__(self, name, surname, age, hobby=None):
        self.name = name
        self.surname = surname
        self.__age = age
        self.hobby = hobby

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        return self.__age


class Employee(Person):
    _DIV = 7
    COUNT_NUM = 6

    def __init__(self, idx, *args):
        min_num = 10 ** (self.COUNT_NUM - 1)
        max_num = 10 ** self.COUNT_NUM - 1
        if idx < min_num or idx > max_num:
            self.idx = randint(min_num, max_num)
        else:
            self.idx = idx
        self.lvl = sum(int(i) for i in str(self.idx)) % self._DIV
        super().__init__(*args)  # 59:30


if __name__ == '__main__':
    emp = Employee(123457, 'Иван', 'Иванов', 23)  # 1:01:10
    print(emp.name)
    print(emp.get_age())
    print(emp.idx)
    # print(emp.id_num)  # 1:04:23
    print(emp.lvl)
"""
123456, 'Иван', 'Иванов', 23
____________________________
Иван
23
123456
0

123457, 'Иван', 'Иванов', 23
____________________________
Иван
23
123456
1

Process finished with exit code 0
"""
# Таким образом, уровень доступа меняется от 0 до 6 по кругу
