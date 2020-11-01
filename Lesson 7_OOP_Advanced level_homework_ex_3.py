class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return self.quantity - other.quantity
        else:
            print('Разность количества ячеек клеток должна быть больше нуля')

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return round(self.quantity / other.quantity)

    def make_order(self, quantity_1):
        for i in range(0, int(self.quantity / quantity_1)):
            string_ = ['*' * quantity_1, ' \n ']
            print(string_[0])
            # if i == quantity_1:
            #     string_.append(' \n ')


try:
    cell = Cell(200)
    cell_1 = Cell(2)
    print(cell * cell_1)
    cell.make_order(5)
except TypeError:
    print('Вы ввели нечисловое значение')
except NameError:
    print('Вы ввели неправильное значение')