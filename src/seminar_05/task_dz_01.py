"""
Задание №6

Выведите в консоль таблицу умножения от 2х2 до 9х10 как
на школьной тетрадке.

Таблицу создайте в виде однострочного генератора, где каждый
элемент генератора - отдельный пример таблицы умножения.

Для вывода результата используйте "принт" без перехода
на новую строку.
2 x 2 =  4    3 x 2 =  6    4 x 2 =  8    5 x 2 = 10
2 x 3 =  6    3 x 3 =  9    4 x 3 = 12    5 x 3 = 15
2 x 4 =  8    3 x 4 = 12    4 x 4 = 16    5 x 4 = 20
2 x 5 = 10    3 x 5 = 15    4 x 5 = 20    5 x 5 = 25
2 x 6 = 12    3 x 6 = 18    4 x 6 = 24    5 x 6 = 30
2 x 7 = 14    3 x 7 = 21    4 x 7 = 28    5 x 7 = 35
2 x 8 = 16    3 x 8 = 24    4 x 8 = 32    5 x 8 = 40
2 x 9 = 18    3 x 9 = 27    4 x 9 = 36    5 x 9 = 45
2 x 10= 20    3 x 10= 30    4 x 10= 40    5 x 10= 50

6 x 2 = 12    7 x 2 = 14    8 x 2 = 16    9 x 2 = 18
6 x 3 = 18    7 x 3 = 21    8 x 3 = 24    9 x 3 = 27
6 x 4 = 24    7 x 4 = 28    8 x 4 = 32    9 x 4 = 36
6 x 5 = 30    7 x 5 = 35    8 x 5 = 40    9 x 5 = 45
6 x 6 = 36    7 x 6 = 42    8 x 6 = 48    9 x 6 = 54
6 x 7 = 42    7 x 7 = 49    8 x 7 = 56    9 x 7 = 63
6 x 8 = 48    7 x 8 = 56    8 x 8 = 64    9 x 8 = 54
6 x 9 = 54    7 x 9 = 63    8 x 9 = 72    9 x 9 = 81
6 x 10= 70    7 x 10= 70    8 x 10= 80    9 x 10= 90
"""
LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMNS = 4


for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMNS):  # 2 , 6(2+4)
    for j in range(LOWER_LIMIT, UPPER_LIMIT + 1):
        for k in range(i, i + COLUMNS):
            if j == UPPER_LIMIT and k == i + COLUMNS - 1:
                print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
            elif k == i + COLUMNS - 1:
                print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
            else:
                print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')


print('*' * 80)
print(' ', end='')

table = (f"{k:>} x {j:>2} = {k * j:>2}\n\n" if j == UPPER_LIMIT and
         k == i + COLUMNS - 1 else
         f"{k:>} x {j:>2} = {k * j:>2}\n" if k == i + COLUMNS - 1 else
         f"{k:>} x {j:>2} = {k * j:>2}\t" for i in range(LOWER_LIMIT,
                                                         UPPER_LIMIT,
                                                         COLUMNS)
         for j in range(LOWER_LIMIT, UPPER_LIMIT + 1) for k in range(i,
                                                                     i + COLUMNS
                                                                     )
         )

print(*table, end='')
