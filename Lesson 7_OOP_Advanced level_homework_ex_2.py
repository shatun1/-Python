class Clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H


    @property
    def Coat_rate(self):
        rate_Coat = round(self.V/6.5 + 0.5)
        return rate_Coat


    @property
    def Costume(self):
        rate_Costume = round(2 * self.H + 0.3)
        return rate_Costume


    # def __add__(self, others):
    #     return self.Coat_rate + self.Costume

clothes_ = Clothes(14, 15)
print(clothes_.Coat_rate)
print(clothes_.Costume)
print(clothes_.Coat_rate + clothes_.Costume)

