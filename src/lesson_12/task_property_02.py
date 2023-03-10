class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


user = User('Стивен', 'Спилберг')
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
user.full_name = 'Стивен Хокинг'  # AttributeError: can't set
# attribute 'full_name'
user.last_name = 'Хокинг'
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
"""
user.first_name = 'Стивен'
user.last_name = 'Спилберг'
user.full_name = 'Стивен Спилберг'
Traceback (most recent call last):
  File "/home/.../lesson_12/task_property_02.py", line 13, in <module>
    user.full_name = 'Стивен Хокинг'  # AttributeError: can't set
AttributeError: can't set attribute 'full_name'

Process finished with exit code 1
"""
# 39:41
