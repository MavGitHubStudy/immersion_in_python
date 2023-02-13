a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}')

a, b, c = {"один", "два", "три", "четыре", "пять"}
print(f'{a=} {b=} {c=}')
"""
a='один' b='два' c='три'
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_05/task_oneline_03.py", line 5, in <module>
    a, b, c  = {"один", "два", "три", "четыре", "пять"}
ValueError: too many values to unpack (expected 3)
"""
