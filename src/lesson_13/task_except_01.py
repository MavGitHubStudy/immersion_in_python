def get(text: str = None) -> int:
    data = input(text)
    try:
        num = int(data)
    except ValueError as e:
        print(f'Ваш ввод привёл к ошибке ValueError: {e}')
        num = 1
        print(f'Будем считать результатом ввода число {num}')
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
"""
Введите целый делитель: сорок два
Ваш ввод привёл к ошибке ValueError: invalid literal for int() with 
base 10: 'сорок два'
Будем считать результатом ввода число 1
100 / 1 = 100.0

Process finished with exit code 0
"""
