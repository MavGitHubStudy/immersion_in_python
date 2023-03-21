from array import array

long_array = array('l', [-6000, 800, 100500])
long_array.append(2**64)  # OverflowError: Python int too large to convert to
# C long
# long_array.append(3.14)  # TypeError: 'float' object cannot be interpreted as
# an integer
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_array_03.py 
Traceback (most recent call last):
  File "/home/.../immersion_in_python/src/lesson_15/task_array_03.py", line 6, 
  in <module>
    long_array.append(3.14)  # TypeError: 'float' object cannot be interpreted as
TypeError: 'float' object cannot be interpreted as an integer

Traceback (most recent call last):
  File "/home/.../immersion_in_python/src/lesson_15/task_array_03.py", line 4, 
  in <module>
    long_array.append(2**64)  # OverflowError: Python int too large to convert to
OverflowError: Python int too large to convert to C long

Process finished with exit code 1
"""
# 1:03:40
