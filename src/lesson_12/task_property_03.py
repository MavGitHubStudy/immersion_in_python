class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: ',
                             f'{self._age}')


user = User('Стивен', 'Спилберг')
user.age = 75
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошёл один год.')
user.age = 76
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошло несколько лет. Изобретена технология омоложения. '
      'Но возраст она не уменьшает.')
user.age = 25  # ValueError: Новый возраст должен быть больше текущего: 76
"""
Меня зовут Стивен Спилберг и мне 75 лет.
Прошёл один год.
Меня зовут Стивен Спилберг и мне 76 лет.
Прошло несколько лет. Изобретена технология омоложения. Но возраст она 
не уменьшает.
Traceback (most recent call last):
  File "/home/.../lesson_12/task_property_03.py", line 32, in <module>
    user.age = 25  # ValueError: Новый возраст должен быть больше текущего: 76
  File "/home/.../lesson_12/task_property_03.py", line 20, in age
    raise ValueError(f'Новый возраст должен быть больше текущего: ',
ValueError: ('Новый возраст должен быть больше текущего: ', '76')

Process finished with exit code 1
"""
# 43:17
