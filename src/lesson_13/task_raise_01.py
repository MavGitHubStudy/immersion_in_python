def add_key(dct, key, value):
    if key in dct:
        raise KeyError(f'Перезаписывание существующего ключа запрещено. '
                       f'{dct[key] = }')
    dct[key] = value
    return dct


data = {'one': 1, 'two': 2}
print(add_key(data, 'three', 3))
print(add_key(data, 'three', 3))
# 38:49
"""
/home/.../python/.venv/bin/python /home/.../src/lesson_13/task_raise_01.py 
{'one': 1, 'two': 2, 'three': 3}
Traceback (most recent call last):
  File "/home/.../src/lesson_13/task_raise_01.py", line 11, in <module>
    print(add_key(data, 'three', 3))
  File "/home/.../src/lesson_13/task_raise_01.py", line 3, in add_key
    raise KeyError(f'Перезаписывание существующего ключа запрещено. '
KeyError: 'Перезаписывание существующего ключа запрещено. dct[key] = 3'

Process finished with exit code 1
"""
