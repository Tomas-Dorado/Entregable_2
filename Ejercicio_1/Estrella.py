import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"(Las coordenadas son: {self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Alfa"
        elif self.x < 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Beta"
        elif self.x < 0 and self.y < 0 and self.z >= 0:
            return "Galaxia Gamma"
        elif self.x >= 0 and self.y < 0 and self.z >= 0:
            return "Galaxia Delta"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        return math.sqrt(
            (self.x - otra_estrella.x) ** 2 +
            (self.y - otra_estrella.y) ** 2 +
            (self.z - otra_estrella.z) ** 2
        )