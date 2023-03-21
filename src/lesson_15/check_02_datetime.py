from datetime import datetime, timedelta

d = datetime.now()  # текущая дата
td = timedelta(hours=1)  # td - разница во времени, равная 1 часу
for i in range(24 * 7):
    if d.weekday() == 6:  # воскресенье
        break;
    else:
        d = d + td
print(i)  # сколько часов осталось с текущей момента времени до наступления
# воскресенья
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/check_02_datetime.py 
107

Process finished with exit code 0
"""
# 46:50
