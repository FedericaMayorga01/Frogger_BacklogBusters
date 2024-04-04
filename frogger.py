#! /usr/bin/env python
import pygame
import random as Random
from pygame.locals import *
from sys import exit


pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 32, 2, 4096)  #Configuracion de sonido

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
info_font = pygame.font.SysFont(font_name, 24)
menu_font = pygame.font.SysFont(font_name, 36)

screen = pygame.display.set_mode((448,546), 0, 32) #Crea la ventana de juego

# --- IMAGENES  ----------------------------------------------
#Cargar los nombres de las imagenes a usar:
fondo_directorio = './images/bg.png'
moves_directorio = './images/sprite_sheets_up.png'
rana_directorio = './images/frog_arrived.png'
auto1_directorio = './images/car1.png'
auto2_directorio = './images/car2.png'
auto3_directorio = './images/car3.png'
auto4_directorio = './images/car4.png'
auto5_directorio = './images/car5.png'
tronco_directorio = './images/tronco.png'

#Convertir las imagenes en objetos dinamicos
fondo = pygame.image.load(fondo_directorio).convert()
animacion = pygame.image.load(moves_directorio).convert_alpha()
rana = pygame.image.load(rana_directorio).convert_alpha()
auto1 = pygame.image.load(auto1_directorio).convert_alpha()
auto2 = pygame.image.load(auto2_directorio).convert_alpha()
auto3 = pygame.image.load(auto3_directorio).convert_alpha()
auto4 = pygame.image.load(auto4_directorio).convert_alpha()
auto5 = pygame.image.load(auto5_directorio).convert_alpha()
tronco = pygame.image.load(tronco_directorio).convert_alpha()

# --- SONIDO --------------------------------------------------
musica_perder = pygame.mixer.Sound('./sounds/boom.wav')
musica_agua = pygame.mixer.Sound('./sounds/agua.wav')
musica_exito = pygame.mixer.Sound('./sounds/success.wav')
musica_fondo = pygame.mixer.Sound('./sounds/guimo.wav')

pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()


class Object():
    def __init__(self,position,sprite):  #Inicializador del objeto, con su posicion y dibujo(sprite)
        self.sprite = sprite
        self.position = position

    def draw(self):
        screen.blit(self.sprite,(self.position))

    def rect(self):
        return Rect(self.position[0],self.position[1],self.sprite.get_width(),self.sprite.get_height())

#Personaje principal
class Frog(Object):
    def __init__(self,position,animacion): #Los mismos parametros que object, sumando la animacion
        self.sprite = animacion
        self.position = position
        self.vidas = 3 #define cantidad de vidas
        self.animation_counter = 0 # se utiliza para determinar qué cuadro de la animación se debe mostrar en un momento dado
        self.animation_tick = 1 #velocidad de la animación, funciona como temporizador para saber cuadno actualizar la imagen
        self.way = "UP"
        self.can_move = 1

    #Animaciones de movimiento
    def cambiar_animacion(self,key_pressed):
        if self.way != key_pressed:
            self.way = key_pressed
            if self.way == "up": # Si la dirección es hacia arriba
                moves_directorio = './images/sprite_sheets_up.png'
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()
            elif self.way == "down": # Si la dirección es hacia abajo
                moves_directorio = './images/sprite_sheets_down.png'
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()
            elif self.way == "left": # Si la dirección es hacia la izquierda
                moves_directorio = './images/sprite_sheets_left.png'
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()
            elif self.way == "right": # Si la dirección es hacia la derecha
                moves_directorio = './images/sprite_sheets_right.png'
                self.sprite = pygame.image.load(moves_directorio).convert_alpha()

    #Movimientos del personaje
    def mover_rana(self,key_pressed, key_up):
       # Aún necesitamos manejar los límites de la pantalla
       # El movimiento horizontal aún no está correcto
        if self.animation_counter == 0 : #Si el contador esta en cero, la animacion debe cambiar segun a donde se movio
            self.cambiar_animacion(key_pressed) #Lamma al metodo para cargar la prox animacion 
        self.prox_animacion()
        if key_up == 1: #identifica que tecla fue presionada y hacia donde moverse, sin salirse de pantalla
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

    #Controlar los contadores de animaciones
    def animateFrog(self,key_pressed,key_up):
        if self.animation_counter != 0 :    #si no esta en su estado inicial
            if self.animation_tick <= 0 :   #verifica si es momento de cambiar de animacion
                self.mover_rana(key_pressed,key_up)
                self.animation_tick = 1
            else :
                self.animation_tick = self.animation_tick - 1

    #Establecer posicion
    def setPos(self,position):
        self.position = position

    #Disminuye vidas
    def perder_vida(self):
        self.vidas = self.vidas - 1

    #Establece la incapacidad de movimeinto de la rana
    def cannotMove(self):
        self.can_move = 0

    #Incrementa el contador para pasar a la proxima animacion
    def prox_animacion(self):
        self.animation_counter = self.animation_counter + 1
        if self.animation_counter == 3 :  #si alcanza el limite de animaciones se reinicia
            self.animation_counter = 0
            self.can_move = 1

    #Perder, reinicia los valores
    def frogDead(self,game): 
        self.setPos_inicial() 
        self.perder_vida()
        game.resetTime()
        self.animation_counter = 0
        self.animation_tick = 1
        self.way = "UP" 
        self.can_move = 1

    #Establece la posicion inicial, abajo al medio
    def setPos_inicial(self):
        self.position = [207, 475]

    #Dibujar al personaje en la posicion y animacion indicada
    def draw(self):
        animacion_actual = self.animation_counter * 30
        screen.blit(self.sprite,(self.position),(0 + animacion_actual, 0, 30, 30 + animacion_actual))

    #Determina en un rectangulo el area ocupada por la raana
    def rect(self):
        return Rect(self.position[0],self.position[1],30,30)

