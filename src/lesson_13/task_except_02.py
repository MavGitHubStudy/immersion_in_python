def get(text: str = None) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
"""
к ошибке ValueError: invalid literal for int() with base 10: 'сорок два'
Попробуйте снова
Введите целый делитель: пять
Ваш ввод привёл к ошибке ValueError: invalid literal for int() with base 10: 'пять'
Попробуйте снова
Введите целый делитель: 3.14
Ваш ввод привёл к ошибке ValueError: invalid literal for int() with base 10: '3.14'
Попробуйте снова
Введите целый делитель: 42
100 / 42 = 2.380952380952381

Process finished with exit code 0
"""
# 12:07
