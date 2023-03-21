import time
from collections import namedtuple
from datetime import datetime

SECONDS = 7
# Дефолтные значения формируются один раз при создании класса,
# а не его экземпляра!
User = namedtuple('User', ['first_name', 'last_name', 'birthday'],
                  defaults=['Иванов', datetime.now()])
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
print(f'Пауза в {SECONDS} секунд...')
time.sleep(SECONDS)
u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_namedtuple_03.py 
Иванов, 14:56:52
Пауза в 7 секунд...
Галилео, 14:56:52

Process finished with exit code 0
"""
# 54:20
