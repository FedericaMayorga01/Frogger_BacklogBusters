from diseñoObserver.Observer import Observer
import pygame

# Directorios de las imagenes de fondo
fondo_directorio = './res/img/bg.png'
fondo_special_directorio = './res/img/bg_special.png'

class Global(Observer):
    screen = pygame.display.set_mode((448, 546), 0, 32)  # Crea la ventana de juego

    def __init__(self):
        self.fondo = pygame.image.load(fondo_directorio).convert()
        pass
    def update(self, sujeto):
        if sujeto.isActive:
            self.fondo= pygame.image.load(fondo_special_directorio).convert()
        else:
            self.fondo = pygame.image.load(fondo_directorio).convert()
        self.screen.blit(self.fondo, (0, 0))

    def setScreen(self):
        self.screen.blit(self.fondo, (0, 0))

    def setFondo(self):
        self.fondo = pygame.image.load(fondo_directorio).convert()

    def setText(self, text,  position):
        self.screen.blit(text, position)
