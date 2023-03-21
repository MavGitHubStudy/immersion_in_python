from collections import namedtuple


Point = namedtuple('Point', 'x, y, z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(b)
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_namedtuple_04.py 
Point(x=6, y=3, z=0)

Process finished with exit code 0
"""
# 56:45
