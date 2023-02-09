"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
ONE = 1
source_list = [1, 3.14, 4, 'text', 1, 7.3, 'text', 5, 3.14, 'example', 2, 3,
               9, 5, 8, 0.3, 7, 1, 3, 6, 8, 7]
print(source_list)
spam = {}

for num in source_list:
    if num in spam:
        spam[num] += 1
    else:
        spam[num] = 1


for key, item in spam.items():
    if item == ONE:
        source_list.remove(key)
print(list(set(source_list)))
