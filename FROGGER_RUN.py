from src.Frog import Frog
from src.Game import Game
from src.Global import Global
import pygame
from pygame.locals import *
from sys import exit
from FroggerGameLogic import FroggerGameLogic
from src.Potenciador import Potenciador
from src.Rocola import Rocola

# --- INICIALIZACION ------------------------------------------
pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 32, 2, 4096)  #Configuracion de sonido

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
info_font = pygame.font.SysFont(font_name, 24)
menu_font = pygame.font.SysFont(font_name, 36)

# --- IMAGENES  ----------------------------------------------
# Carga los nombres de las imagenes a usar:
moves_directorio = './res/img/sprite_sheets_up.png'
rana_directorio = './res/img/frog_arrived.png'
potenciador_directorio = './res/img/potenciador.png'
auto1_directorio = './res/img/car1.png'
auto2_directorio = './res/img/car2.png'
auto3_directorio = './res/img/car3.png'
auto4_directorio = './res/img/car4.png'
auto5_directorio = './res/img/car5.png'
tronco_directorio = './res/img/tronco.png'

# Convierte las imagenes en objetos dinamicos
animacion = pygame.image.load(moves_directorio).convert_alpha()
rana = pygame.image.load(rana_directorio).convert_alpha()
potenciador_sprite = pygame.image.load(potenciador_directorio).convert_alpha()
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
musica_fondo1 = pygame.mixer.Sound('./res/sounds/guimo.wav')
musica_fondo2 = pygame.mixer.Sound('./res/sounds/guimo2.wav')
musica_potenciador = pygame.mixer.Sound('./res/sounds/guimo3.wav')

pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

#--- INICIALIZA EL JUEGO -------------------------------------
text_info = menu_font.render(('Presiona cualquier tecla para iniciar!'), 1, (0, 0, 0))
gameInit = 0

# ---------------------------------------------------------------
function = FroggerGameLogic()
glb = Global()
rocola = Rocola(musica_fondo1, musica_fondo2, musica_potenciador)
# ---------------------------------------------------------------

# Inicializa el juego
while gameInit == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            gameInit = 1

    # Dibuja el fondo y el texto del menú en la pantalla
    glb.setFondo()
    glb.setScreen()
    glb.setText(text_info, (5, 150))
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
    # Frecuencia de los enemigos / 30 ticks == 1 segundo
    ticks_enemys = [30, 0, 30, 0, 60]
    # Frecuencia de las plataformas
    ticks_plataforms = [0, 0, 30, 30, 30]
    ticks_time = 30
    pressed_keys = 0
    key_pressed = 0

    # ---------------------------------------------------------
    # Creamos un potenciador
    potenciador = Potenciador(potenciador_sprite)

    # Agregamos los OBSERVERS del potenciador
    potenciador.add_observer(game)
    potenciador.add_observer(glb)
    potenciador.add_observer(rocola)
    # ---------------------------------------------------------

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

        # ---------------------------------------------------------
        # Resetea la posición del potenciador
        function.resetPotenciador(potenciador)

        # Si el potenciador está activo, disminuye el tiempo restante
        function.potenciadorActive(potenciador)
        # ---------------------------------------------------------

        # Agrega elementos extra
        function.createEnemys(ticks_enemys, enemys, game, potenciador, auto1, auto2, auto3, auto4, auto5)
        function.createPlataform(ticks_plataforms, plataforms, game, potenciador, tronco)

        # ---------------------------------------------------------
        # Va rotando la música de fondo
        rocola.tiempoMusica()
        # ---------------------------------------------------------

        # Mueve los elementos extra
        function.moveList(enemys, game.speed)
        function.moveList(plataforms, game.speed)

        function.ubicacion_rana(frog, enemys, plataforms, llegadas, game, musica_perder, musica_agua, musica_exito, rana, potenciador, ticks_enemys, ticks_plataforms)

        function.nextLevel(llegadas, frog, game)

        # Informacion sobre el juego en pantalla
        text_info1 = info_font.render(('Nivel: {0}               Puntos: {1}'.format(game.level, game.points)), 1, (255, 255, 255))
        text_info2 = info_font.render(('Tiempo: {0}           Vidas: {1}'.format(game.time, frog.vidas)), 1, (255, 255, 255))
        # Se dibuja el fondo y la informacion en pantalla
        glb.setScreen()
        glb.setText(text_info1, (10, 520))
        glb.setText(text_info2, (250, 520))

        # Dibuja los elementos extras
        function.drawList(enemys)
        function.drawList(plataforms)
        function.drawList(llegadas)

        # ---------------------------------------------------------
        # Dibuja el potenciador si no esta activo
        if not potenciador.isActive:
            potenciador.draw()
        # ---------------------------------------------------------

        # Movimientos y animaciones de la rana
        frog.animateFrog(key_pressed,key_up)
        frog.draw()

        # ---------------------------------------------------------
        # Destruye los elementos extra que salen de pantalla
        function.destroyEnemys(enemys)
        function.destroyPlataforms(plataforms)
        # ---------------------------------------------------------

        pygame.display.update()
        time_passed = clock.tick(30)

    # En caso de perder las tres vidas
    while gameInit == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                gameInit = 0

        glb.setFondo()
        glb.setScreen()

        # Define los textos de la pantalla
        text = game_font.render('GAME OVER', 1, (255, 0, 0))
        text_points = game_font.render(('Puntuacion: {0}'.format(game.points)), 1, (255, 0, 0))
        text_reiniciar = info_font.render('Presione cualquier tecla para reiniciar!', 1, (255, 0, 0))

        # Se dibuja el texto sobre la pantalla
        glb.setText(text, (75, 120))
        glb.setText(text_points, (10, 170))
        glb.setText(text_reiniciar, (70, 250))

        pygame.display.update()