class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1


fib = Fibonacci(20, 100)
for num in fib:  # TypeError: 'Fibonacci' object is not iterable
    print(num)
"""
Traceback (most recent call last):
  File "/home/.../lesson_12/task_iter_01.py", line 10, in <module>
    for num in fib:  # TypeError: 'Fibonacci' object is not iterable
TypeError: 'Fibonacci' object is not iterable

Process finished with exit code 1
"""
# 15:47
