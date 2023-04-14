class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass = 25
        self._thickness = 0.05

    def calculate_asphalt_mass(self):
        asphalt_mass = self._length * self._width * self._mass * self._thickness
        return asphalt_mass / 1000


road = Road(20, 5000)


asphalt_mass = road.calculate_asphalt_mass()

print(f"Масса асфальта для покрытия всего дорожного полотна: {asphalt_mass} т")