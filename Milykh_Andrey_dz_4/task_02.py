"""
Напишите функцию для транспонирования матрицы.

Пояснения:
Матрица - это список, содержащий списки.
Транспонирование - замена строк столбцами.
"""


def transpose_matrix(matrix_):
    matrix_rows = len(matrix_)
    matrix_columns = len(matrix_[0])
    matrix_rows, matrix_columns = matrix_columns, matrix_rows

    trans_matrix = []
    for i in range(matrix_rows):
        trans_matrix.append([0] * matrix_columns)

    for i in range(matrix_columns):
        for j in range(matrix_rows):
            trans_matrix[j][i] = matrix_[i][j]
    return trans_matrix


def transpose_zip(matrix_):
    zipped_rows = zip(*matrix_)
    trans_matrix = []
    for row in zipped_rows:
        trans_matrix.append(list(row))
    return trans_matrix


matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
res = transpose_matrix(matrix)
print(res)
res = transpose_zip(matrix)
print(res)
