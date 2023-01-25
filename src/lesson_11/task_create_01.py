

class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        # принтим только в учебных целях, а не для реальнхы задач
        print(f'Создал {self} со свойствами:\n'
              f'{self.name = },\t{self.equipment = },\t'
              f'{self.life = }')


print('Создаём первый раз')
u_1 = User('Спенглер')
print('Создаём второй раз')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
print('Создаём третий раз')
u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэц')
"""
Создаём первый раз
Создал <__main__.User object at 0x7fbe8b0ab370> со свойствами:
self.name = 'Спенглер',	self.equipment = [],	self.life = 3
Создаём второй раз
Создал <__main__.User object at 0x7fbe8b0ab400> со свойствами:
self.name = 'Венкман',	self.equipment = ['протонный ускоритель', 'ловушка'],	self.life = 3
Создаём третий раз
Создал <__main__.User object at 0x7fbe8b06d660> со свойствами:
self.name = 'Стэц',	self.equipment = ['ловушка', 'прибор ночного видения'],	self.life = 3

Process finished with exit code 0
"""
# 08:43
