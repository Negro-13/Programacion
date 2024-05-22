matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 2]]
def multmatrix(matrix1, matrix2):
    result = 0
    for fil in range(len(matrix1)):
        for col in range(len(matrix1)):
            matrix1[i][j] = 0
            matrix1[i][j] += matrix1[fil][col] * matrix2[fil][col]
        return matrix1