from datetime import datetime, timedelta

date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')

birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_datetime_04.py 
delta = datetime.timedelta(days=1702)	-	1702 days, 0:00:00
new_date = datetime.datetime(1536, 12, 13, 6, 0)	-	1536-12-13 06:00:00

Process finished with exit code 0
"""
# 37:55
