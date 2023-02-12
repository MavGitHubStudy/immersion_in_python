"""
Задание №6

Функция получает на вход список чисел и два индекса.

Вернуть сумму чисел между переданными индексами.

Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""
# 01:35:10 - 01:42:00


def sum_counter(lst: list[int], idx1: int, idx2: int) -> int:
    if idx2 > idx1:
        return sum(lst[idx1:idx2])


res = sum_counter([1, 2, 3, 4, 5], 1, 3)
print(res)
"""
5
"""
res = sum_counter([1, 2, 3, 4, 5], -1, 42)
print(res)
"""
5  # почему ?
"""
res = sum_counter([1, 2, 3, 4, 5], -10, 42)
print(res)
"""
15
"""

print('*' * 80)


# Dmitry Voytik
def sum_counter_2(lst: list[int], idx1: int, idx2: int) -> int:
    if 0 < idx1 < idx2:
        return sum(lst[idx1:idx2 + 1])
    if 0 < idx1 < idx2 and idx2 > len(lst):
        return sum(lst[idx1:])


res = sum_counter_2([1, 2, 3, 4, 789], -1, 42)
print(res)
"""
None
"""

print('*' * 80)


# Khalil Batkaev
def list_sum(numbers: list, start_idx: int, end_idx: int):
    if start_idx < 0:
        start_idx = 0
    if start_idx > end_idx:
        start_idx, end_idx = end_idx, start_idx
    return sum(numbers[start_idx:end_idx])


res = list_sum([1, 2, 3, 4, 789], -1, 42)
print(res)
"""
799
"""

res = list_sum([1, 2, 3, 4, 5], 2, 3)
print(res)
"""
3
"""

res = list_sum([1, 2, 3, 4, 5], -20, 3)
print(res)
"""
6
"""

res = list_sum([1, 2, 3, 4, 5], 2, 654653)
print(res)
"""
12
"""

res = list_sum([1, 2, 3, 4, 5], -25, 654653)
print(res)
"""
15
"""

res = list_sum([1, 2, 3, 4, 5], -1, 654653)
print(res)
"""
15
"""

res = list_sum([1, 2, 3, 4, 5], 42, -6)
print(res)
"""
15
"""

res = list_sum([1, 2, 3, 4, 5], 42, -2)
print(res)
"""
9
"""


def list_sum_2(numbers: list, start_idx: int, end_idx: int):
    i = min(start_idx, end_idx) if min(start_idx, end_idx) >= 0 else 0
    j = max(start_idx, end_idx) if max(start_idx, end_idx) < len(numbers) \
        else len(numbers)
    return sum(numbers[i:j])


res = list_sum_2([1, 2, 3, 4, 5], 42, -2)
print(res)
print(sum([]))
res = list_sum_2([1, 2, 3, 4, 5], 0, -2)
print(res)
