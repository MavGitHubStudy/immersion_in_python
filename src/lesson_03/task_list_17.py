import copy

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, id(matrix), new_m, id(new_m), sep='\n')
# matrix[0][1] = 555
# print(matrix, id(matrix), new_m, id(new_m), sep='\n')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, id(matrix), new_m, id(new_m), sep='\n')
matrix[0][1] = 555
print(matrix, id(matrix), new_m, id(new_m), sep='\n')