#Todo objeto que hace perder a la rana
class Enemy(Object):  
    def __init__(self,position,sprite_enemy,way,factor): 
        self.sprite = sprite_enemy #Visual que representa el enemigo
        self.position = position 
        self.way = way #Direccion a la que tiene permitido moverse 
        self.factor = factor #factor para determinar lavelocidad de movimiento

    #Determina el movimiento y la velocidad del enemigo
    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed * self.factor
        elif self.way == "left":
            self.position[0] = self.position[0] - speed * self.factor

#Plataformas moviles en las partes de agua, permiten a la rana cruzar
class Plataform(Object):
    def __init__(self,position,tronco,way):
        self.sprite = tronco
        self.position = position
        self.way = way

    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed
        elif self.way == "left":
            self.position[0] = self.position[0] - speed

#Estado del juego
class Game():
    def __init__(self,speed,level):
        self.speed = speed
        self.level = level
        self.points = 0
        self.time = 30
        self.gameInit = 0

    #Incrementar nivel
    def incLevel(self):
        self.level = self.level + 1

    #Incrementar velocidad
    def incSpeed(self):
        self.speed = self.speed + 1

    #Incrementar puntos
    def incPoints(self,points):
        self.points = self.points + points

    #Decrementar el tiempo restante de juego
    def decTime(self):
        self.time = self.time - 1

    #Restablecer tiempo
    def resetTime(self):
        self.time = 30


#---FUNCIONES GENERALES -------------------------------

#Dibujar en pantalla una lista de objetos
def drawList(list):
    for i in list:
        i.draw()

#Mover todos los elementos de la lista
def moveList(list,speed):
    for i in list:
        i.move(speed)

#Eliminar los enemigos que se pasan de los limites pantalla
def destroyEnemys(list):
    for i in list:
        if i.position[0] < -80:
            list.remove(i)
        elif i.position[0] > 516:
            list.remove(i)

#Eliminar las plataformas que se pasan de los limites pantalla
def destroyPlataforms(list):
    for i in list:
        if i.position[0] < -100:
            list.remove(i)
        elif i.position[0] > 448:
            list.remove(i)

