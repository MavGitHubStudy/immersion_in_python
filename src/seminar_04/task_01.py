"""
Задание №1

- Напишите функцию, которая принимает строку текста.
  Вывести функцией каждое слово с новой строки.

- Строки нумеруются начиная с единицы.

- Слова выводятся отсортированными согласно кодировки
  Unicode

- Текст выравнивается по правому краю так, чтобы
  у самого длинного слова был один пробел между ним
  и номером строки.
"""


def string_preview(text: str) -> None:
    text = sorted(text.split())
    # print(text)
    max_len = max(map(lambda x: len(x), text))
    """
    Получаем последовательность длин слов, 
    а затем выбираем из неё max
    """
    max_len = len(max(text, key=len))
    """
    Функция maх возвращает 'появилась' как самое длинное слово.
    Функция len возвращает длину этого слова.
    """
    # max_len = max([len(x) for x in text])
    max_len = max((len(x) for x in text))
    """
    Генератор списков, который перебирает каждое слово
    в списке, вычисляет его длину, а затем определяет 
    max. 
    Квадратные скобки определяют список, в котором будут
    храниться длины всех слов, и который занимает память
    компьютера.
    Но нам длины не нужны, нам нужно только максимальное
    значение!
    Если мы заменим квадратные скобки на круглые, то
    вместо формирования списка, мы будем формировать 
    генераторное выражение, которое будет 'на лету'
    генерировать эти значения и передавать их в функцию
    max. 
    """

    for i, world in enumerate(text, start=1):
        print(f'{i:>3} {world:>{max_len}}')


# Заглавные буквы идут раньше при сортировке
string_preview('Лекция появилась только сегодня')
