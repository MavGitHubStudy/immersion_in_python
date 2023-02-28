"""
task_closure_06.py

closure[ˈkləʊʒə] - замыкание
"""
# 12:52
from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text = ''

    def add_two_str(b: str) -> str:
        nonlocal text  # чтобы не получить ошибку с неизменяемой переменной
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
"""
Hello, Alex
Hello, Alex, Karina
Good bye, Alina
Hello, Alex, Karina, John
Good bye, Alina, Neo

Process finished with exit code 0
"""
