"""
# task_01.py (24:10 - 30:16 - 33:57)
"""
"""
Задание №1

- Создайте функцию, которая запрашивает числовые данные от
  пользователя до тех пор, пока он не ведёт целое или 
  вещественное число.
- Обрабатывайте не числовые данные как исключения.
"""


# def get_number() -> float | int:
def task() -> float | int:
    while True:
        value = input('Введите число: ')
        try:
            result = int(value) if '.' not in value else float(value)
            return result
        except ValueError:
            print(f'Неверный ввод: {value = }')


if __name__ == '__main__':
    print(task())
