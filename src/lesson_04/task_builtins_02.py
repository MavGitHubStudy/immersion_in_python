"""add(function, iterable)"""
numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))  # оборачиваем результат работы
print(res)
"""
(42, 1024)
"""