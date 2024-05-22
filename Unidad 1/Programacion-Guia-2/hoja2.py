matrix1 = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]      
matrix2 = [
        [9, 8, 7], 
        [6, 5, 4], 
        [3, 2, 1]]
def multmatrix(matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
                suma = 0
                fil2 = 0
                col2 = 0
                for j in range(len(matrix1)):
                        suma = suma + matrix1[i][j] * matrix2[fil2][col2]
                        fil2 += 1
                result.append(suma)
        return result
print(multmatrix(matrix1, matrix2))
