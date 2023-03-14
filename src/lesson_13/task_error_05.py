from task_error_04 import UserNameError, UserAgeError


class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
        if self.MAX_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name,          # добавили name -
                                self.MIN_LEN,  # что вызвало
                                self.MAX_LEN)  # ошибку
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)  # добавили age - что вызвало ошибку
        else:
            self.age = age


user = User('Яков', '-12')
# 55:35
"""
Traceback (most recent call last):
  File "/home/.../src/lesson_13/task_error_05.py", line 21, in <module>
    user = User('Яков', '-12')
  File "/home/.../src/lesson_13/task_error_05.py", line 12, in __init__
    raise UserNameError(name,          # добавили name -
task_error_04.UserNameError: Имя пользователя Яков содержит 4 символа(ов).
Это меньше нижней границы. Попадите в диапазон (6, 30).

Process finished with exit code 1
"""
