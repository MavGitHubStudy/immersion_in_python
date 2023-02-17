"""
Задание №2

- Создайте модуль с функцией внутри.

- Функция принимает на вход три целых числа: нижнюю
  и верхнюю границу и количество попыток.

- Внутри генерируется случайное число в указанных границах
  и пользователь должен угадать его за заданное число.

- Функция выводит подсказки "больше" и "меньше".

- Если число угадано, возвращается истина, а если попытки
  исчерпаны - ложь.
"""
# 26:30
from random import randrange


def guess_the_number(start: int, stop: int, num_tries: int):
    num = randrange(start, stop + 1)
    count = 0
    while count < num_tries:
        count += 1
        user_in = int(input("Введите число: "))
        if num < user_in:
            print(f"Загаданное число меньше {user_in}")
        elif num > user_in:
            print(f"Загаданное число больше {user_in}")
        else:
            print(f"Угадали число за {count} попыток")
            return True
    return False


if __name__ == "__main__":
    guess_the_number(1, 10, 5)
