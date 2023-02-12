"""
Решить задачи, которые не успели решить на семинаре.

Задание №6

Функция получает на вход список чисел и два индекса.

Вернуть сумму чисел между переданными индексами.

Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def list_sum(numbers: list, start_idx: int, end_idx: int):
    i = min(start_idx, end_idx) if min(start_idx, end_idx) >= 0 else 0
    j = max(start_idx, end_idx) if max(start_idx, end_idx) < len(numbers) \
        else len(numbers)
    return sum(numbers[i:j])


res = list_sum([1, 2, 3, 4, 5], 42, -2)
print(res)
res = list_sum([1, 2, 3, 4, 5], 0, -2)
print(res)
