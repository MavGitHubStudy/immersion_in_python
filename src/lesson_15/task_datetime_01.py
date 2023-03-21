from datetime import time, date, datetime

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, second=0,
              microsecond=24)
print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{dt = }\t-\t{dt}')
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_datetime_01.py 
d = datetime.date(2007, 6, 15)	-	2007-06-15
t = datetime.time(2, 14, 0, 24)	-	02:14:00.000024
dt = datetime.datetime(2007, 6, 15, 2, 14, 0, 24)	-	2007-06-15 02:14:00.000024

Process finished with exit code 0
"""
# 32:15
