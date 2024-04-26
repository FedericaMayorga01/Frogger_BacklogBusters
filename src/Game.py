# Estado del juego
class Game():
    def __init__(self,speed,level):
        self.speed = speed
        self.level = level
        self.points = 0
        self.time = 30
        self.gameInit = 0

    # Incrementa el nivel
    def incLevel(self):
        self.level = self.level + 1

    # Incrementa la velocidad
    def incSpeed(self):
        self.speed = self.speed + 1

    # Incrementa los puntos
    def incPoints(self,points):
        self.points = self.points + points

    # Decrementa el tiempo restante de juego
    def decTime(self):
        self.time = self.time - 1

    # Restablece el tiempo
    def resetTime(self):
        self.time = 30