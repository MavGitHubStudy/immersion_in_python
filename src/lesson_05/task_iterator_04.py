"""next(iterator[, default"""

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
# print(next(list_iter))  # StopIteration
"""
raceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_05/task_iterator_04.py", line 9, in <module>
    print(next(list_iter))  # StopIteration
StopIteration

Process finished with exit code 1
"""
print(next(list_iter, 42))
"""
2
4
6
8
42
"""
