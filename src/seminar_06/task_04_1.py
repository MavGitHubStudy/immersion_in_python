"""
Задание №4

Создайте модуль с функцией внутри.

Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.

Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
"""


def one_hundred_for_one(question: str, answers: list[str], count: int) -> int:
    other_count = 0
    while count > other_count:
        print(question)
        from_user = input("Ваш вариант: ")
        other_count += 1
        if from_user.capitalize() in answers:
            return other_count
    return 0


if __name__ == '__main__':
    text = "Как зовут преподавателя?"
    variants = ["Михаил", "Алексей", "Анна", "С3ро"]
    print(one_hundred_for_one(text, variants, 3))
