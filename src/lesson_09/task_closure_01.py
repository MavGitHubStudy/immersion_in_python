"""
task_closure_01.py

closure[ˈkləʊʒə] - замыкание
"""


def func(a):
    x = 1  # функция работает с х который равен 1,
    # т.е. мы замкнули х внутри функции
    res = x + a
    return res


x = 100
print(func(5))
