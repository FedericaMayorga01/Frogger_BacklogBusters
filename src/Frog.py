import pygame
from pygame.locals import *
from src.Global import Global as glb
from src.Object import Object

# Personaje principal
class Frog(Object):
    def __init__(self,position,animacion):      # Los mismos parametros que object, sumando la animacion
        self.sprite = animacion
        self.position = position
        self.vidas = 3                          # Define cantidad de vidas
        self.animation_counter = 0              # Se utiliza para determinar qué cuadro de la animación se debe mostrar en un momento dado
        self.animation_tick = 1                 # velocidad de la animación, funciona como temporizador para saber cuadno actualizar la imagen
        self.way = "UP"
        self.can_move = 1

    # Animaciones de movimiento
    def cambiar_animacion(self,key_pressed):
        if self.way != key_pressed:
            self.way = key_pressed
            # Si la dirección es hacia arriba
    
            if self.way == "up":
                moves_directorio = './res/img/sprite_sheets_up.png' 
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()
            # Si la dirección es hacia abajo
            elif self.way == "down":
                moves_directorio = './res/img/sprite_sheets_down.png'
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()
            # Si la dirección es hacia la izquierda
            elif self.way == "left":
                moves_directorio = './res/img/sprite_sheets_left.png'
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()
            # Si la dirección es hacia la derecha
            elif self.way == "right":
                moves_directorio = './res/img/sprite_sheets_right.png'
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()

    # Movimientos del personaje
    def mover_rana(self,key_pressed, key_up):
    # TODO:     Aún necesitamos manejar los límites de la pantalla
    #           El movimiento horizontal aún no está correcto
        # Si el contador esta en cero, la animacion debe cambiar segun a donde se movio
        if self.animation_counter == 0 :
            # LLama al metodo para cargar la prox animacion
            self.cambiar_animacion(key_pressed)
        self.prox_animacion()
        # Identifica que tecla fue presionada y hacia donde moverse, sin salirse de pantalla
        if key_up == 1:
            if key_pressed == "up":
                if self.position[1] > 39:
                    self.position[1] = self.position[1]-13
            elif key_pressed == "down":
                if self.position[1] < 473:
                    self.position[1] = self.position[1]+13
            if key_pressed == "left":
                if self.position[0] > 2:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]-13
                    else:
                        self.position[0] = self.position[0]-14
            elif key_pressed == "right":
                if self.position[0] < 401:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]+13
                    else:
                        self.position[0] = self.position[0]+14

    # Controla los contadores de animaciones
    def animateFrog(self,key_pressed,key_up):
        # Si no esta en su estado inicial
        if self.animation_counter != 0 :
            # Verifica si es momento de cambiar de animacion
            if self.animation_tick <= 0 :
                self.mover_rana(key_pressed,key_up)
                self.animation_tick = 1
            else :
                self.animation_tick = self.animation_tick - 1

    # Establece la posicion
    def setPos(self,position):
        self.position = position

    # Disminuye las vidas
    def perder_vida(self):
        self.vidas = self.vidas - 1

    # Establece la incapacidad de movimeinto de la rana
    def cannotMove(self):
        self.can_move = 0

    # Incrementa el contador para pasar a la proxima animacion
    def prox_animacion(self):
        self.animation_counter = self.animation_counter + 1
        # Si alcanza el limite de animaciones, se reinicia
        if self.animation_counter == 3 :
            self.animation_counter = 0
            self.can_move = 1

    # Cuando se pierde, se reinician los valores
    def frogDead(self,game):
        self.setPos_inicial()
        self.perder_vida()
        game.resetTime()
        self.animation_counter = 0
        self.animation_tick = 1
        self.way = "UP"
        self.can_move = 1

    # Establece la posicion inicial, centrada
    def setPos_inicial(self):
        self.position = [207, 475]

    # Dibuja al personaje en la posicion y animacion indicada
    def draw(self):
        animacion_actual = self.animation_counter * 30
        glb.screen.blit(self.sprite, (self.position),(0 + animacion_actual, 0, 30, 30 + animacion_actual))

    # Determina en un rectangulo el area ocupada por la rana
    def rect(self):
        return Rect(self.position[0],self.position[1],30,30)