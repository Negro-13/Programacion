matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def multmatrix(matrix1, matrix2):
    resultado = []
    for fil in range(len(matrix1)):
        resultado.append([])
        for col in range(len(matrix1)):
            suma = 0
            for mult in range(len(matrix1)):
                suma += matrix1[fil][mult] * matrix2[mult][col]
            resultado[fil].append(suma)
    return resultado

print(multmatrix(matrix1, matrix2))