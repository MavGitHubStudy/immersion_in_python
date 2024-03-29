import argparse

parser = argparse.ArgumentParser(prog='average',
                                 description='My first argument parser',
                                 epilog='Returns the arithmetic mean'
                                 )
parser.add_argument('numbers', metavar='N', type=float, nargs='*',
                    help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

r"""
Примеры запуска в терминале:
python ./task_argparse_02.py --help
"""
# 1:16:20
"""
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
python ./task_argparse_02.py --help
usage: average [-h] [N ...]

My first argument parser

positional arguments:
  N           press some numbers

options:
  -h, --help  show this help message and exit

Returns the arithmetic mean
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
"""
