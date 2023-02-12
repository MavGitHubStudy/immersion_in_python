"""
Задача №3

- Функция получает на вход строку из двух чисел через пробел.

- Сформируйте словарь, где ключом будет символ из Unicode,
  а значением - целое число.

- Диапазон пар ключ-значение от наименьшего из введённых
  пользователем чисел до наибольшего включительно.
"""


# 00:41:00
# Khalil Batkaev
def unicode_table(text: str) -> dict[str, int]:
    num_1, num_2 = map(int, text.split())
    if num_2 < num_1:
        num_1, num_2 = num_2, num_1
    result = {}
    for num in range(num_1, num_2 + 1):
        result[chr(num)] = num

    return result


# Дмитрий Кардава
def func(st: str) -> dict[str, int]:
    first, second = map(int, st.split())
    if first > second:
        first, second = second, first
    d = {}
    for i in range(first, second + 1):
        d.setdefault(chr(i), i)  # более затратно по ресурсам 

    return d


res = unicode_table('65 90')
print(res)
res = func('65 90')
print(res)
