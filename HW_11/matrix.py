#создайте класс Матрица.
#добавьте методы для: вывода на печать, сравнения, сложения, умножения.

from random import randint

class Matrix:
    def __init__(self, number_of_column, number_of_row):
        self.number_of_column = number_of_column
        self.number_of_row = number_of_row
        self.filled_matrix = [[] for i in range(number_of_row)]

    def fill_matrix_rnd(self):
        for i in range(self.number_of_row):
            for j in range(self.number_of_column):
                self.filled_matrix[i].append(randint(1, 100))
        return self.filled_matrix

    def fill_matrix_0(self):
        for i in range(self.number_of_row):
            for j in range(self.number_of_column):
                self.filled_matrix[i].append(0)
        return self.filled_matrix

    def __str__(self):
        return str(self.filled_matrix)

    def __repr__(self):
        return f"Class: {Matrix.__name__} (number_of_column={self.number_of_column}, number_of_row={self.number_of_row}, " \
               f"filled_matrix={self.filled_matrix})"

    def __add__(self, other):
        add_matrix = (Matrix(self.number_of_column, self.number_of_row))
        if self != other:
            return None
        else:
            for i in range(self.number_of_row):
                for j in range(self.number_of_column):
                    add_matrix.filled_matrix[i].append(self.filled_matrix[i][j] + other.filled_matrix[i][j])
            return add_matrix

    def __mul__(self, other):
        mul_matrix = (Matrix(self.number_of_column, self.number_of_row))
        mul_matrix.fill_matrix_0()
        for i in range(self.number_of_row):
            for j in range(other.number_of_column):
                for k in range(other.number_of_row):
                    mul_matrix.filled_matrix[i][j] += self.filled_matrix[i][k] * other.filled_matrix[k][j]
        return mul_matrix

    def __eq__(self, other):
        for i in range(self.number_of_row):
            for j in range(self.number_of_column):
                if self.filled_matrix[i][j] != other.filled_matrix[i][j]:
                    return False
        return True


if __name__ == '__main__':
    matrix1 = Matrix(3, 4)
    matrix1.fill_matrix_rnd()
    matrix2 = Matrix(3, 3)
    matrix2.fill_matrix_rnd()
    matrix4 = matrix1
    print(f"{matrix1=}")
    print(matrix2)
    print(matrix1 == matrix2)
    print(matrix1 == matrix4)
    matrix5 = matrix1 * matrix2
    print(matrix5)