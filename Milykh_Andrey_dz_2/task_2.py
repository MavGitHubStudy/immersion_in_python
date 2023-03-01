"""
Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте
для проверки своего результата.
"""
ZERO = 0
HEX = 16


num: int = int(input("Введите целое число: "))
print(f"{num}, {type(num)}")
work_num: int = num
result: str = ""
prefix: str = ""

if num < ZERO:
    prefix = "-0x"
    work_num = -num
elif num == ZERO:
    prefix = "0x"
    result = "0"
else:
    prefix = "0x"
    work_num = num

while work_num > ZERO:
    remainder = work_num % HEX
    if remainder == 10:
        result = 'a' + result
    elif remainder == 11:
        result = 'b' + result
    elif remainder == 12:
        result = 'c' + result
    elif remainder == 13:
        result = 'd' + result
    elif remainder == 14:
        result = 'e' + result
    elif remainder == 15:
        result = 'f' + result
    else:
        result = str(remainder) + result

    work_num //= HEX

result = prefix + result
print(f"{result}, {type(result)}")

print(f"Проверка: {num = }, {hex(num) = }, {type(hex(num))}")
