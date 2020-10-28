# 1) Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from copy import deepcopy


class Matrix:
    loyal_regime = True

    def __init__(self, matrix, is_original=True):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = max([len(x) if x else 0 for x in matrix])
        if is_original:
            self.matrix = self.normal(self.rows, self.cols).matrix
            for row in range(self.rows):
                for col in range(self.cols):
                    self.matrix[row][col] = int(self.matrix[row][col])

    def __str__(self):
        print('matrix:')  # добавил подобные принты, чтобы не плутать на выводе
        s = ''
        for array in self.matrix:
            for i in array:
                s += f'{i: 8}'
            s += '\n'
        return s

    def normal(self, rows, cols):
        result = self.copy()
        for i in range(rows - len(result.matrix)):
            result.matrix.append([0 for _ in range(cols)])
        for row in range(rows):
            for col in range(cols - len(result.matrix[row])):
                result.matrix[row].append(0)
        return result

    def copy(self):
        return Matrix(deepcopy(self.matrix), is_original=False)

    def __add__(self, other):
        print('add', end='-')
        if Matrix.loyal_regime:
            result = self.normal(max(self.rows, other.rows), max(self.cols, other.cols))
            other = other.normal(max(self.rows, other.rows), max(self.cols, other.cols))
        else:
            if self.rows != other.rows or self.cols != other.cols:
                print('Error')
                return None
            result = self.copy()
        for i in range(len(result.matrix)):
            for j in range(len(result.matrix[0])):
                result.matrix[i][j] += other.matrix[i][j]
        return result

    def __sub__(self, other):
        print('sub', end='-')
        if Matrix.loyal_regime:
            result = self.normal(max(self.rows, other.rows), max(self.cols, other.cols))
            other = other.normal(max(self.rows, other.rows), max(self.cols, other.cols))
        else:
            if self.rows != other.rows or self.cols != other.cols:
                print('Error')
                return None
            result = self.copy()
        for i in range(len(result.matrix)):
            for j in range(len(result.matrix[0])):
                result.matrix[i][j] -= other.matrix[i][j]
        return result

    def __mul__(self, other):
        print('mul', end='-')
        if self.rows != other.cols or self.cols != other.rows:
            print('Error')
            return None
        result = Matrix([[0]]).normal(self.rows, self.rows)
        for row in range(self.rows):
            for col in range(self.rows):
                local_p = 0
                for i in range(self.cols):
                    local_p += self.matrix[row][i] * other.matrix[i][col]
                result.matrix[row][col] = local_p
        return result


if __name__ == '__main__':
    a = Matrix([[1, 2, 7], [3, 4], [5, '6']])
    b = Matrix([[1, 2], [3, 4], ['5', 6]])
    с = Matrix([[1, 2], [], [5, 6], [8]])
    print(a)
    print(b)
    print(с)
    print(a + b + с)
    print(a + b - с)
    print(a)
    print(b)
    print(с)
    print()
    a = Matrix([[1, 2, 7], [3, 4, 5]])
    b = Matrix([[1, 2], [3, 4], ['5', 6]])
    print(a)
    print(b)
    print(a * b)
    print(b * a)

    print('non loyal regime:')
    print()
    Matrix.loyal_regime = False
    a = Matrix([[1, 2, 7], [3, 4], [5, '6']])
    b = Matrix([[1, 2], [3, 4]])
    print(a)
    print(b)
    print(a + b)
