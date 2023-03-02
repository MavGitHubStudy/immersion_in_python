class Person: # 28:50
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')
"""
p1.name = 'Сильвана', p1.race = 'Эльф'
p2.name = 'Иван', p2.race = 'Человек'
p3.name = 'Грогу', p3.race = 'unknown'

Process finished with exit code 0
"""
