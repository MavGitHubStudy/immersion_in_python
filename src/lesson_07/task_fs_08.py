import os
from pathlib import Path

print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
"""
['new_data.txt', 'task_files_21.py', 'task_files_08.py', 'check_01_files.py', 'task_files_12.py', 'task_files_17.py', 'task_fs_02.py', 'bin_data', 'task_fs_06.py', 'task_files_19.py', 'task_files_11.py', 'task_fs_07.py', 'task_files_10.py', 'task_files_15.py', 'task_files_07.py', 'task_files_23.py', 'test_data.txt', 'task_fs_04.py', 'new_path_dir', 'task_files_01.py', 'task_files_25.py', 'data.txt', 'task_files_06.py', 'task_files_22.py', 'task_fs_05.py', 'task_fs_03.py', 'task_files_04.py', 'data.bin', 'task_files_20.py', 'task_files_13.py', 'task_files_09.py', 'new_os_dir', 'task_files_05.py', 'task_files_18.py', 'task_files_24.py', 'task_files_14.py', 'dir', 'task_files_16.py', 'text_data.txt', 'task_fs_08.py', 'task_files_03.py', 'task_fs_01.py']
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/new_data.txt
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_21.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_08.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/check_01_files.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_12.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_17.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_02.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/bin_data
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_06.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_19.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_11.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_07.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_10.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_15.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_07.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_23.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/test_data.txt
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_04.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/new_path_dir
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_01.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_25.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/data.txt
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_06.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_22.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_05.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_03.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_04.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/data.bin
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_20.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_13.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_09.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/new_os_dir
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_05.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_18.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_24.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_14.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/dir
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_16.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/text_data.txt
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_08.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_files_03.py
/home/novichkov/work/gb/immersion_in_python/src/lesson_07/task_fs_01.py

Process finished with exit code 0
"""
