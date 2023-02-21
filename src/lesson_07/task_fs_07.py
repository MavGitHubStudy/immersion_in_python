import os
from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')
"""
file_1 = '/home/novichkov/work/gb/immersion_in_python/src/lesson_07/dir/new_file.txt'
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/dir/new_file.txt
file_2 = PosixPath('/home/novichkov/work/gb/immersion_in_python/src/lesson_07/dir/new_file.txt')
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/dir/new_file.txt

Process finished with exit code 0
"""