# 1:04:30


def factorial(n):
    number = 1
    for i_ in range(1, n + 1):
        number *= i_
        yield number


my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))  # StopIteration
"""
<generator object factorial at 0x7efeacd309e0>
1
2
6
24
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_05/task_yield_03.py", line 17, in <module>
    print(next(my_iter))  # StopIteration
StopIteration

Process finished with exit code 1
"""
