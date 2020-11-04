class Data:
    data_string = None

    def __init__(self, data_string):
        self.data_string = str(data_string)

    @classmethod
    def data_out(cls):
        data_ = [el for el in MyData.data_string.split() if el.isdigit()]
        return data_

    @staticmethod
    def validing():
        data_ = [el for el in MyData.data_string.split() if el.isdigit()]
        if int(data_[0]) > 31:
            print('День введен неверно')
        elif int(data_[1]) > 12:
            print('Месяц введен неверно ')
        elif int(data_[2]) > 2021:
            print('Год введен неверно')
        else:
            print(MyData.data_string)


MyData = Data('23 - 12 - 2004')
print(MyData.data_out())
MyData.validing()
