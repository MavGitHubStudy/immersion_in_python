"""
Задание №5

Напишите программу, которая выводит на экран числа от 1 до 100.

При этом вместо чисел, кратных трём, программа должна выводить
слово "Fizz".

Вместо чисел, кратных пяти - слово "Buzz".

Если число кратно и 3, и 5, программа должна выводить
слово "FizzBuzz".

*Превратите решение в генераторное выражение.
"""


# mav
def func(num_):
    if num_ % 3 == 0 and num_ % 5 == 0:
        yield 'FizzBuzz'
    elif num_ % 3 == 0:
        yield 'Fizz'
    elif num_ % 5 == 0:
        yield 'Buzz'
    else:
        yield num_


# result = (num for num in range(0, 100 + 1, 2) if num // 10 + num % 10 != 8)
for num in range(1, 100 + 1):
    print(*func(num), end=' ')
# print()

print('*' * 80)

# Khalil Batkaev
result = ('FizzBuzz' if num % 3 == 0 and num % 5 == 0
          else 'Fizz' if num % 3 == 0
          else 'Buzz' if num % 5 == 0
          else num
          for num in range(1, 100 + 1))
print(*result)

print('*' * 80)

# Dmitry Voytic - вариант хуже, т.к. создаётся ГЕНЕРАТОР ИЗ ГЕНЕРАТОРА !
nums = (i for i in range(1, 100+1))
res = ('FizzBuzz' if j % 3 == 0 and j % 5 == 0 else
       'Fizz' if j % 3 == 0 else
       'Buzz' if j % 5 == 0 else
       j for j in nums)
print(*res)
