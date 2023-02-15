"""
Задание №4

Создайте генератор чётных чисел от нуля до 100.

Из последовательности исключите числа, сумма цифр
которых равна 8.

Решение в одну строку.
"""
# 46:50
# Dmitry Voytic
nums = [i for i in range(0, 101) if i % 2 == 0 and (i % 10 + i // 10 != 8)]
# print(nums)
print(*nums)

print('*' * 80)

# Khalil Batkaev
result = (num for num in range(0, 100 + 1, 2) if num // 10 + num % 10 != 8)
print(*result)
