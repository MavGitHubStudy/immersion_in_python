import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

logger.debug('Очень подробная отладочная информация. '
             'Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_logging_02.py 
DEBUG:__main__:Очень подробная отладочная информация. Заменяем множество "принтов"
INFO:__main__:Немного информации о работе кода
WARNING:__main__:Внимание! Надвигается буря!
ERROR:__main__:Поймали ошибку. Дальше только неизвестность
CRITICAL:__main__:На этом всё

Process finished with exit code 0
"""
# 17:35
