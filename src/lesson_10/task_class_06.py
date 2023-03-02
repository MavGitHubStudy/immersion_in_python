class Person:
    max_up = 3


p1 = Person()
p2 = Person()
Person.level = 1
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

p1.health = 100  # обособленное значение
# print(f'{Person.health = }, {p1.health = }, {p2.health = }')
"""
Person.level = 1, p1.level = 1, p2.level = 1
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_class_06.py", line 11, in <module>
    print(f'{Person.health = }, {p1.health = }, {p2.health = }')
AttributeError: type object 'Person' has no attribute 'health'

Process finished with exit code 1
"""
# print(f'{p1.health = }, {p2.health = }')
"""
Person.level = 1, p1.level = 1, p2.level = 1
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_class_06.py", line 20, in <module>
    print(f'{p1.health = }, {p2.health = }')
AttributeError: 'Person' object has no attribute 'health'
"""
print(f'{p1.health = }')
"""
Person.level = 1, p1.level = 1, p2.level = 1
p1.health = 100
"""
