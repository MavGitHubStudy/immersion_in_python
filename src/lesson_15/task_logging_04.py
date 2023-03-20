import logging
from other import log_all

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_logging_04.py 
WARNING:Основной файл проекта:Внимание! Используем вызов функции из другого модуля
WARNING:other:Внимание! Надвигается буря!
ERROR:other:Поймали ошибку. Дальше только неизвестность
CRITICAL:other:На этом всё

Process finished with exit code 0
"""
