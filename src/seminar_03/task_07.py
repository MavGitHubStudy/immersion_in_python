"""
Задание №7

- Пользователь вводит строку текста.

- Подсчитайте, сколько раз встречается каждая буква
  в строке без использования метода count и с ним.

- Результат сохраните в словаре, где ключ - символ,
  а значение - частота встречи символа в строке.

- Обратите внимание на порядок ключей. Объясните,
  почему они совпадают или не совпадают в ваших
  решениях.
"""
from collections import Counter

# text = 'any string  who is name table'

string_for_work = input("Enter text: ")
res = Counter(string_for_work)
# print(res)
# print('*' * 79)
print(dict(res))

print('*' * 79)
text = 'any string  who is name table'
res = {}
for c in text:
    res[c] = res.setdefault(c, 0) + 1
print(res)

print('*' * 79)
text = 'any string  who is name table'
res = {}
for c in text:
    res.setdefault(c, text.count(c))
print(res)

print('*' * 79)
text = 'any string  who is name table'
res = {}
for c in set(text):  # set(text) - только уникальные буквы внутри строки
    res[c] = text.count(c)
print(res)
