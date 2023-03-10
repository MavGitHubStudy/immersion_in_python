class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


user = User('Стивен')
print(f'{user.name = }')
user.name = 'Славик'  # AttributeError: can't set attribute 'name'
"""
user.name = 'Стивен'
Traceback (most recent call last):
  File "/home/.../lesson_12/task_property_01.py", line 12, in <module>
    user.name = 'Славик'  # AttributeError: can't set attribute 'name'
AttributeError: can't set attribute 'name'

Process finished with exit code 1
"""
# 37:47
