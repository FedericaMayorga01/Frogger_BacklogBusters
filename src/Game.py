# Estado del juego
class Game():
    def __init__(self,speed,level):
        self.speed = speed
        self.original_speed = speed
        self.level = level
        self.points = 0
        self.time = 30
        self.gameInit = 0
        self.potenciador_active = False

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

    def start_bonus(self, duration):
        self.bonus_timer = duration
        self.original_speed = self.speed
        self.speed *= 0.9  # Reduce the game speed by 10%

    def update(self):
        if self.bonus_timer > 0:
            self.bonus_timer -= 1
            if self.bonus_timer == 0:
                self.speed = self.original_speed  # Restore the original speed