"""
Задание №5

Добавьте в модуль с загадками функцию, которая хранит
словарь списков.

Ключ словаря - загадка, значение - список с отгадками.

Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""


def secrets():
    secrets_dict = {
        "Загадка1": ('ответ1', 'ответ2'),
        "Загадка2": ('ответ3', 'ответ4'),
    }

    for secret, answers in secrets_dict.items():
        pass
