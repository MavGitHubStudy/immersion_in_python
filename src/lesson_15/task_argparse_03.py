import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*',
                    help='press some numbers')
args = parser.parse_args()
print(f'Получили экземпляр Namespace: {args = }')
print(f'У Namespace работает точечная нотация: {args.numbers = }')
print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')

r"""
Примеры запуска в терминале:
python ./task_argparse_03.py 42 3.14 73
"""
# 1:19:24
"""
(.venv) novichkov@linuxint: ~/.../immersion_in_python/src/lesson_15: (main) $ 
python ./task_argparse_03.py 42 3.14 73
Получили экземпляр Namespace: args = Namespace(numbers=[42.0, 3.14, 73.0])
У Namespace работает точечная нотация: args.numbers = [42.0, 3.14, 73.0]
Объекты внутри могут быть любыми: args.numbers[1] = 3.14
(.venv) novichkov@linuxint: ~/work/gb/immersion_in_python/src/lesson_15: (main) $ 
"""

