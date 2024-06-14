from src.Frog import Frog
from src.Game import Game
from src.Global import Global
import pygame
from pygame.locals import *
from sys import exit
from FroggerGameLogic import FroggerGameLogic

# --- INICIALIZACION ------------------------------------------
pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 32, 2, 4096)  #Configuracion de sonido

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
info_font = pygame.font.SysFont(font_name, 24)
menu_font = pygame.font.SysFont(font_name, 36)

#screen = pygame.display.set_mode((448,546), 0, 32) #Crea la ventana de juego

# --- IMAGENES  ----------------------------------------------
# Carga los nombres de las imagenes a usar:
fondo_directorio = './res/img/bg.png'
moves_directorio = './res/img/sprite_sheets_up.png'
rana_directorio = './res/img/frog_arrived.png'
auto1_directorio = './res/img/car1.png'
auto2_directorio = './res/img/car2.png'
auto3_directorio = './res/img/car3.png'
auto4_directorio = './res/img/car4.png'
auto5_directorio = './res/img/car5.png'
tronco_directorio = './res/img/tronco.png'

# Convierte las imagenes en objetos dinamicos
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
musica_perder = pygame.mixer.Sound('./res/sounds/boom.wav')
musica_agua = pygame.mixer.Sound('./res/sounds/agua.wav')
musica_exito = pygame.mixer.Sound('./res/sounds/success.wav')
musica_fondo = pygame.mixer.Sound('./res/sounds/guimo.wav')

pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

#--- INICIALIZA EL JUEGO -------------------------------------
musica_fondo.play(-1)
text_info = menu_font.render(('Presiona cualquier tecla para iniciar!'), 1, (0, 0, 0))
gameInit = 0
function = FroggerGameLogic()

# Inicializa el juego
while gameInit == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            gameInit = 1

     # Dibuja el fondo y el texto del menú en la pantalla
    Global.screen.blit(fondo, (0, 0))
    Global.screen.blit(text_info, (5, 150))
    pygame.display.update()

# Luego de presionar alguna tecla
while True:
    gameInit = 1
    # Velocidad y nivel inicial
    game = Game(3, 1)
    key_up = 1
    frog_initial_position = [207, 475]
    frog = Frog(frog_initial_position, animacion)
    # Listas de enemigos, plataformas y llegadas en el juego
    enemys = []
    plataforms = []
    llegadas = []
    # 30 ticks == 1 segundo
    # Frecuencia de los enemigos
    ticks_enemys = [30, 0, 30, 0, 60] 
    # Frecuencia de las plataformas
    ticks_plataforms = [0, 0, 30, 30, 30] 
    ticks_time = 30
    pressed_keys = 0
    key_pressed = 0

    # Ciclo principal de juego
    while frog.vidas > 0:
        # Eventos del juego
        for event in pygame.event.get():
            if event.type == QUIT:
                # Si se cierra la ventana terminar juego
                exit() 
            if event.type == KEYUP:
                # Si se deja de presionar una tecla
                key_up = 1 
            if event.type == KEYDOWN: 
                #Si se presiona una tecla
                if key_up == 1 and frog.can_move == 1 : 
                    key_pressed = pygame.key.name(event.key)
                    frog.mover_rana(key_pressed, key_up)
                    frog.cannotMove()

        # Tiempo de vida de la rana
        if not ticks_time:
            ticks_time = 30
            game.decTime()
        else:
            ticks_time -= 1

        if game.time == 0:
            frog.frogDead(game)

        # Agrega elementos extra    
        function.createEnemys(ticks_enemys, enemys, game, auto1, auto2, auto3, auto4, auto5)
        function.createPlataform(ticks_plataforms, plataforms, game, tronco)

        # Mueve los elementos extra
        function.moveList(enemys, game.speed)
        function.moveList(plataforms, game.speed)

        function.ubicacion_rana(frog, enemys, plataforms, llegadas, game, musica_perder, musica_agua, musica_exito, rana)

        function.nextLevel(llegadas, frog, game)

        # Informacion sobre el juego en pantalla
        text_info1 = info_font.render(('Nivel: {0}               Puntos: {1}'.format(game.level, game.points)), 1, (255, 255, 255))
        text_info2 = info_font.render(('Tiempo: {0}           Vidas: {1}'.format(game.time, frog.vidas)), 1, (255, 255, 255))
        # Se dibuja el fondo y la informacion en pantalla
        Global.screen.blit(fondo, (0, 0))
        Global.screen.blit(text_info1, (10, 520))
        Global.screen.blit(text_info2, (250, 520))

        # Dibuja los elementos extras
        function.drawList(enemys)
        function.drawList(plataforms)
        function.drawList(llegadas)

        # Movimientos y animaciones de la rana
        frog.animateFrog(key_pressed,key_up)
        frog.draw()

        # Destruye los elementos extra que salen de pantalla
        function.destroyEnemys(enemys)
        function.destroyPlataforms(plataforms)

        pygame.display.update()
        time_passed = clock.tick(30)

    # En caso de perder las tres vidas
    while gameInit == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                gameInit = 0

        Global.screen.blit(fondo, (0, 0))
        # Define los textos de la pantalla
        text = game_font.render('GAME OVER', 1, (255, 0, 0))
        text_points = game_font.render(('Puntuacion: {0}'.format(game.points)), 1, (255, 0, 0))
        text_reiniciar = info_font.render('Presione cualquier tecla para reiniciar!', 1, (255, 0, 0))
        # Se dibuja el texto sobre la pantalla
        Global.screen.blit(text, (75, 120))
        Global.screen.blit(text_points, (10, 170))
        Global.screen.blit(text_reiniciar, (70, 250))

        pygame.display.update()
