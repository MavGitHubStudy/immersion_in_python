from random import randint


def binary_random_search(minimum: int, maximum: int, count: int) -> bool:
    num = randint(minimum, maximum + 1)
    search_num = None
    while search_num != num:
        search_num = int(input("Угадайте число: "))
        print([
                  ["Загаданное число меньше", "Загаданное число больше"]
                  [search_num < num],
                  "Угадали!"
              ]
              [search_num == num])
        count -= 1
        if count == 0:
            print("Попытки закончились")
            return False
    return True


if __name__ == '__main__':
    print(binary_random_search(-1, -1, 5))
    # print(binary_random_search(0, 10, 5))
