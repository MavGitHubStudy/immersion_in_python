def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data= }')  # Для демонстрации работы, но не для привычки
    # печатать из функции


my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')
"""
In main my_list = [2, 4, 6, 8]
In func data= [3, 5, 7, 9]
my_list = [3, 5, 7, 9]	new_list = None

Process finished with exit code 0
"""