import pygame
from src.Global import Global  # Import the global screen variable

class Potenciador:
    def __init__(self, position, animation):
        self.position = position
        self.animation = animation
        self.visible = True

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.animation.get_width(), self.animation.get_height())

    def draw(self):
        if self.visible:
            Global.screen.blit(self.animation, self.position)