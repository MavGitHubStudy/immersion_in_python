"""
Задание №4

Создайте вручную список с повторяющимися элементами.

Удалите из него все элементы, которые встречаются
дважды.
"""
TWO = 2

list_num = [1, 2, 1, 3, 2, 1, 4, 5, 4, 5, 6, 5]
print(list_num)
spam = {}

for num in list_num:
    if num in spam:
        spam[num] += 1
    else:
        spam[num] = 1

for key, item in spam.items():
    if item == TWO:
        list_num.remove(key)
        list_num.remove(key)

print(list_num)

print('*' * 79)
list_num = [1, 2, 1, 3, 2, 1, 4, 5, 4, 5, 6, 5]
print(list_num)
for el in list_num:
    if list_num.count(el) == TWO:
        list_num.remove(el)
        list_num.remove(el)
print(list_num)

print('*' * 79)
list_num = [1, 2, 1, 3, 2, 1, 4, 5, 4, 5, 6, 5]
COUNT = 3
print(list_num)
for el in list_num:
    if list_num.count(el) == COUNT:
        for _ in range(COUNT):
            list_num.remove(el)
print(list_num)


