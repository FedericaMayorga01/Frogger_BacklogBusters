from src.Object import Object

# Plataformas moviles en las partes de agua, permiten que la rana cruce
class Plataform(Object):
    def __init__(self,position,tronco,way):
        self.sprite = tronco
        self.position = position
        self.way = way

    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed
        elif self.way == "left":
            self.position[0] = self.position[0] - speed