# 37:20
"""
Задание №3

Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш вбор.

У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п.,
на ваш выбор.

Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""
# 42:50


class Person:
    #46:03
    # def __init__(self, full_name, age):
    #     self.full_name = full_name
    #     self.__age = age
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


if __name__ == '__main__':
    p1 = Person('Иван', 'Иванов', 23)
    print(p1.get_age())
    p1.birthday()
    print(p1.get_age())
    print(p1.get_full_name())
    print(p1.name)
    print(p1._Person__age)  # Запрещённый способ !
    # Плохой стиль программирования.
"""
23
24
Иван Иванов
Иван

Process finished with exit code 0
"""
# 48:13
