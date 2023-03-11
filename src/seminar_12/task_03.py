"""
Задание №3

- Создайте класс-генератор.
- Экземпляр класса должен генерировать факториал числа
  в диапазоне от start до stop с шагом step.
- Если переданы два параметра, считаем step=1.
- Если передан один параметр, также считаем start=1.
"""


# 43:43 - 50:20 - 52:02


class Factorial:
    # def __init__(self, stop: int, start: int = 1, step: int = 1):
    def __init__(self, *args):
        match len(args):
            case 1:
                self.stop = args[0]
                self.start = self.step = 1
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):
        self.result = 1
        for i in range(2, self.start):
            self.result *= i
        while self.start <= self.stop:
            self.result *= self.start
            self.start += self.step
            return self.result
        raise StopIteration


def main():
    f1 = Factorial(5)
    for num in f1:
        print(num)
    print('*' * 50)
    f2 = Factorial(5, 10)
    for num in f2:
        print(num)
    print('*' * 50)
    f3 = Factorial(5, 10, 2)
    for num in f3:
        print(num)
    # for i in range(1, 10, 2):
    #     print(i)
    # print('*' * 50)
    # for i in range(1, 5):
    #     print(i)
    # print('*' * 50)
    # for i in range(3):
    #     print(i)
    # print('*' * 50)


if __name__ == '__main__':
    main()
"""
/home/.../.venv/bin/python /home/.../src/seminar_12/task_03.py 
1
2
6
24
120
**************************************************
120
720
5040
40320
362880
3628800
**************************************************
120
5040
362880

Process finished with exit code 0
"""
# 1:09:38
