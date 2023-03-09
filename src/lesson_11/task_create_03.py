

class NamedInt(int):  # создаём класс NamedInt, дочерний для класса int
    def __new__(cls, value, name):  # value - число или строка, value -
        # дополнительный параметр, который мы используем
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance


print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
print('Создаём второй раз')
b = NamedInt(73, 'Лучше просто число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')
"""
Создаём первый раз
Создал класс <class '__main__.NamedInt'>
Создаём второй раз
Создал класс <class '__main__.NamedInt'>
a = 42	a.name = 'Главный ответ жизни, Вселенной и вообще'	type(a) = <class '__main__.NamedInt'>
b = 73	b.name = 'Лучше просто число'	type(b) = <class '__main__.NamedInt'>
c = 115	type(c) = <class 'int'>

Process finished with exit code 0
"""
#  13:43
