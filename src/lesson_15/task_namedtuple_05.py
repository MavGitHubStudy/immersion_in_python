from collections import namedtuple


Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
data = [Point(2, 202, 4), Point(10, -100, -500), Point(3, 7, 11), Point(2, 3,
                                                                        1)]
print(sorted(data))
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_namedtuple_05.py 
[Point(x=2, y=3, z=1), Point(x=2, y=202, z=4), Point(x=3, y=7, z=11), 
Point(x=10, y=-100, z=-500)]

Process finished with exit code 0
"""
# 57:30
