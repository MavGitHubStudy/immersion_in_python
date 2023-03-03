path_1 = '/home/user'
path_2 = '/my_project/workdir'
result = path_1/ path_2  # TypeError: unsupported operated operand type(s)
# for /: 'str' and 'str'
"""
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_10/task_polymorphism_02.py", line 3, in <module>
    result = path_1/ path_2  # TypeError: unsupported operated operand type(s)
TypeError: unsupported operand type(s) for /: 'str' and 'str'

Process finished with exit code 1
"""
