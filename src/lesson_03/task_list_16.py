# my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
# new_list = my_list
# print(my_list, id(my_list), new_list, id(new_list), sep='\n')
# my_list[2] = 555
# print(my_list, id(my_list), new_list, id(new_list), sep='\n')

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, id(my_list), new_list, id(new_list), sep='\n')
my_list[2] = 555
print(my_list, id(my_list), new_list, id(new_list), sep='\n')
