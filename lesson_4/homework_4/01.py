# Транспонирование матрицы

# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и возвращает
# транспонированную матрицу.

matrix = [[1, 2], [3, 4]]


def transpose(matrix):
    res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return res


transposed_matrix = transpose(matrix)
print(transposed_matrix)
"""
<<<<<<< HEAD

# def transpose(matrix):
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])
#
#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]
#
#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]
#
#     return transposed

=======
>>>>>>> origin/master

"""