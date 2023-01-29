from math import sqrt


"""
Вычислить корни квадратного уравнения,
коэффициенты a, b, c которого вводятся с клавиатуры.

Квадратное уравнение имеет вид

ax2 + bx + c = 0

При его решении сначала вычисляют дискриминант по формуле

D = b2 - 4ac

Если D > 0, то квадратное уравнение имеет два корня; 
если D = 0, то 1 корень; и 
если D < 0, то делают вывод, что корней нет.

Таким образом, программа для нахождения корней квадратного уравнения
может иметь три ветви условного оператора.

Функция float преобразует переданный ей аргумент в вещественное число.
"""


def quadratic_equation():
    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + sqrt(discr)) / (2 * a)
        x2 = (-b - sqrt(discr)) / (2 * a)
        print("x1 = %.2f\nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")


"""
Задание №6

- Напишите программу, которая запрашивает год и проверяет его на високосность.
- Распишите все возможные проверки в цепочке elif
- Откажетесь от магических чисел
- Обязательно учтите год ввода Григорианского календаря
- В коде должны быть один input и один print

https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BE%D0%B4
"""


def task_6():
    SMALL_YEAR = 4
    MIDDLE_YEAR = 100
    BIG_YEAR = 400
    GREG_YEAR = 1582

    year = int(input('Введите год в формате yyyy: '))
    if year < GREG_YEAR:
        result = "Григорианский календарь ещё не существует"
    elif year % BIG_YEAR == 0:
        result = "Високосный"
    elif year % MIDDLE_YEAR == 0:
        result = "Обычный"
    elif year % SMALL_YEAR == 0:
        result = "Високосный"
    else:
        result = "Обычный"

    # if year < GREG_YEAR:
    #     result = "Григорианский календарь ещё не существует"
    # elif year % SMALL_YEAR != 0:
    #     result = "Обычный"
    # elif year % MIDDLE_YEAR == 0:
    #     if year % BIG_YEAR == 0:
    #         result = "Високосный"
    #     else:
    #         result = "Обычный"
    # else:
    #     result = "Високосный"

    # А теперь выберем все случаи, когда год обычный и запишем их в одну строку:
    #
    # if year % SMALL_YEAR != 0 or \
    #         year % MIDDLE_YEAR == 0 and year % BIG_YEAR != 0:
    #     print("Обычный")
    # else:
    #     print("Високосный")

    print(result)


"""
Задание №7

- Пользователь вводит число от 1 до 999. Используя операции с числами, сообщите,
  что введено: цифра, двузначное число или трёхзначное число.
  
- Для цифры верните её квадрат, например 5 - 25

- Для двузначного число верните произведение цифр, например 30 - 0

- Для трёхзначного числа верните его зеркальное отображение, например 520 - 25

- Если число не из диапазона, запросите новое число

- Откажитесь от магических чисел

- В коде должны быть один input и один print
"""


def task_7():
    MIN_NUMBER = 1
    MAX_NUMBER = 999
    TEN = 10
    HUNDRED = 100
    ZERO = 0
    SQUARE = 2
    while True:
        num = int(input("Введите число от 1 до 999 включительно: "))
        if MIN_NUMBER <= num <= MAX_NUMBER:
            break

    if num // TEN == 0:
        result = "цифра " + str(num) + " - " + str(num ** SQUARE) + "(" \
                                                            "квадрат цифры)"
    elif num // HUNDRED == 0:
        result = "двузначное число " + str(num) + " - " + str(
            num // TEN + num % TEN) + "(сумма его цифр)"
    else:
        # result = "трёхзначное число " + str(num) + " - " + str(
        #     num % TEN) + str(num // TEN % TEN) + str(num // HUNDRED) \
        #     + "(зеркальное число)"
        math_result = (num % TEN * HUNDRED) + (num // TEN % TEN * TEN) \
                      + (num // HUNDRED)
        result = "трёхзначное число " + str(num) + " - " + str(
            math_result) + "(зеркальное число)"
    print(result)


def main():
    # quadratic_equation()
    # task_6()
    task_7()


if __name__ == "__main__":
    main()
