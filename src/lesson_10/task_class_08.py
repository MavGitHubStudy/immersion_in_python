class Person:
    max_up = 3

    def __init__(self):
        self.level = 1  # уровень
        self.health = 100  # здоровье


p1 = Person()
p2 = Person()
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health = }')
"""
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_classs_08.py", line 13, in <module>
    print(f'{Person.max_up = }, {Person.level = }, {Person.health = }')
AttributeError: type object 'Person' has no attribute 'level'

Process finished with exit code 1
"""
# print(f'{Person.max_up = }, {Person.health = }')
"""
raceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_classs_08.py", line 22, in <module>
    print(f'{Person.max_up = }, {Person.health = }')
AttributeError: type object 'Person' has no attribute 'health'
"""

Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')
"""
p1.max_up = 3, p1.level = 1, p1.health = 100
p2.max_up = 3, p2.level = 1, p2.health = 100
Person.level = 100, p1.level = 1, p2.level = 1

Process finished with exit code 0
"""
