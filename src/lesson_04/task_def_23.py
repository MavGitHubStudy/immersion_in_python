LIMIT = 1_000


def func(x, y):
    result = x ** y % LIMIT  # допустимый приём
    return result


print(func(42, 73))
