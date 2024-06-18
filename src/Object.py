from pygame.locals import *
from src.Global import Global as glb

class Object():
    def __init__(self,position,sprite):  #Inicializa el objeto, con su posicion y dibujo (sprite)
        self.sprite = sprite
        self.position = position

    def draw(self):
        glb.screen.blit(self.sprite,(self.position))

    def rect(self):
        return Rect(self.position[0],self.position[1],self.sprite.get_width(),self.sprite.get_height())