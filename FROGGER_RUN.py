from src.Object import Object
from src.Frog import Frog
from src.Enemy import Enemy
from src.Plataform import Plataform
from src.Potenciador import Potenciador
from src.Game import Game
from src.Global import Global
import pygame
from pygame.locals import *
from sys import exit


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
potenciador_directorio = './res/img/potenciador.png'
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
potenciador_sprite = pygame.image.load(potenciador_directorio).convert_alpha()
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


# --- FUNCIONES GENERALES -------------------------------

# Dibuja en pantalla una lista de objetos
def drawList(list):
    for i in list:
        i.draw()

# Mueve todos los elementos de la lista
def moveList(list,speed):
    for i in list:
        i.move(speed)

# Elimina los enemigos que se pasan de los limites pantalla
def destroyEnemys(list):
    for i in list:
        if i.position[0] < -80:
            list.remove(i)
        elif i.position[0] > 516:
            list.remove(i)

# Elimina las plataformas que se pasan de los limites pantalla
def destroyPlataforms(list):
    for i in list:
        if i.position[0] < -100:
            list.remove(i)
        elif i.position[0] > 448:
            list.remove(i)

# Inicializa el enemigo
def createEnemys(list,enemys,game): 
    # list = contaodres para controlar el tiempo entre la creacion de enemigos
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            # Si el contador llega a cero, crea un nuevo enemigo y reinicia el contador.
            if i == 0:  
                #Enemigo tipo 1
                list[0] = (40*game.speed)/game.level  * (2.5 if game.speed < 3 else 1)
                position_init = [-55,436]
                enemy = Enemy(position_init,auto1,"right",1)
                enemys.append(enemy)

            # Configuración del segundo tipo de enemigo.
            elif i == 1: 
                list[1] = (30*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [506, 397]
                enemy = Enemy(position_init,auto2,"left",2)
                enemys.append(enemy)

            # Configuración del tercer tipo de enemigo.
            elif i == 2:   
                list[2] = (40*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [-80, 357]
                enemy = Enemy(position_init,auto3,"right",2)
                enemys.append(enemy)

            # Configuración del cuarto tipo de enemigo.
            elif i == 3: 
                list[3] = (30*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [516, 318]
                enemy = Enemy(position_init,auto4,"left",1)
                enemys.append(enemy)
            
            # Configuración del quinto tipo de enemigo.
            elif i == 4:  
                list[4] = (50*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [-56, 280]
                enemy = Enemy(position_init,auto5,"right",1)
                enemys.append(enemy)

# Agrega plataformas para saltar
def createPlataform(list,plataforms,game):
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:
                list[0] = (30*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [-100,200]
                plataform = Plataform(position_init,tronco,"right")
                plataforms.append(plataform)

            elif i == 1:
                list[1] = (30*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [448, 161]
                plataform = Plataform(position_init,tronco,"left")
                plataforms.append(plataform)

            elif i == 2:
                list[2] = (40*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [-100, 122]
                plataform = Plataform(position_init,tronco,"right")
                plataforms.append(plataform)

            elif i == 3:
                list[3] = (40*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [448, 83]
                plataform = Plataform(position_init,tronco,"left")
                plataforms.append(plataform)

            elif i == 4:
                list[4] = (20*game.speed)/game.level * (2.5 if game.speed < 3 else 1)
                position_init = [-100, 44]
                plataform = Plataform(position_init,tronco,"right")
                plataforms.append(plataform)


# Comprueba si la rana chocó con algun enemigo
def rana_calle(frog,enemys,potenciador,game):
    # Compara las areas con el metodo rect del los objetos y la rana
    for i in enemys:
        enemyRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(enemyRect):
            musica_perder.play()
            frog.frogDead(game)

# Confirma si la rana está sobre alguna plataforma cuando está en el lago
def rana_lago(frog,plataforms,game):
    # Si la rana esta sobre una plataforma, se debe mover con ella
    # Si la rana no esta sobre ninguna, se muere

    # Se determina si esta sobre alguna plataforma 
    seguro = 0 
    wayPlataform = ""
    for i in plataforms:
        plataformRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(plataformRect):
            seguro = 1
            wayPlataform = i.way

    # Si la rana no está sobre ninguna plataforma
    if seguro == 0: 
        musica_agua.play()
        frog.frogDead(game)

    # Si la rana está sobre una plataforma
    elif seguro == 1: 
        if wayPlataform == "right":
            frog.position[0] = frog.position[0] + game.speed

        elif wayPlataform == "left":
            frog.position[0] = frog.position[0] - game.speed

# Comprueba si la rana llega a la zona de llegada y si lo hace, crea un marcador en esa posición
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

# Da la ubicacion de la rana y llama a las funciones correspondientes
def ubicacion_rana(frog):
    # Si esta en la carretera
    if frog.position[1] > 240 :
        rana_calle(frog,enemys,potenciador,game)

    # Si llega al rio
    elif frog.position[1] < 240 and frog.position[1] > 40:
        rana_lago(frog,plataforms,game)

    # Si alcanzó la meta
    elif frog.position[1] < 40 :
        frogArrived(frog,llegadas,game)

# Crea un marcador en la zona de llegada
def createArrived(frog,llegadas,game,position_init):
    llegada_rana = Object(position_init,rana)
    llegadas.append(llegada_rana)
    musica_exito.play()
    # Restablece la posicion inicial
    frog.setPos_inicial()
    game.incPoints(10 + game.time)
    game.resetTime()
    frog.animation_counter = 0
    frog.animation_tick = 1
    frog.can_move = 1

# Crea el proximo nivel
def nextLevel(llegadas, enemys, plataforms, frog, game):
    if len(llegadas) == 5:
        llegadas[:] = []
        frog.setPos_inicial()
        game.incLevel()
        game.incSpeed()
        game.incPoints(100)
        game.resetTime()


#--- INICIALIZA EL JUEGO -------------------------------------
musica_fondo.play(-1)
text_info = menu_font.render(('Presiona cualquier tecla para iniciar!'), 1, (0, 0, 0))
gameInit = 0

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
    # ---------------------------------------------------------
    # Create a potenciador
    potenciador = Potenciador(potenciador_sprite)

    # Add a timer for the potenciador
    potenciador_timer = 0

    # Add a timer for the speed boost
    speed_boost_timer = 0
    # ---------------------------------------------------------

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
        createEnemys(ticks_enemys, enemys, game)
        createPlataform(ticks_plataforms, plataforms, game)

        # ---------------------------------------------------------
        # Every 500 ticks, reset the potenciador's position
        if potenciador_timer >= 500 and not game.potenciador_active:
            potenciador.reset_position()
            potenciador_timer = 0
        else:
            potenciador_timer += 1

        # If the frog collides with the potenciador, reduce the game speed for 200 ticks
        if frog.rect().colliderect(potenciador.rect()):
            game.speed /= 2
            speed_boost_timer = 200
            game.potenciador_active = True
            potenciador.disappear()
            ticks_enemys = [x * 2.5 for x in ticks_enemys]
            ticks_plataforms = [x * 2.5 for x in ticks_plataforms]

        # If the speed boost timer is active, decrement it
        if speed_boost_timer > 0:
            speed_boost_timer -= 1
        elif speed_boost_timer == 0 and game.speed < 3:  # Reset the game speed when the timer runs out
            game.speed *= 2
            game.potenciador_active = False
        # ---------------------------------------------------------

        # Mueve los elementos extra
        moveList(enemys, game.speed)
        moveList(plataforms, game.speed)

        ubicacion_rana(frog)

        nextLevel(llegadas, enemys, plataforms, frog, game)

        # Informacion sobre el juego en pantalla
        text_info1 = info_font.render(('Nivel: {0}               Puntos: {1}'.format(game.level, game.points)), 1, (255, 255, 255))
        text_info2 = info_font.render(('Tiempo: {0}           Vidas: {1}'.format(game.time, frog.vidas)), 1, (255, 255, 255))
        # Se dibuja el fondo y la informacion en pantalla
        Global.screen.blit(fondo, (0, 0))
        Global.screen.blit(text_info1, (10, 520))
        Global.screen.blit(text_info2, (250, 520))

        # Dibuja los elementos extras
        drawList(enemys)
        drawList(plataforms)
        drawList(llegadas)

        # Movimientos y animaciones de la rana
        frog.animateFrog(key_pressed,key_up)
        frog.draw()
        potenciador.draw()

        # Destruye los elementos extra que salen de pantalla
        destroyEnemys(enemys)
        destroyPlataforms(plataforms)

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