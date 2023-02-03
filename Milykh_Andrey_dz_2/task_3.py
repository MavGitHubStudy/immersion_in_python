"""
Напишите программу, которая принимает две строки вида “a/b” - дробь
с числителем и знаменателем. Программа должна возвращать сумму и произведение*
дробей. Для проверки своего кода используйте модуль fractions.
"""
import math
import fractions


DIVISION_SYMBOL = '/'

fraction1 = input('Введите первую дробь в формате "a/b": ')
fraction2 = input('Введите вторую дробь в формате "a/b": ')
numerator1 = ""
numerator2 = ""
denominator1 = ""
denominator2 = ""

i = 0
for fraction in fraction1, fraction2:
    # print(i, fraction)
    division_sign_found = False
    for char in fraction:
        if char != DIVISION_SYMBOL:
            if not division_sign_found:
                if i:
                    numerator2 += char
                else:
                    numerator1 += char
            else:
                if i:
                    denominator2 += char
                else:
                    denominator1 += char
        else:
            division_sign_found = True
    i += 1

if int(denominator1) == 0 or int(denominator2) == 0:
    print("Знаменатель дроби не может быть равен нулю!")
    exit()

amount_numerator = int(numerator1) * int(denominator2) + int(
    denominator1) * int(numerator2)
amount_denominator = int(denominator1) * int(denominator2)
greatest_common_divisor = math.gcd(amount_numerator, amount_denominator)
amount_numerator //= greatest_common_divisor
amount_denominator //= greatest_common_divisor
if abs(amount_numerator) == amount_denominator:
    print(f"Сумма двух дробей равна: {amount_numerator}")
else:
    print(
        f"Сумма двух дробей равна: {amount_numerator}/{amount_denominator}")

product_numerator = int(numerator1) * int(numerator2)
product_denominator = int(denominator1) * int(denominator2)
greatest_common_divisor = math.gcd(product_numerator, product_denominator)
# print(greatest_common_divisor)
product_numerator //= greatest_common_divisor
product_denominator //= greatest_common_divisor
if abs(product_numerator) == product_denominator:
    print(f"Произведение двух дробей равно: {product_numerator}")
else:
    print(
        f"Произведение двух дробей равно: {product_numerator}"
        f"/{product_denominator}"
    )

print("Проверка.")
f1 = fractions.Fraction(int(numerator1), int(denominator1))
f2 = fractions.Fraction(int(numerator2), int(denominator2))
print(f1 + f2)
print(f1 * f2)
