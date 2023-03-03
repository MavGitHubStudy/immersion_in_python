class User:

    def __init__(self, name, phone, password):
        self.__name__ = name  # магическая переменная !!!
        self._phone = phone
        self.__password = password


u1 = User('One', '123-45-67', 'qwerty')

print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password = }')
"""
u1.__name__ = 'One', u1._phone = '123-45-67', u1._User__password = 'qwerty'

Process finished with exit code 0
"""
