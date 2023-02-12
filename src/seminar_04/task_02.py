"""
Задание №2

- Напишите функцию, которая принимает сроку текста.

- Сформируйте список с уникальными кодами Unicode
  каждого символа введённой строки, отсортированный
  по убыванию.
"""
# 27:40 - 30:30


# Dmitry Voytik
def unicode_getter(string: str) -> list[int]:
    unicode_lst = []
    for i in string:
        unicode_lst.append(ord(i))

    return sorted(set(unicode_lst), reverse=True)


print(unicode_getter("Лекция только сегодня появилась"))


def unicode_getter_better(string: str) -> list[int]:
    unicode_lst = []
    for char in set(string):
        unicode_lst.append(ord(char))

    return sorted(set(unicode_lst), reverse=True)
    # sorted() всегда возвращает список!


print(unicode_getter("Лекция только сегодня появилась"))
print(unicode_getter_better("Лекция только сегодня появилась"))
