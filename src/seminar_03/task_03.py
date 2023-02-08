"""
Задание №3

Создайте вручную кортеж, содержащий элементы разных
типов.

Получите из него словарь списков, где
- ключ - тип элемента
- значение - список элементов данного типа
"""
# 49:20
random_tuple = (1, 2.13, 5, 8.12, 'hello', 8, 'hi', True, [1, 2, 3], [4, 5, 6])
result_dict = {}
values = []

for item in random_tuple:
    # print(item)
    values = result_dict.get(type(item))
    if values:
        values.append(item)
    else:
        values = [item]
    result_dict.setdefault(type(item), values)
print(result_dict)

print('*' * 79)
d = {}
for i in random_tuple:
    d.setdefault(type(i), []).append(i)
print(d)

print('*' * 79)
d = {}
for i in random_tuple:
    d[type(i)] = d[type(i)] + [i] if type(i) in d else [i]
print(d)
