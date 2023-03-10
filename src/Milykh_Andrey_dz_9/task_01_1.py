"""
Задание

1) Напишите следующие функции:

   - Нахождение корней квадратного уравнения;

   - Генерация csv файла с тремя случайными числами в каждой строке
     (100-1000 строк).
"""
import csv
from math import sqrt
from random import randint
from typing import Tuple, List

MIN_NUM = -100
MAX_NUM = 100
QUANTITY = 3

MIN_ROWS = 100
MAX_ROWS = 1000


def equation2csv(_file: str, _rows: int) -> None:
    """Функция генерации csv файла

    Parameters
    ----------
    _file : str
        имя csv-файла для сохранения параметров квадратных уравнений

    _rows : int
        количество строк параметров квадратных уравнений;
        каждая строка - параметры одного квадратного уравнения

    :return: None
        - функция ничего не возвращает
    """
    if _rows < MIN_ROWS:
        _rows = MIN_ROWS
    elif _rows > MAX_ROWS:
        _rows = MAX_ROWS

    header = ['a', 'b', 'c']
    with open(_file, 'w', encoding='utf-8') as f_csv:
        writer = csv.writer(f_csv)

        # write the header
        writer.writerow(header)

        # write the data
        for _ in range(_rows):
            data = generate_ints(MIN_NUM, MAX_NUM, QUANTITY)
            writer.writerow(data)


def generate_ints(_min_num: int, _max_num: int, _quantity: int) -> List:
    """Функция генерации целых чисел, кроме 0

    Parameters
    ----------
    _min_num: int
        минимальное целое число

    _max_num : int
        максимальное целое число

    _quantity : int
        количество генерируемых целых чисел

    :return: List
        - функция возвращает список сгенерированных целых чисел
    """
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


def quadratic_equation(_a: int,
                       _b: int,
                       _c: int) -> Tuple | float | None:
    """Функция вычисления корней квадратного уравнения

    a•x²+b•x+c=0

    Parameters
    ----------
    _a : int, _b : int, _c : int
        коэффициенты квадратного уравнения

    :return: Tuple | float | None
        - функция возвращает
          Tuple - если два корня,
          float - если один корень,
          None - если корней нет
    """
    a = float(_a)
    b = float(_b)
    c = float(_c)
    _discr = b ** 2 - 4 * a * c
    if _discr > 0:
        x1 = (-b + sqrt(_discr)) / (2 * a)
        x2 = (-b - sqrt(_discr)) / (2 * a)
        return x1, x2
    elif _discr == 0:
        x = -b / (2 * a)
        return x
    else:
        return None  # корней нет


def show_solution(res: any) -> None:
    if type(res) == tuple:
        print(f'Два корня: x₁ = {res[0]}, x₂ = {res[1]}')
    elif type(res) == float:
        print(f'Один корень: x = {res}')
    elif res is None:
        print(f'Корней нет')


if __name__ == '__main__':
    # два корня уравнения
    result = quadratic_equation(-3, 6, 2)
    print(f'-3•x²+6•x+2=0')
    show_solution(result)
    # один корень уравнения
    print(f'-4•x²+28•x-49=0')
    result = quadratic_equation(-4, 28, -49)
    show_solution(result)
    # корней нет
    result = quadratic_equation(4, 1, 2)
    print(f'4•x²+x+2=0')
    show_solution(result)

    # print(generate_ints(MIN_NUM, MAX_NUM, QUANTITY))

    equation2csv('equation.csv', 50)  # в файле будет 100 строк с данными
    # equation2csv('equation.csv', 1100)  # в файле будет 1000 строк с данными
