from collections import namedtuple
from datetime import datetime

# namedtuple - фабричная функция из модуля collections
User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(f'{type(User)}, {type(u_1)}')
# Обратите внимание!
# type(User) - это <class 'type'>, т.е. это класс, как если бы мы создавали
# класс через ключевое слово class,
# а тип объекта u_1 - это экземпляр класса User
# Всё то же самое, что и в ООП, но без явного ООП.
"""
home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_namedtuple_01.py 
User(first_name='Исаак', last_name='Ньютон', 
birthday=datetime.datetime(1643, 1, 4, 0, 0))
<class 'type'>, <class '__main__.User'>

Process finished with exit code 0
"""
# 52:00
