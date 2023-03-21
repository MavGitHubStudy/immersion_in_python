from array import array

long_array = array('l', [-6000, 800, 100500])
long_array.append(42)
print(long_array)
print(long_array[2])
print(long_array.pop())
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_array_02.py 
array('l', [-6000, 800, 100500, 42])
100500
42

Process finished with exit code 0

"""
# 1:02:20
