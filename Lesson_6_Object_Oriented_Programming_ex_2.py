class Road:
    def __init__(self, _length, _width,  massa_per_meter, thickness):
        self._length = _length
        self._width = _width
        print(f'{int((self._length * self._width * massa_per_meter * thickness) / 1000)} т.')


asphalt_area = Road(20, 5000, 25, 5)
