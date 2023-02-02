"""
Задание №3

Напишите программу, которая получает целое число и возвращает его двоичное,
восьмеричное строковое представление.

Функции bin и oct используйте для проверки своего результата, а не для решения.

*Дополнительно

- Попробуйте избежать дублирования кода в преобразованных к разным системам
счисления

- Избегайте магических чисел

- Добавьте аннотацию типов там, где это возможно
"""
print(f'Вариант 1')
DATA = 'b', 'o', 'x'  # 2-я, 8-я, 16-я
num: int = int(input('Введите целое число num: '))
for char in DATA:
    print(format(num, char))
    # print(format(num, "o"))
# print(f"{bin(num)=}")
# print(f"{oct(num)=}")
print(f"Проверка: {bin(num) =}, {oct(num) = }")

# 01:00:00
print(f'Вариант 2')
ZERO = 0
BIN = 2
OCT = 8
HEX = 16


n: int = int(input('Enter integer num: '))

for num in BIN, OCT:
    work_num = n
    b: str = ""
    while work_num > ZERO:
        b = str(work_num % num) + b
        # b = tmp + b
        work_num = int(work_num / num)  # n // BIN
    print(b)
# 01:14:00