#Inicializar enemigo
def createEnemys(list,enemys,game): #list=contaodres para controlar el tiempo entre la creacion de enemigos,
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:  # Si el contador llega a cero, crea un nuevo enemigo y reinicia el contador.
                #Enemigo tipo 1
                list[0] = (40*game.speed)/game.level
                position_init = [-55,436]
                enemy = Enemy(position_init,auto1,"right",1)
                enemys.append(enemy)
            elif i == 1: # Configuración del segundo tipo de enemigo.
                list[1] = (30*game.speed)/game.level
                position_init = [506, 397]
                enemy = Enemy(position_init,auto2,"left",2)
                enemys.append(enemy)
            elif i == 2:   # Configuración del tercer tipo de enemigo.
                list[2] = (40*game.speed)/game.level
                position_init = [-80, 357]
                enemy = Enemy(position_init,auto3,"right",2)
                enemys.append(enemy)
            elif i == 3: # Configuración del cuarto tipo de enemigo.
                list[3] = (30*game.speed)/game.level
                position_init = [516, 318]
                enemy = Enemy(position_init,auto4,"left",1)
                enemys.append(enemy)
            elif i == 4:  # Configuración del quinto tipo de enemigo.
                list[4] = (50*game.speed)/game.level
                position_init = [-56, 280]
                enemy = Enemy(position_init,auto5,"right",1)
                enemys.append(enemy)

#Agregar plataforma para saltar
def createPlataform(list,plataforms,game):
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:
                list[0] = (30*game.speed)/game.level
                position_init = [-100,200]
                plataform = Plataform(position_init,tronco,"right")
                plataforms.append(plataform)
            elif i == 1:
                list[1] = (30*game.speed)/game.level
                position_init = [448, 161]
                plataform = Plataform(position_init,tronco,"left")
                plataforms.append(plataform)
            elif i == 2:
                list[2] = (40*game.speed)/game.level
                position_init = [-100, 122]
                plataform = Plataform(position_init,tronco,"right")
                plataforms.append(plataform)
            elif i == 3:
                list[3] = (40*game.speed)/game.level
                position_init = [448, 83]
                plataform = Plataform(position_init,tronco,"left")
                plataforms.append(plataform)
            elif i == 4:
                list[4] = (20*game.speed)/game.level
                position_init = [-100, 44]
                plataform = Plataform(position_init,tronco,"right")
                plataforms.append(plataform)


#Comprueba si la rana chocó con algun enemigo
def rana_calle(frog,enemys,game):
    #Compara las areas con el metodo rect del los objetos y la rana
    for i in enemys:
        enemyRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(enemyRect):
            musica_perder.play()
            frog.frogDead(game)

#Confirma si la rana está sobre alguna plataforma cuandoo está en el lago
def rana_lago(frog,plataforms,game):
    #Si la rana esta sobre una plataforma, se debe mover con ella
    #Si la rana no esta sobre ninguna. se muere

    seguro = 0 #determina si estaa sobre alguna plataforma 
    wayPlataform = ""
    for i in plataforms:
        plataformRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(plataformRect):
            seguro = 1
            wayPlataform = i.way

    if seguro == 0: # Si la rana no está sobre ninguna plataforma
        musica_agua.play()
        frog.frogDead(game)

    elif seguro == 1: # Si la rana está sobre una plataforma
        if wayPlataform == "right":
            frog.position[0] = frog.position[0] + game.speed

        elif wayPlataform == "left":
            frog.position[0] = frog.position[0] - game.speed

#Comprueba si la rana llega a la zona de llegada y si lo hace, crea un marcador en esa posición
def frogArrived(frog,llegadas,game):
    if frog.position[0] > 33 and frog.position[0] < 53:
        position_init = [43,7]
        createArrived(frog,llegadas,game,position_init)

    elif frog.position[0] > 115 and frog.position[0] < 135:
        position_init = [125,7]
        createArrived(frog,llegadas,game,position_init)

    elif frog.position[0] > 197 and frog.position[0] < 217:
        position_init = [207,7]
        createArrived(frog,llegadas,game,position_init)

    elif frog.position[0] > 279 and frog.position[0] < 299:
        position_init = [289,7]
        createArrived(frog,llegadas,game,position_init)

    elif frog.position[0] > 361 and frog.position[0] < 381:
        position_init = [371,7]
        createArrived(frog,llegadas,game,position_init)

    else:
        frog.position[1] = 46
        frog.animation_counter = 0
        frog.animation_tick = 1
        frog.can_move = 1


def ubicacion_rana(frog):
    #Si esta en la carretera
    if frog.position[1] > 240 :
        rana_calle(frog,enemys,game)

    #Si llega al rio
    elif frog.position[1] < 240 and frog.position[1] > 40:
        rana_lago(frog,plataforms,game)

    #Si alcanzó la meta
    elif frog.position[1] < 40 :
        frogArrived(frog,llegadas,game)

