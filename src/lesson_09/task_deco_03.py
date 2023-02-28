from typing import Callable


def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Старт декоратор А')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print('Завершение декоратора А')
        return result

    print('Возвращаем декоратор А')
    return wrapper_a


def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Старт декоратора B')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print('Завершение декоратора B')
        return result

    print('Возвращаем декоратор B')
    return wrapper_b


def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Старт декоратора C')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print('Завершение декоратора C')
        return result

    print('Возвращаем декоратор С')
    return wrapper_c


# Декорирование всегда происходит снизу вверх и один раз!
@deco_c
@deco_b
@deco_a
def main():
    print('Старт основной функции')


if __name__ == '__main__':
    print('>>> Запуск main()')
    main()
    print('>>> Завершение main()')
"""
# Декорирование всегда происходит снизу вверх и один раз
# в момент запуска нашей программы !
# ==========================================================
Возвращаем декоратор А
Возвращаем декоратор B
Возвращаем декоратор С
# ==========================================================
# Работа декораторов происходит сверху вниз !
# ==========================================================
>>> Запуск main()
Старт декоратора C
Запускаю wrapper_b
Старт декоратора B
Запускаю wrapper_a
Старт декоратор А
Запускаю main
Старт основной функции
Завершение декоратора А
Завершение декоратора B
Завершение декоратора C
>>> Завершение main()

Process finished with exit code 0
"""
