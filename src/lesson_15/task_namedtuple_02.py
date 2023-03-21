from collections import namedtuple
from datetime import datetime

User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(u_1.first_name, u_1.birthday.year)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_namedtuple_02.py 
User(first_name='Исаак', last_name='Ньютон', birthday=datetime.datetime(1643, 1,
 4, 0, 0))
Исаак 1643

Process finished with exit code 0
"""
# 53:50
