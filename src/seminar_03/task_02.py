"""
Задание №2

Пользователь вводит данные. Сделайте проверку данных и
преобразуйте, если возможно, в один из вариантов ниже:

- целое положительное число
- вещественное положительное или отрицательное число
- строку в нижнем регистре, если в троке есть хотя бы
  одна заглавная буква
- строку в верхнем (нижнем) регистре в остальных случаях
"""
some_data = input('Введите: ')
# if some_data.isdigit():
#     print(f'{int(some_data)} - целое положительное число')
if some_data.isdecimal():
    print(f'{int(some_data)} - целое положительное или '
          f'отрицательное число')
elif some_data.isalpha():
    if some_data.lower() == some_data:
        print('В нижнем регистре')
    else:
        print('В верхнем регистре')
elif some_data.count('-') <= 1 and some_data[1:].count('-') == 0 and \
        some_data.count('.') == 1 and some_data.replace('-', '').replace(
        '.', '').isdecimal():  #
    print('Вещественное')
