from random import randint


def fun(a1, a2, b):
    random_num = randint(a1, a2)
    input_num = int(input(f'Введите число от {a1} до {a2}: '))
    k = 1
    while random_num != input_num and b > k:
        if random_num < input_num:
            print('Введите число меньше')
        elif random_num > input_num:
            print('Введите число больше')
        input_num = int(input(f'Введите число от {a1} до {a2}: '))
        k += 1

    # if random_num == input_num:
    #     return True
    # return False
    return random_num == input_num   # Возвращаем результат сравнения


if __name__ == '__main__':
    print(fun(2, 10, 5))
