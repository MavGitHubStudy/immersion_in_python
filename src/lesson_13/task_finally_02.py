file = open('text.txt', 'r', encoding='utf-8')
try:
    data = file.read().split()
    print(data[len(data)])
finally:
    print('Закрываю файл')
    file.close()
# 25:07
"""
Закрываю файл
Traceback (most recent call last):
  File "/home/.../src/lesson_13/task_finally_02.py", line 4, in <module>
    print(data[len(data)])
IndexError: list index out of range

Process finished with exit code 1
"""
