class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix_data])

    def __add__(self, other):
        if len(self.matrix_data) != len(other.matrix_data) or len(self.matrix_data[0]) != len(other.matrix_data[0]):
            return "Матрицы разных размеров нельзя складывать"
        else:
            result_matrix = []
            for i in range(len(self.matrix_data)):
                row = []
                for j in range(len(self.matrix_data[0])):
                    row.append(self.matrix_data[i][j] + other.matrix_data[i][j])
                result_matrix.append(row)
            return Matrix(result_matrix)


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])


print("Матрица 1:")
print(matrix1)
print("Матрица 2:")
print(matrix2)


print("Результат сложения матриц:")
print(matrix1 + matrix2)