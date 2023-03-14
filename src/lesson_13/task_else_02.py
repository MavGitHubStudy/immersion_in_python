MAX_COUNT = 5

result = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('Введите целое число: '))
        print('Успешно получили целое число')
    except ValueError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
    else:
        try:
            result = 100 / num
        except ZeroDivisionError as e:
            result = float('inf')
        break

print(f'{result = }')
"""
Введите целое число: сорок два
Попытка 1 из 5 завершилась ошибкой invalid literal for int() with base 10:
 'сорок два'
Введите целое число: 0
Успешно получили целое число
result = inf

Process finished with exit code 0
"""
# 20:460
