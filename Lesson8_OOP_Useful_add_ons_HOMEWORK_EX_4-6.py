class StoreMashines:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.office = []
        self.undefined = []

    @property
    def filling(self):
        unit_characteristic = {'Название устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
        self.undefined.append(unit_characteristic)
        while True:
            unit_name = input('Введите название техники')
            try:
                unit_price = input('Введите цену')
                unit_quantity = input('Введите количество техники')
                if not unit_quantity.isdigit() or not unit_price.isdigit():
                    raise OwnError("Количество техники и(или) цена должны быть числовыми значениями")
            except (ValueError, OwnError) as err:
                print(err)
                continue
            unit_characteristic = {'Название устройства': unit_name, 'Цена за ед': unit_price, 'Количество': unit_quantity}
            control = input('Куда вы хотите отнести товар, в офис или на склад? Введите q чтобы выйти.').lower()
            if control == 'в офис':
                self.office.append(unit_characteristic)
            if control == 'на склад':
                self.my_store_full.append(unit_characteristic)
            if control == 'q':
                self.undefined.append(unit_characteristic)
                result = f'Техника на складе : {self.my_store_full}; Техника в офисе: {self.office}; Неопределенная техника: {self.undefined}'
                return result



class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Printer(StoreMashines):
    def __init__(self, numb, material, quality, brand):
        super().__init__(numb, material, quality)
        printer_dict = {'Материал': material, 'Качество': quality, 'брэнд': brand, 'to print smth': f"{numb} 'times'"}
        print(f'Индивидуальные харрактеристики принтера: {printer_dict}')



class Scanner(StoreMashines):
    def __init__(self, numb, material, quality, brand):
        super().__init__(numb, material, quality)
        Scaner_dict = {'Материал': material, 'Качество': quality, 'брэнд': brand, 'to scan smth': f"{numb} 'times'"}
        print(f'Индивидуальные харрактеристики сканера: {Scaner_dict}')

class Copier(StoreMashines):
    def __init__(self, numb, material, quality, brand):
        super().__init__(numb, material, quality)
        Copier_dict = {'Материал': material, 'Качество': quality, 'брэнд': brand, 'to copy smth': f"{numb} 'times'"}
        print(f'Индивидуальные харрактеристики ксерокса: {Copier_dict}')

a = StoreMashines('Принтер', 20000, 200)
print(a.filling)
b = Printer(5, 'plastic', 'good', 'Nikon')
c = Scanner(2, 'plastic', 'middle', 'Samsung')
d = Copier(1, 'plastic', 'best', 'acer')

