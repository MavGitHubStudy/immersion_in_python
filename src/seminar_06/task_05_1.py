"""
Задание №5

Добавьте в модуль с загадками функцию, которая хранит
словарь списков.

Ключ словаря - загадка, значение - список с отгадками.

Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""


def guess(question: str, answer: list[str], count: int):
    count_ = 0
    print(question)

    while True:
        count_ += 1
        choice = input('Введите отгадку: ').lower()

        if choice in answer:
            return count_  # отгадали с count_ попытки
        print(f'Неверно. Осталось {count - count_} попыток')

        if count == count_:
            return 0  # проиграли


def library(func, count):
    data = {
        'Без окон, без дверей, полна горница людей': ['огурец', 'арбуз',
                                                      'помидор'],
        'Зимой и летом одним цветом': ['ёлка', 'ель', 'сосна']
    }
    for key, item in data.items():
        print(func(key, [elem.lower() for elem in item], count))


if __name__ == '__main__':
    print(library(guess, 3))
