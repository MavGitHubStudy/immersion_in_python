"""
Задание №5

Напишите программу, которая решает квадратные уравнения
даже если дискриминант отрицательный.

Используйте комплексные числа для извлечения квадратного
корня.

Подсказки:
d = b**2-4*a*c
(-b+-d**0.5)/(2*a)
"""
# 01:33:30
import cmath


"""
import math


# res = math.sqrt(-1)
# print(res)

# res = -1 ** 0.5
# -1.0

res = -10 ** 0.5
# -3.1622776601683795
print(res)
"""

TWO = 2
FOUR = 4

a = complex(input("a = "))
b = complex(input("b = "))
c = complex(input("c = "))
if a == 0:
    # print('Это не квадратное уравнение!')
    exit('Это не квадратное уравнение!')
d = b ** TWO - FOUR * a * c
print(f'{d = }')
x1 = (-b + cmath.sqrt(d)) / (TWO * a)
x2 = (-b - cmath.sqrt(d)) / (TWO * a)
print(f"{x1 = }")
print(f"{x2 = }")
