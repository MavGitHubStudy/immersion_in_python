import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*',
                    help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

r"""
Примеры запуска в терминале:
python ./task_argparse_01.py 42 3.14 73
python ./task_argparse_01.py --help
python ./task_argparse_01.py Hello world!
"""
# 1:11:00
"""
Terminal:

(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
python ./task_argparse_01.py 42 3.14 73
В скрипт передано: Namespace(numbers=[42.0, 3.14, 73.0])
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $


(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
python ./task_argparse_01.py --help
usage: task_argparse_01.py [-h] [N ...]

My first argument parser

positional arguments:
  N           press some numbers

options:
  -h, --help  show this help message and exit
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
 
 
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
python ./task_argparse_01.py Hello world!
usage: task_argparse_01.py [-h] [N ...]
task_argparse_01.py: error: argument N: invalid float value: 'Hello'
(.venv) novichkov@linuxint: ~/work/gb/immersion_in_python/src/lesson_15: (main) $ 
"""
# 1:14:10
