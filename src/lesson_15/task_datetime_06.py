from datetime import time, datetime

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
t = time(hour=2, minute=14, microsecond=24)

new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)
print(f'{new_dt}\n{one_more_hour}')
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_datetime_06.py 
2012-06-15 02:14:00.000024
03:14:00.000024

Process finished with exit code 0
"""
# 41:55
