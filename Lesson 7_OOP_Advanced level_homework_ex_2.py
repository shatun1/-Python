from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h


class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)

    @abstractmethod
    def coat_rate(self):
        pass


class Costume(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)

    @abstractmethod
    def costume_rate(self):
        pass


class SumRateClothes(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)

    @property
    def coat_rate(self):
        rate_coat = round(self.v/6.5 + 0.5)
        print(f'Затраты на пошив пальто:{rate_coat}')
        return rate_coat

    @property
    def costume_rate(self):
        rate_costume = round(2 * self.h + 0.3)
        print(f'Затраты на пошив костюма:{rate_costume}')
        return rate_costume


clothes_a = SumRateClothes(14, 15)
print(f'Общие затраты на пошив костюма и пальто:{clothes_a.coat_rate + clothes_a.costume_rate}')
