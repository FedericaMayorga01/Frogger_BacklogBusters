from src.Object import Object
import random
from src.Global import Global as glb

class Potenciador(Object):
    def __init__(self, sprite):
        self.sprite = sprite
        # Tiempo en una posicion del potenciador
        self.timer = 0
        # Cuanto tiempo va a estar activo el potenciador
        self.active_timer = 0
        # Initialize the potenciador at a random position
        position = [random.randint(0, 420), random.randint(280, 445)]
        super().__init__(position, sprite)

    def reset_position(self):
        # Reset the position to a new random position
        self.position = [random.randint(0, 420), random.randint(280, 445)]

    def disappear(self):
        # Set the position to an off-screen location
        self.position = [-100, -100]
