"""
Задание №4

Напишите программу, которая вычисляет площадь круга
и длину окружности по введённому диаметру.

Диаметр не превышает 1000 y.e.

Точность вычислений должна составлять не менее 42 знаков
после запятой.
"""
# import decimal
# import math


# diameter = float(input("Enter diameter: "))
# length = 2 * math.pi * diameter / 2
# square = math.pi * (diameter / 2) ** 2
# print(f'{length = }, {square = }')

from decimal import getcontext, Decimal
from math import pi


MAX_VAL = 1000
TWO = 2
getcontext().prec = 42  # prec - количество знаков для вычислений
PI = Decimal(pi)

while True:
    diameter = Decimal(input("Enter diameter: "))
    if diameter < MAX_VAL:
        break

length = TWO * PI * (diameter / TWO)
square = PI * (diameter / TWO) ** TWO
print(f"{length = }, {square = }")
