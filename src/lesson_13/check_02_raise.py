def func(a, b, c):
    if a < b < c:
        raise ValueError('Не перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Это имя занято!')
    elif max(a, b, c, key=len) < 5:  # число не позволяет найти свою длину
        raise MemoryError('Слишком глуп!')
    else:
        raise RuntimeError('Что-то не так!!!')


func(11, 3, 3)  # 1 Что-то не так
func(3, 2, 7)  # 2 Что-то не так
func(73, -40, 9)  # 3  Это имя занято Слишком глуп!
func(10, 20, 30)  # 4  Не перемешано!
# 44:50
"""
/home/.../.venv/bin/python /home/.../src/lesson_13/check_02_raise.py 
Traceback (most recent call last):
  File "/home/.../src/lesson_13/check_02_raise.py", line 12, in <module>
    func(11, 3, 3)  # 1 Что-то не так
  File "/home/.../src/lesson_13/check_02_raise.py", line 6, in func
    elif max(a, b, c, key=len) < 5:  # число не позволяет найти свою длину
TypeError: object of type 'int' has no len()

Process finished with exit code 1
"""

