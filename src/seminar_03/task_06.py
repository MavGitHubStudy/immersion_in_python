"""
Задача №6

Пользователь вводит строку текста. Вывести каждое слово
с новой строки.

- Строки нумеруются начиная с единицы

- Слова выводятся отсортированными согласно кодировки Unicode

- Текст выравнивается по правому краю так, чтобы у самого
  длинного слова был один пробел между ним и номером строки
"""
start_lst = input("Enter any words: ").split()
# temp_lst = []
#
# for i in start_lst.split():
#     temp_lst.append(i)

for idx, val in enumerate(sorted(start_lst), start=1):
    # print(idx, val)
    print(f'{idx} {val:>25}')


print('*' * 79)
START_NUM = 1

data = input("Введите текст: ").split()
data.sort()
max_len = 0
for item in data:
    if len(item) > max_len:
        max_len = len(item)

for i, item in enumerate(data, start=START_NUM):
    print(f'{i} {item:>{max_len}}')
