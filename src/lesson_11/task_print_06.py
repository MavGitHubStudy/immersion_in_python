"""
Приоритет методов

Варианты срабатывания __str__ и __repr__

print(user)
__str__

print(f'{user}')
__str__

print(repr(user))
__repr__

print(f'{user = }')
__repr__

print(collections)
__repr__
"""
# 44:37


class User:

    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment \
            else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)
print(f'{user}')

print(repr(user))
print(f'{user = }')
"""
Перед нами Венкман с оборудованием: протонный ускоритель, ловушка. Количество 
жизней - 3
Перед нами Венкман с оборудованием: протонный ускоритель, ловушка. Количество 
жизней - 3
User(Венкман, ['протонный ускоритель', 'ловушка'])
user = User(Венкман, ['протонный ускоритель', 'ловушка'])

Process finished with exit code 0
"""
