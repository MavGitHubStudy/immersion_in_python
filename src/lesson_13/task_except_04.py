def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            div = 100 / num
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
        except ZeroDivisionError as e:
            div = float('inf')  # inf - бесконечность
            break
    return num, div


if __name__ == '__main__':
    n, d = hundred_div_num('Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')
"""
Введите целый делитель: сорок два
Ваш ввод привёл к ошибке ValueError: invalid literal for int() 
with base 10: 'сорок два'
Попробуйте снова
Введите целый делитель: 0
Результат операции: "100 / 0 = inf"

Process finished with exit code 0
"""
# 16:36 - 16:48
