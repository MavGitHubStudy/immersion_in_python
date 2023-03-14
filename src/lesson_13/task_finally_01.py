def get(text: str = None) -> int:
    num = None
    try:
        num = int(input(text))
    except ValueError as e:
        print(f'Ваш ввод привёл к ошибке ValueError: {e}')
    finally:
        return num if isinstance(num, int) else 1


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    try:
        print(f'100 / {number} = {100 / number}')
    except ZeroDivisionError as e:
        print(f'На ноль делить нельзя. Получим {e}')
# 23:25
"""
/home/.../.venv/bin/python /home/.../src/lesson_13/task_finally_01.py 
Введите целый делитель: сорок два
Ваш ввод привёл к ошибке ValueError: invalid literal for int() with base 10: 
'сорок два'
100 / 1 = 100.0

Process finished with exit code 0
"""
# 23:50
"""
/home/.../.venv/bin/python /home/.../src/lesson_13/task_finally_01.py 
Введите целый делитель: 0
На ноль делить нельзя. Получим division by zero

Process finished with exit code 0
"""
