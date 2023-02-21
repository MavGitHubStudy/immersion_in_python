import os
from pathlib import Path

# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir()  # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)
"""
Traceback (most recent call last):
  File "/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_04.py", line 4, in <module>
    os.makedirs('dir/other_dir/new_os_dir')
  File "/usr/lib/python3.10/os.py", line 225, in makedirs
    mkdir(name, mode)
FileExistsError: [Errno 17] File exists: 'dir/other_dir/new_os_dir'
"""
