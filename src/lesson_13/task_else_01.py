MAX_COUNT = 5

result = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('Введите целое число: '))
        print('Успешно получили целое число')
    except ValueError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
    else:
        result = 100 / num
        break

print(f'{result = }')
"""
/home/.../.venv/bin/python /home/.../src/lesson_13/task_else_01.py 
Введите целое число: сорок два
Попытка 1 из 5 завершилась ошибкой invalid literal for int() with base 10:
 'сорок два'
Введите целое число: 42
Успешно получили целое число
result = 2.380952380952381

Process finished with exit code 0
"""
# 19:30