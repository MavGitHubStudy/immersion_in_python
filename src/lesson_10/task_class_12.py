class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity
    # other - это другой экземпляр такого же класса


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = } {p3.health = }')

p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
"""
p1.health = 100, p2.health = 100 p3.health = 100
p1.health = 110, p2.health = 90, p3.health = 100

Process finished with exit code 0
"""
