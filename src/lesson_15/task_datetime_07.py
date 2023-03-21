from datetime import datetime

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)

print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W '
                  'неделя и %j день года.'))
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_datetime_07.py 
2007-06-15 02:14:00.000024
1181859240.000024
2007-06-15T02:14:00.000024
4
Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.

Process finished with exit code 0
"""
# 42:35
