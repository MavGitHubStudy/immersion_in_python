import argparse


def quadratic_equations(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float, nargs=3,
                        help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))

# 1:23:00
r"""
Примеры запуска в терминале:


(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
python ./task_argparse_04.py 2 -12 10
(5.0, 1.0)
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 


(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
python ./task_argparse_04.py -h
usage: task_argparse_04.py [-h] a b c a b c a b c

Solving quadratic equations

positional arguments:
  a b c       enter a b c separated by a space

options:
  -h, --help  show this help message and exit
(.venv) novichkov@linuxint: ~/work/gb/immersion_in_python/src/lesson_15: (main) $ 
"""