#Llegada, termina el nivel
def createArrived(frog,llegadas,game,position_init):
    llegada_rana = Object(position_init,rana)
    llegadas.append(llegada_rana)
    musica_exito.play()
    frog.setPos_inicial() #Restablece la posicion inicial
    game.incPoints(10 + game.time)
    game.resetTime()
    frog.animation_counter = 0
    frog.animation_tick = 1
    frog.can_move = 1

#Proximo nivel
def nextLevel(llegadas,enemys,plataforms,frog,game):
    if len(llegadas) == 5:
        llegadas[:] = []
        frog.setPos_inicial()
        game.incLevel()
        game.incSpeed()
        game.incPoints(100)
        game.resetTime()


#---INICIALIZAR -------------------------------------------------------
musica_fondo.play(-1)
text_info = menu_font.render(('Presiona cualquier tecla para iniciar!'),1,(0,0,0))
gameInit = 0

#Inicializa el juego
while gameInit == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            gameInit = 1

     # Dibuja el fondo y el texto del menú en la pantalla
    screen.blit(fondo, (0, 0))
    screen.blit(text_info,(5,150))
    pygame.display.update()

#Luego de presionar alguna tecla
while True:
    gameInit = 1
    game = Game(3,1) #Velocidad y nivel inicial
    key_up = 1
    frog_initial_position = [207,475]
    frog = Frog(frog_initial_position,animacion)

    enemys = []
    plataforms = []
    llegadas = []
    #30 ticks == 1 segundo
    ticks_enemys = [30, 0, 30, 0, 60] #Frecuencia de los enemigos
    ticks_plataforms = [0, 0, 30, 30, 30] #Frecuencia de las plataformas
    ticks_time = 30
    pressed_keys = 0
    key_pressed = 0

    #Ciclo principal de juego
    while frog.vidas > 0:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit() #Si se cierra la ventana terminar juego
            if event.type == KEYUP:
                key_up = 1 #Tecla dejada de presionar
            if event.type == KEYDOWN: 
                if key_up == 1 and frog.can_move == 1 : #Tecla presionada
                    key_pressed = pygame.key.name(event.key)
                    frog.mover_rana(key_pressed,key_up)
                    frog.cannotMove()

        #Tiempo de vida de la rana
        if not ticks_time:
            ticks_time = 30
            game.decTime()
        else:
            ticks_time -= 1

        if game.time == 0:
            frog.frogDead(game)

        #Agregar elementos extra    
        createEnemys(ticks_enemys,enemys,game)
        createPlataform(ticks_plataforms,plataforms,game)

        #Mueve los extras
        moveList(enemys,game.speed)
        moveList(plataforms,game.speed)

        ubicacion_rana(frog)

        nextLevel(llegadas,enemys,plataforms,frog,game)

        #Informacion sobre el jeugo en pantalla
        text_info1 = info_font.render(('Nivel: {0}               Puntos: {1}'.format(game.level,game.points)),1,(255,255,255))
        text_info2 = info_font.render(('Tiempo: {0}           Vidas: {1}'.format(game.time,frog.vidas)),1,(255,255,255))
        screen.blit(fondo, (0, 0))
        screen.blit(text_info1,(10,520))
        screen.blit(text_info2,(250,520))

        #Dibuja extras
        drawList(enemys)
        drawList(plataforms)
        drawList(llegadas)

        #Movimientos y animaciones de rana
        frog.animateFrog(key_pressed,key_up)
        frog.draw()

        #Destruye enemigos que salen de pantalla
        destroyEnemys(enemys)
        destroyPlataforms(plataforms)

        pygame.display.update()
        time_passed = clock.tick(30)

    #En caso de perder las tres vidas
    while gameInit == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                gameInit = 0

        screen.blit(fondo, (0, 0))
        text = game_font.render('GAME OVER', 1, (255, 0, 0))
        text_points = game_font.render(('Puntuacion: {0}'.format(game.points)),1,(255,0,0))
        text_reiniciar = info_font.render('Presione cualquier tecla para reiniciar!',1,(255,0,0))
        screen.blit(text, (75, 120))
        screen.blit(text_points,(10,170))
        screen.blit(text_reiniciar,(70,250))

        pygame.display.update()
