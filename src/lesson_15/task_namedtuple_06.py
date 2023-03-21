from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
}
print(d)

mut_point = Point(2, [3, 4, 5], 6)
print(mut_point)
d.update({mut_point: 'bad_point'})  # TypeError: unhashable type: 'list'
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_namedtuple_06.py 
{Point(x=2, y=3, z=4): 'first', Point(x=10, y=-100, z=-500): 'second', Point(x=3, y=7, z=11): 'last'}
Point(x=2, y=[3, 4, 5], z=6)
Traceback (most recent call last):
  File "/home/.../immersion_in_python/src/lesson_15/task_namedtuple_06.py", 
  line 13, in <module>
    d.update({mut_point: 'bad_point'})  # TypeError: unhashable type: 'list'
TypeError: unhashable type: 'list'

Process finished with exit code 1
"""
# 59:00
