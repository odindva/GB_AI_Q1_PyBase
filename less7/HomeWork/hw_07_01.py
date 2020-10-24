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


class Matrix:
    def __init__(self, array_of_arrays):
        self.array_of_arrays = array_of_arrays

    def __str__(self):
        s = ''
        for array in self.array_of_arrays:
            for i in array:
                s += f'{i: 8}'
            s += '\n'
        return s

    def __add__(self, other):
        result = self
        for i in range(len(self.array_of_arrays)):
            for j in range(len(self.array_of_arrays[0])):
                result.array_of_arrays[i][j] += other.array_of_arrays[i][j]
        return result


if __name__ == '__main__':
    a = Matrix([[1, 2], [3, 4], [5, 6]])
    b = Matrix([[1, 2], [3, 4], [5, 6]])
    print(a)
    print(b)
    print(a + b)
