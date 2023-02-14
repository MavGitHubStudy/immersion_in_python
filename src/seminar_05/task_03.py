"""
Задание № 3

Продолжаем развивать задачу 2.

Возьмите словарь, который вы получили. Сохраните его итератор.

Далее выведите первые 5 пар ключ-значение, обращаясь к итератору,
а не к словарю.
"""
text = "проверочная строка"
result = {char: ord(char) for char in text}
print(result)

res_iter = iter(result.items())
print(res_iter)
# print(next(res_iter))
# print(next(res_iter))
# print(next(res_iter))
# print(next(res_iter))
# print(next(res_iter))
for _ in range(5):
    print(next(res_iter))

print('*' * 80)

# Dmitry Voytik
# более сложный вариант
itr = iter(items_ for items_ in result.items())
print(itr)
for _ in range(5):
    print(next(itr))
