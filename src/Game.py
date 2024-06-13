from diseñoObserver.Observer import Observer
from src.Potenciador import Potenciador


# Estado del juego
class Game(Observer):
    def __init__(self, speed, level):
        self.speed = speed
        self.base_speed = speed
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
        self.base_speed = self.speed + 1

    # Incrementa los puntos
    def incPoints(self,points):
        self.points = self.points + points

    # Decrementa el tiempo restante de juego
    def decTime(self):
        self.time = self.time - 1

    # Restablece el tiempo
    def resetTime(self):
        self.time = 30

    def scale_speed(self,prescaler):
        self.speed *= prescaler

    def reset_speed(self):
        self.speed = self.base_speed

    def update(self, sujeto):
        # Chequeamos que el Sujeto sea un Potenciador, porque podemos estar observando otros Sujetos
        if isinstance(sujeto, Potenciador):
            if sujeto.isActive:
                self.scale_speed(0.5)
            else:
                self.reset_speed()