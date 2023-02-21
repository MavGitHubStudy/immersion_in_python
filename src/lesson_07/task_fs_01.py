import os  # старый модуль
from pathlib import Path  # v.3.4 появился в этой версии
# импортируется класс Path

print(os.getcwd())
print(Path.cwd())
"""
/home/novichkov/work/gb/immersion_in_python/src/lesson_07
/home/novichkov/work/gb/immersion_in_python/src/lesson_07

Process finished with exit code 0
"""