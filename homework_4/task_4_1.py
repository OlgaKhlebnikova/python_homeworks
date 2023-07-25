"""Напишите функцию для транспонирования матрицы"""

def transpose(matrix_1):
    trans_matrix = [[0 for j in range(len(matrix_1))] for i in range(len(matrix_1[0]))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            trans_matrix[j][i] = matrix_1[i][j]
    return trans_matrix

matrix = [[2,3],[7,8],[9,6]]
print(f"Исходная матрица{matrix}\nТранспонированная матрица {transpose(matrix)}")

# Для красивого вывода
print(f"Исходная матрица:")

for i in range(0, len(matrix)):
    for i2 in range(0, len(matrix[i])):
        print(matrix[i][i2], end=' ')
    print()
new_matrix = transpose(matrix)
print(f"Транспонированная матрица:")
for i in range(0, len(new_matrix)):
    for i2 in range(0, len(new_matrix[i])):
        print(new_matrix[i][i2], end=' ')
    print()