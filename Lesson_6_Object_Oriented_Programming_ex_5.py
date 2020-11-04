class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title}(a) '

    def pen_info(self):
        return self.title


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}(и) '
    def Pencil_info(self):
        return self.title


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}(а) '
    def Handle_info(self):
        return self.title


Pen_ = Pen('Карандаш')
print(Pen_.pen_info(), " , ", Pen_.draw())
Pencil_ = Pencil('Ручка')
print(Pencil_.Pencil_info(), ' , ', Pencil_.draw())
Handle_ = Handle('Маркер')
print(Handle_.Handle_info(), ' , ', Handle_.draw())
