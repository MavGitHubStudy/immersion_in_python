"""
Задание


1) Напишите следующие функции:

   - Декоратор, запускающий функцию нахождения корней квадратного
     уравнения с каждой тройкой чисел из csv файла;

   - Декоратор, сохраняющий переданные параметры и результаты
     работы в json файл.

3) Соберите пакет с играми из тех файлов, что уже были созданы
   в рамках курса.
"""


import csv
# from pathlib import Path
from math import sqrt
from random import randint
from typing import Tuple, List, Callable

MIN_NUM = -1000
MAX_NUM = 50
QUANTITY = 3

MIN_ROWS = 100
MAX_ROWS = 1000


def incoming_equations(_file: str):

    def deco(func: Callable):
        data = []

        def wrapper(*args, **kwargs):
            with open(_file, 'r', encoding='utf-8') as f_csv:
                csv_reader = csv.reader(f_csv)
                for line_no, line in enumerate(csv_reader, 1):
                    if line_no != 1:
                        str_nums = list(line)
                        int_nums = map(int, str_nums)
                        a, b, c = int_nums

                        part1 = f'{a}•x²'

                        if b > 0:
                            part2 = f'+{b}•x'
                        else:
                            part2 = f'{b}•x'

                        if c > 0:
                            part3 = f'+{c}'
                        else:
                            part3 = f'{c}'

                        print()
                        print(f'{part1}{part2}{part3}=0')
                        result = func(a, b, c, *args, **kwargs)
                        # result = func(*line, *args, **kwargs)
                        show_solution(result)
                        data.append(result)

            return data

        return wrapper

    return deco


def equation2csv(_file: str, _rows: int) -> None:
    if _rows < MIN_ROWS:
        _rows = MIN_ROWS
    elif _rows > MAX_ROWS:
        _rows = MAX_ROWS

    header = ['a', 'b', 'c']
    with open(_file, 'w', encoding='utf-8') as f_csv:
        csv_writer = csv.writer(f_csv)

        # write the header
        csv_writer.writerow(header)

        # write the data
        for _ in range(_rows):
            data = generate_ints(MIN_NUM, MAX_NUM, QUANTITY)
            csv_writer.writerow(data)


def generate_ints(_min_num: int, _max_num: int, _quantity) -> List:
    lst = []
    for _ in range(_quantity):
        int_num = randint(_min_num, _max_num)
        while int_num == 0:
            int_num = randint(_min_num, _max_num)
        lst.append(int_num)
    return lst


"""
Функция вычисления корней квадратного уравнения,
коэффициенты a, b, c которого являются входными параметрами.

Квадратное уравнение имеет вид

ax^2 + bx + c = 0

При его решении сначала вычисляют дискриминант по формуле

D = b2 - 4ac

Если D > 0, то квадратное уравнение имеет два корня;
если D = 0, то 1 корень; и
если D < 0, то делают вывод, что корней нет.

Таким образом, программа для нахождения корней квадратного уравнения
может иметь три ветви условного оператора.

Функция float преобразует переданный ей аргумент в вещественное число.
"""

file_name = 'equation.csv'


@incoming_equations(file_name)
def quadratic_equation(_a: int,
                       _b: int,
                       _c: int) -> Tuple | float | None:
    a = float(_a)
    b = float(_b)
    c = float(_c)
    _discr = b ** 2 - 4 * a * c
    if _discr > 0:
        x1 = (-b + sqrt(_discr)) / (2 * a)
        x2 = (-b - sqrt(_discr)) / (2 * a)
        # print("x1 = %.2f\nx2 = %.2f" % (x1, x2))
        return x1, x2
    elif _discr == 0:
        x = -b / (2 * a)
        # print("x = %.2f" % x)
        return x
    else:
        # print("Корней нет")
        return None


def show_solution(res: any) -> None:
    if type(res) == tuple:
        print(f'Два корня: x₁ = {res[0]}, x₂ = {res[1]}')
    elif type(res) == float:
        print(f'Один корень: x = {res}')
    elif res is None:
        print(f'Корней нет')


if __name__ == '__main__':
    # # два корня уравнения
    # result = quadratic_equation(-3, 6, 2)
    # print(f'-3•x²+6•x+2=0')
    # show_solution(result)
    # # один корень уравнения
    # print(f'-4•x²+28•x-49=0')
    # result = quadratic_equation(-4, 28, -49)
    # show_solution(result)
    # # корней нет
    # result = quadratic_equation(4, 1, 2)
    # print(f'4•x²+x+2=0')
    # show_solution(result)

    # print(generate_ints(MIN_NUM, MAX_NUM, QUANTITY))

    # equation2csv('equation.csv', 50)
    # equation2csv('equation.csv', 1300)
    quadratic_equation()
