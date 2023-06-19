def transpose_matrix(matrix):
    # задаемем размер матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    # создаем новую матрицу
    transposed_matrix = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(cols):
        for j in range(rows):
            transposed_matrix[i][j] = matrix[j][i]

    return transposed_matrix



# для проверки
#    matrix = [
#        [1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]
#    ]
#    transposed = transpose_matrix(matrix)
#    print(transposed)