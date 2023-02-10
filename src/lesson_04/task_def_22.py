def main(a):
    """Не локальные переменные"""
    x = 1

    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }')  # Для демонстрации раьботы,
        # но не для привычки печатать из функции
        return y + 1

    return x + func(a)


x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')
"""
In main x = 42
In func x = 101
x = 42	z = 44
"""