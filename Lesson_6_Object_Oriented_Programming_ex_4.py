class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f'{self.speed} км/ч'


    def traffic(self):
        if int(self.speed) > 0:
            return 'Машина едет'
        else:
            return 'Машина стоит'

    def Go(self):
        return 'Машина едет'

    def Stop(self):
        return 'машина остановилась'

    def turn(self, direction):
        if direction == 'left' or direction == 'влево':
            return f'Машина поворачивает в {direction}'
        elif direction == 'right' or direction == 'вправо':
            return f'Машина поворачивает в {direction}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def car_info_1(self):
        return self.speed, self.color, self.name, self.is_police

    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Скорость = {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def car_info_2(self):
        return self.speed, self.color, self.name, self.is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def car_info_3(self):
        return self.speed, self.color, self.name, self.is_police

    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Скорость = {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def car_info_4(self):
        return self.speed, self.color, self.name, self.is_police


Nissan = TownCar('60', 'белая', 'volkswagen', False)
print('\n', Nissan.car_info_1(), " , ",  Nissan.show_speed(), " , ", Nissan.turn('влево'), " , ",  Nissan.traffic())
print('\n', Nissan.speed, '\n', Nissan.color, '\n', Nissan.name, '\n', Nissan.is_police)
Lamborghini = SportCar('200', 'желтая', 'Lamborghini', False)
print('\n', Lamborghini.car_info_2(), " , ",  Lamborghini.show_speed(), " , ", Lamborghini.turn('влево'), " , ",  Lamborghini.traffic())
print('\n', Lamborghini.speed, '\n', Lamborghini.color, '\n', Lamborghini.name, '\n', Lamborghini.is_police)
Kia = WorkCar('50', 'серая', 'Kia', False)
print('\n', Kia.car_info_3(), " , ",  Kia.show_speed(), " , ", Kia.turn('влево'), " , ",  Kia.traffic())
print('\n', Kia.speed, '\n', Kia.color, '\n', Kia.name, '\n', Kia.is_police)
Chevrolet = PoliceCar('180', 'черная', 'Chevrolet', 'True')
print('\n', Chevrolet.car_info_4(), " , ",  Chevrolet.show_speed(), " , ", Chevrolet.turn('влево'), " , ",  Chevrolet.traffic())
print('\n', Chevrolet.speed, '\n', Chevrolet.color, '\n', Chevrolet.name, '\n', Chevrolet.is_police)
