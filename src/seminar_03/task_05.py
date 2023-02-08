"""
Задание №5

Создайте вручную список с повторяющимися целыми числами.

Сформируйте список с порядковыми номерами нечётных
элементов исходного списка.

Нумерация начинается с единицы.
"""
START_NUM = 1

list_num = [1, 2, 1, 3, 2, 1, 4, 5, 4, 5, 6, 5]
print(list_num)
list_res = []
for i, el in enumerate(list_num, start=START_NUM):
    if el % 2 != 0:
        list_res.append(i)
print(list_res)


print('*' * 79)
print('Не для этого семинара, а для общего развития')
even_idx_list = [i for i, el in enumerate(list_num, start=START_NUM) if el % 2]
print(even_idx_list)
