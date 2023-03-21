from datetime import timedelta

delta = timedelta(weeks=53, days=500, hours=73, minutes=101, seconds=303,
                  milliseconds=67890, microseconds=1234567)
neg_delta = timedelta(days=-3, minutes=-42)
print(f'{delta = }\t-\t{delta}')
print(f'{neg_delta = }\t-\t{neg_delta}')
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_datetime_03.py 
delta = datetime.timedelta(days=874, seconds=10032, microseconds=124567)	-	
874 days,
 2:47:12.124567
neg_delta = datetime.timedelta(days=-4, seconds=83880)	-	-4 days, 23:18:00

Process finished with exit code 0
"""
# 36:05
