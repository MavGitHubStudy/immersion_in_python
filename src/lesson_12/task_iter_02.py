class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self


fib = Fibonacci(20, 100)
for num in fib:  # TypeError: iter() returned non-iterator of type 'Fibonacci'
    print(num)
"""
Traceback (most recent call last):
  File "/home/.../lesson_12/task_iter_02.py", line 13, in <module>
    for num in fib:  # TypeError: 'Fibonacci' object is not iterable
TypeError: iter() returned non-iterator of type 'Fibonacci'

Process finished with exit code 1
"""
# 16:41
