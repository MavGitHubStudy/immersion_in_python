"""
Задание №2

- Доработаем задачу 1.
- Создайте менеджер контекста, который при выходе
  сохраняет значения JSON в файле.

Задание №1

- Создайте класс-функцию, который считает факториал числа
  при вызове экземпляра.
- Экземпляр должен запоминать последние k значений.
- Параметр k передаётся при создании экземпляра.
- Добавьте метод для просмотра ранее вызываемых значений
  и их факториалов.
"""
# 29:40
from collections import deque


class Factorial:
    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})
        return result

    def view(self):
        return self.memory


def main():
    f = Factorial(3)
    print(f(5))
    print(f(2))
    print(f(12))
    print(f(7))
    print(f(21))
    print(f.view())


if __name__ == '__main__':
    main()
"""
/home/.../seminar_12/task_01.py 
120

Process finished with exit code 0
"""
# 19:06
"""
/home/.../immersion_in_python/.venv/bin/python 
/home/.../immersion_in_python/src/seminar_12/task_01_2.py 
120
2
479001600
5040
51090942171709440000
deque([{12: 479001600}, {7: 5040}, {21: 51090942171709440000}], maxlen=3)

Process finished with exit code 0
"""
# 22:16
