import logging
from other import log_all

FORMAT = '{levelname:<8} {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger('main')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
"""
/home/novichkov/work/gb/immersion_in_python/.venv/bin/python /home/novichkov/work/gb/immersion_in_python/src/lesson_15/task_logging_06.py 
WARNING  2023-03-21 00:35:14,150. В модуле "main" в строке 009 функция "<module>()" в 1679348114.1505167 секунд записала сообщение: Внимание! Используем вызов функции из другого модуля
INFO     2023-03-21 00:35:14,150. В модуле "other" в строке 009 функция "log_all()" в 1679348114.1506927 секунд записала сообщение: Немного информации о работе кода
WARNING  2023-03-21 00:35:14,150. В модуле "other" в строке 010 функция "log_all()" в 1679348114.1507714 секунд записала сообщение: Внимание! Надвигается буря!
ERROR    2023-03-21 00:35:14,150. В модуле "other" в строке 011 функция "log_all()" в 1679348114.1508505 секунд записала сообщение: Поймали ошибку. Дальше только неизвестность
CRITICAL 2023-03-21 00:35:14,150. В модуле "other" в строке 012 функция "log_all()" в 1679348114.150926 секунд записала сообщение: На этом всё

Process finished with exit code 0

"""
# 25:26
