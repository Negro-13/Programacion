matrix1 =  [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]
matrix2 =  [[9, 8, 7], 
            [6, 5, 4], 
            [3, 2, 1]]

def summatrix(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            matrix1[i][j] += matrix2[i][j] 
    return matrix1
print(summatrix(matrix1, matrix2))