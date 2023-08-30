import doctest
class Matrix:
    """Класс матрица для сложения, сравнения умножения и вывода на печать!
    >>> matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> print(matrix_1)
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    <BLANKLINE>
    >>> matrix_2 = Matrix([[10, 9, 8], [8, 7, 6], [6, 5, 4]])
    >>> print(matrix_1 + matrix_2)
    [11, 11, 11]
    [12, 12, 12]
    [13, 13, 13]
    <BLANKLINE>
    >>> print(matrix_1 * matrix_2)
    [44, 38, 32]
    [116, 101, 86]
    [188, 164, 140]
    <BLANKLINE>
    >>> matrix_1 == matrix_2
    False
    >>> matrix_1 == Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> matrix_3 = Matrix([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
    >>> matrix_1 == matrix_3
    Traceback (most recent call last):
    ...
    ValueError: Матрицы разных размеров
    """

    def __init__(self, _my_matrix):
        """Инициализация класса"""
        self._my_matrix = _my_matrix  # _my_matrix так как мы хотим сравнивать изменяемый объект

    def __eq__(self, other):
        """Метод сравнивает матрицы"""
        if len(self._my_matrix) != len(other._my_matrix) or len(self._my_matrix[0]) != len(other._my_matrix[0]):
            raise ValueError("Матрицы разных размеров")
        else:
            for i in range(len(self._my_matrix)):
                for j in range(len(self._my_matrix[0])):
                    if self._my_matrix[i][j] != other._my_matrix[i][j]:
                        return False
            return True

    def __str__(self):
        """Метод  возвращает строковое представление объекта"""
        s = ''
        for i in range(len(self._my_matrix)):
            s += str(self._my_matrix[i]) + '\n'
        return s

    def __add__(self, other):
        """Метод сложения"""
        if len(self._my_matrix) != len(other._my_matrix) or len(self._my_matrix[0]) != len(other._my_matrix[0]):
            raise ValueError("Матрицы разных размеров")
        else:
            sum_matrix = list([] for _ in range(len(self._my_matrix)))

            for i in range(len(self._my_matrix)):
                for j in range(len(self._my_matrix[0])):
                    temp = self._my_matrix[i][j] + other._my_matrix[i][j]
                    sum_matrix[i].append(temp)
            return Matrix(sum_matrix)

    def __mul__(self, other):
        """Метод умножения"""
        if len(self._my_matrix) != len(other._my_matrix) or len(self._my_matrix[0]) != len(other._my_matrix[0]):
            raise ValueError("Матрицы разных размеров")
        else:
            mul_matrix = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._my_matrix)] for i_row in
                          self._my_matrix]
        return Matrix(mul_matrix)


if __name__ == '__main__':
    doctest.testmod(verbose=True)