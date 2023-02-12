"""
Задание №4

- Функция получает на вход список чисел.

- Отсортируйте его элементы in place без использования
  встроенных в язык сортировок.

- Как вариант, напишите сортировку пузырьком. Её
  описание есть в википедии.
"""


# Dmitry Voytik
def bubble_sort(nums: list[int]) -> list[int]:
    swapped = False
    for i in range(len(nums) - 1, 0, -1):  # с конца, до начала,
    # не включительно
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return nums


# Это не сортировка bubble !!!
def bubble_sort_2(numbers: list[int]) -> None:
    for i in range(len(numbers)):
        is_sorted = True
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                is_sorted = False
        if is_sorted:
            break


res = bubble_sort([1, 2, 5, 11, 9, 5, 6, 3, 1, 0])
print(res)

numbers_list = [5, 7, 6, 2, 1, 10]
bubble_sort_2(numbers_list)
print(numbers_list)
