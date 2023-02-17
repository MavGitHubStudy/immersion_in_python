"""
Задание №5

Добавьте в модуль с загадками функцию, которая хранит
словарь списков.

Ключ словаря - загадка, значение - список с отгадками.

Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""


def next_variants(question=None, answers=None, all_variants=None) -> dict[
                                                                   str:str]:
    if all_variants is None:
        all_variants = {}
    if question is not None:
        all_variants[question] = answers
    return all_variants


def get_play(variants_: dict) -> None:
    [one_hundred_for_one(i, j) for i, j in variants_.items()]


def one_hundred_for_one(question: str, answers: list[str], count=3) -> int:
    other_count = 0
    while other_count < count:
        print(question)
        from_user = input("Ваш вариант: ")
        other_count += 1
        if from_user.capitalize() in answers:
            return other_count

    return 0


if __name__ == '__main__':
    text = "Как зовут преподавателя?"
    variants = ["Михаил", "Алексей", "Анна", "С3ро"]
    next_variants(text, variants)
    text = "Когда начнётся курс Java?"
    variants = ["Июнь", "Июль", "Никогда"]
    next_variants(text, variants)
    get_play(next_variants())
