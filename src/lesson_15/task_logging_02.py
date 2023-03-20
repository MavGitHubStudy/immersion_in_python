import logging

logging.basicConfig(level=logging.NOTSET)
logging.debug('Очень подробная отладочная информация. '
              'Заменяем множество "принтов"')
logging.info('Немного информации о работе кода')
logging.warning('Внимание! Надвигается буря!')
logging.error('Поймали ошибку. Дальше только неизвестность')
logging.critical('На этом всё')
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_logging_02.py 
DEBUG:root:Очень подробная отладочная информация. Заменяем множество "принтов"
INFO:root:Немного информации о работе кода
WARNING:root:Внимание! Надвигается буря!
ERROR:root:Поймали ошибку. Дальше только неизвестность
CRITICAL:root:На этом всё

Process finished with exit code 0
"""
# 15:40
