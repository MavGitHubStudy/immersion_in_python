class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
print(f'{p1.power = }')
print(f'{p1.name = }, {p1.up = }, {p1.power = }')
"""
# super().__init__(*args, **kwargs)

p1.power = 'archery'
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_inheritance_02.py", line 38, in <module>
    print(f'{p1.name = }, {p1.up = }, {p1.power = }')
AttributeError: 'Hero' object has no attribute 'name'

Process finished with exit code 1

super().__init__(*args, **kwargs)

p1.power = 'archery'
p1.name = 'Сильвана', p1.up = 3, p1.power = 'archery'

Process finished with exit code 0

"""
