from diseñoObserver.Sujeto import Sujeto
from src.Object import Object
import random

class Potenciador(Object, Sujeto):
    def __init__(self, sprite):
        self.sprite = sprite
        # Tiempo en una posicion del potenciador
        self.timer = 0
        # Cuanto tiempo va a estar activo el potenciador
        self.active_timer = 0
        # Estado del potenciador
        self.isActive = False
        # Inicializamos la posición del potenciador
        position = [random.randint(0, 420), random.randint(240, 445)]
        Object.__init__(self, position, sprite)
        Sujeto.__init__(self)

    def reset_position(self):
        # Reseteamos la posicón del potenciador
        self.position = [random.randint(0, 420), random.randint(240, 445)]

    def disappear(self):
        # Hace desaparecer el potenciador
        self.position = [-100, -100]

    def activar(self):
        self.active_timer = 200
        self.disappear()
        self.isActive = True

        self.notify_observers()

    def desactivar(self):
        self.isActive = False

        self.notify_observers()