from task_error_01 import UserNameError, UserAgeError


class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
        if self.MAX_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError
        else:
            self.age = age


user = User('Яков', '-12')
# 51:45
"""
Traceback (most recent call last):
  File "/home/.../src/lesson_13/task_error_02.py", line 19, in <module>
    user = User('Яков', '-12')
  File "/home/.../src/lesson_13/task_error_02.py", line 12, in __init__
    raise UserNameError
task_error_01.UserNameError

Process finished with exit code 1
"""
