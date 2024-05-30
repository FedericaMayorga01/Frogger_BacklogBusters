from src.Enemy import Enemy
from src.Object import Object
from src.Plataform import Plataform


class FroggerGameLogic:
    def __init__(self):
        pass

    # Dibuja en pantalla una lista de objetos
    def drawList(self, list):
        for i in list:
            i.draw()

    # Mueve todos los elementos de la lista
    def moveList(self, list, speed):
        for i in list:
            i.move(speed)

    # Elimina los enemigos que se pasan de los limites pantalla
    def destroyEnemys(self, list):
        for i in list:
            if i.position[0] < -80:
                list.remove(i)
            elif i.position[0] > 516:
                list.remove(i)

    # Elimina las plataformas que se pasan de los limites pantalla
    def destroyPlataforms(self,list):
        for i in list:
            if i.position[0] < -100:
                list.remove(i)
            elif i.position[0] > 448:
                list.remove(i)

    # Inicializa el enemigo
    def createEnemys(self,list, enemys, game, auto1, auto2, auto3, auto4, auto5):
        # list = contaodres para controlar el tiempo entre la creacion de enemigos
        for i, tick in enumerate(list):
            list[i] = list[i] - 1
            if tick <= 0:
                # Si el contador llega a cero, crea un nuevo enemigo y reinicia el contador.
                if i == 0:
                    # Enemigo tipo 1
                    list[0] = (40 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [-55, 436]
                    enemy = Enemy(position_init, auto1, "right", 1)
                    enemys.append(enemy)

                # Configuración del segundo tipo de enemigo.
                elif i == 1:
                    list[1] = (30 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [506, 397]
                    enemy = Enemy(position_init, auto2, "left", 2)
                    enemys.append(enemy)

                # Configuración del tercer tipo de enemigo.
                elif i == 2:
                    list[2] = (40 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [-80, 357]
                    enemy = Enemy(position_init, auto3, "right", 2)
                    enemys.append(enemy)

                # Configuración del cuarto tipo de enemigo.
                elif i == 3:
                    list[3] = (30 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [516, 318]
                    enemy = Enemy(position_init, auto4, "left", 1)
                    enemys.append(enemy)

                # Configuración del quinto tipo de enemigo.
                elif i == 4:
                    list[4] = (50 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [-56, 280]
                    enemy = Enemy(position_init, auto5, "right", 1)
                    enemys.append(enemy)

    # Agrega plataformas para saltar
    def createPlataform(self, list, plataforms, game, tronco):
        for i, tick in enumerate(list):
            list[i] = list[i] - 1
            if tick <= 0:
                if i == 0:
                    list[0] = (30 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [-100, 200]
                    plataform = Plataform(position_init, tronco, "right")
                    plataforms.append(plataform)

                elif i == 1:
                    list[1] = (30 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [448, 161]
                    plataform = Plataform(position_init, tronco, "left")
                    plataforms.append(plataform)

                elif i == 2:
                    list[2] = (40 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [-100, 122]
                    plataform = Plataform(position_init, tronco, "right")
                    plataforms.append(plataform)

                elif i == 3:
                    list[3] = (40 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [448, 83]
                    plataform = Plataform(position_init, tronco, "left")
                    plataforms.append(plataform)

                elif i == 4:
                    list[4] = (20 * game.speed) / game.level * (2.5 if game.potenciador_active else 1)
                    position_init = [-100, 44]
                    plataform = Plataform(position_init, tronco, "right")
                    plataforms.append(plataform)

    # Comprueba si la rana chocó con algun enemigo
    def rana_calle(self, frog, enemys, game, musica_perder, potenciador, ticks_enemys, ticks_plataforms):
        # Compara las areas con el metodo rect del los objetos y la rana
        frogRect = frog.rect()
        potRect = potenciador.rect()

        # Si la rana colisiona con el potenciador
        if frogRect.colliderect(potRect):
            game.scale_speed(0.5)
            potenciador.active_timer = 200
            game.activarPotenciador()
            potenciador.disappear()
            for i in range(len(ticks_enemys)):
                ticks_enemys[i] *= 2.5
            for i in range(len(ticks_plataforms)):
                ticks_plataforms[i] *= 2.5

        # Si la rana colisiona con un enemigo
        for i in enemys:
            enemyRect = i.rect()
            if frogRect.colliderect(enemyRect):
                musica_perder.play()
                frog.frogDead(game)

    # Confirma si la rana está sobre alguna plataforma cuando está en el lago
    def rana_lago(self, frog, plataforms, game, musica_agua):
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


    # Da la ubicacion de la rana y llama a las funciones correspondientes
    def ubicacion_rana(self, frog, enemys, plataforms, llegadas, game, musica_perder, musica_agua, musica_exito, rana, potenciador, ticks_enemys, ticks_plataforms):
        # Si esta en la carretera
        if frog.position[1] > 240:
            self.rana_calle(frog, enemys, game, musica_perder, potenciador, ticks_enemys, ticks_plataforms)

        # Si llega al rio
        elif frog.position[1] < 240 and frog.position[1] > 40:
            self.rana_lago(frog, plataforms, game, musica_agua)

        # Si alcanzó la meta
        elif frog.position[1] < 40:
            self.frogArrived(frog, llegadas, game, musica_exito, rana)

    # Crea un marcador en la zona de llegada
    def createArrived(self, frog, llegadas, game, position_init, musica_exito, rana):
        llegada_rana = Object(position_init, rana)
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
    def nextLevel(self, llegadas, frog, game):
        if len(llegadas) == 5:
            llegadas[:] = []
            frog.setPos_inicial()
            game.incLevel()
            game.incSpeed()
            game.incPoints(100)
            game.resetTime()

    # Comprueba si la rana llega a la zona de llegada y si lo hace, crea un marcador en esa posición
    def frogArrived(self, frog, llegadas, game, musica_exito, rana):
        if frog.position[0] > 33 and frog.position[0] < 53:
            position_init = [43, 7]
            self.createArrived(frog, llegadas, game, position_init, musica_exito, rana)

        elif frog.position[0] > 115 and frog.position[0] < 135:
            position_init = [125, 7]
            self.createArrived(frog, llegadas, game, position_init, musica_exito, rana)

        elif frog.position[0] > 197 and frog.position[0] < 217:
            position_init = [207, 7]
            self.createArrived(frog, llegadas, game, position_init, musica_exito, rana)

        elif frog.position[0] > 279 and frog.position[0] < 299:
            position_init = [289, 7]
            self.createArrived(frog, llegadas, game, position_init, musica_exito, rana)

        elif frog.position[0] > 361 and frog.position[0] < 381:
            position_init = [371, 7]
            self.createArrived(frog, llegadas, game, position_init, musica_exito, rana)

        else:
            frog.position[1] = 46
            frog.animation_counter = 0
            frog.animation_tick = 1
            frog.can_move = 1

    # ---------------------------------------------------------
    # Resetea la posición del potenciador
    def resetPotenciador(self, potenciador, game):
        if potenciador.timer >= 500 and not game.potenciador_active:
            potenciador.reset_position()
            potenciador.timer = 0
        else:
            potenciador.timer += 1

    # Si el potenciador está activo, disminuye el tiempo restante
    def potenciadorActive(self, potenciador, game):
        if potenciador.active_timer > 0:
            potenciador.active_timer -= 1
        elif potenciador.active_timer == 0 and game.potenciador_active:  # Reseteamos la velocidad cuando el potenciador se termina
            game.reset_speed()
            game.desactivarPotenciador()
    # ---------------------------------------------------------