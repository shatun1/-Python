class Road:
    def __init__(self, _length, _width, thickness):
        self._length = _length
        self._width = _width
        self.thickness = thickness


    def massa_per_meter(self):
        mass_per_meter = 0.01 * self.thickness
        massa = self._length * self._width * mass_per_meter * self.thickness
        return massa


asphalt_mass = Road(20, 5000, 5)
print(f'{int(asphalt_mass.massa_per_meter())} т.')