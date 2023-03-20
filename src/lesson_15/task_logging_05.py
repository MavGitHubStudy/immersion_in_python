import logging
from other import log_all

logging.basicConfig(filename='project.log', filemode='w',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/lesson_15/task_logging_05.py 

Process finished with exit code 0
"""
