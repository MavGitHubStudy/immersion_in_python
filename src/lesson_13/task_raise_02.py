class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Длина имени должна быть между 6 и 30 '
                             f'символами. {len(name) = }')
        if not isinstance(age, (int, float)):
            raise  TypeError(f'Возраст должен быть числом. Используйте int '
                             f'или float. {type(age) = }')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным. {age = }')
        else:
            self.age = age


# user = User('Яков', '-12')
# 41:18
"""
/home/.../.venv/bin/python /home/.../src/lesson_13/task_raise_02.py 
Traceback (most recent call last):
  File "/home/.../src/lesson_13/task_raise_02.py", line 17, in <module>
    user = User('Яков', '-12')
  File "/home/.../src/lesson_13/task_raise_02.py", line 6, in __init__
    raise ValueError(f'Длина имени должна быть между 6 и 30 '
ValueError: Длина имени должна быть между 6 и 30 символами. len(name) = 4

Process finished with exit code 1
"""
# 41:47 попробуем задать более длинное имя
# user = User('ЯквоДлинный', '-12')
"""
Traceback (most recent call last):
  File "/home/.../src/lesson_13/task_raise_02.py", line 31, in <module>
    user = User('ЯквоДлинный', '-12')
  File "/home/.../src/lesson_13/task_raise_02.py", line 9, in __init__
    raise  TypeError(f'Возраст должен быть числом. Используйте int '
TypeError: Возраст должен быть числом. Используйте int или float. 
type(age) = <class 'str'>

Process finished with exit code 1
"""
# 42:30
# user = User('ЯквоДлинный', -12)
"""
Traceback (most recent call last):
  File "/home/.../src/lesson_13/task_raise_02.py", line 44, in <module>
    user = User('ЯквоДлинный', -12)
  File "/home/.../src/lesson_13/task_raise_02.py", line 12, in __init__
    raise ValueError(f'Возраст должен быть положительным. {age = }')
ValueError: Возраст должен быть положительным. age = -12

Process finished with exit code 1
"""
# 42:50 отлично, вводим финальные правки
user = User('ЯквоДлинный', 12)
"""
/home/.../.venv/bin/python /home/.../src/lesson_13/task_raise_02.py 

Process finished with exit code 0
"""
