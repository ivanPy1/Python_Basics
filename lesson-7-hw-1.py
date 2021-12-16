# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, matrix_data):
        self.matrix = matrix_data

    def __str__(self):
        for matrix_str in self.matrix:
            result_matrix = '\n'.join('   '.join(map(str, row)) for row in self.matrix)
            return result_matrix

    def __add__(self, other):

        new_matrix_data = self.matrix.copy()
        for matrix_str in range(0, len(self.matrix)):
            for m_column in range(0, len(self.matrix[matrix_str])):
                new_matrix_data[matrix_str][m_column] += other.matrix[matrix_str][m_column]
        return Matrix(new_matrix_data)


first_matrix = Matrix([[31, 22, 16], [37, 43, 19], [51, 86, 59]])
second_matrix = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])

print(f'Первая матрица: ' + '\n' + str(first_matrix))
print(f'Вторая матрица: ' + '\n' + str(second_matrix))
print(f'Сумма первой и второй матрицы: ' + '\n' + str(first_matrix + second_matrix))
