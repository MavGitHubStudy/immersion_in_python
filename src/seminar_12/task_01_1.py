"""
Задание №1

Создайте класс-функцию, который считает факториал числа
при вызове экземпляра.

Экземпляр должен запоминать последние k значений.

Параметр k передаётся при создании экземпляра.

Добавьте метод для просмотра ранее вызываемых значений
и их факториалов.
"""
# 10:30
from collections import deque


class Factorial:
    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def main():
    f = Factorial(3)
    print(f(5))


if __name__ == '__main__':
    main()
"""
/home/.../seminar_12/task_01.py 
120

Process finished with exit code 0
"""
# 19:06
