"""
task_closure_05.py

closure[ˈkləʊʒə] - замыкание
"""
# 11:28
from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)

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
