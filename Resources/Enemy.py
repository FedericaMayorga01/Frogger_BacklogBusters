from Resources.Object import Object

# Los objetos que hacen perder a la rana
class Enemy(Object):
    def __init__(self,position,sprite_enemy,way,factor):
        # Visual que representa el enemigo
        self.sprite = sprite_enemy
        self.position = position
        # Direccion a la que tiene permitido moverse
        self.way = way
        # Factor para determinar la velocidad de movimiento
        self.factor = factor

    # Determina el movimiento y la velocidad del enemigo
    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed * self.factor
        elif self.way == "left":
            self.position[0] = self.position[0] - speed * self.factor