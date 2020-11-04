class Matrix:
    def __init__(self, matr):
        self.matr = matr
        # self.list_1 = list_1
        # self.list_2 = list_2

    def __add__(self, other):
        matr_sum_list = []

        for i in range(len(self.matr)):
            matr_sum_list.append([])
            for j in range(len(other.matr[i])):
                matr_sum_list[i].append(self.matr[i][j] + other.matr[i][j])

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr_sum_list]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))


list_1 = [[1, 2, 11], [2, 4, 3], [23, 0, 11]]
list_2 = [[57, 67, 2], [4, 53, 87], [4, 65, 12]]
matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)
print(f'Первая матрица:\n{matrix_1}\n{"*" * 100}.\nВторая матрица:\n{matrix_2}\n{"*" * 100}')
print(f'Сумма матриц:\n{matrix_1 + matrix_2}\n{"*" * 100}')
