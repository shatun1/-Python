class ComplexNumber:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return f'Сумма :{self.number_1 + other.number_1, self.number_2 + other.number_2}'

    def __mul__(self, other):
        return f'Произведение :{self.number_1 * other.number_1, self.number_2 * other.number_2}'


ex_1 = ComplexNumber(2, -2)
ex_2 = ComplexNumber(4, 1)
print(ex_1 + ex_2)
print(ex_1 * ex_2)
