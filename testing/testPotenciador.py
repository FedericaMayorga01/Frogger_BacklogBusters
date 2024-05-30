import unittest
from unittest.mock import Mock

import pygame

from FroggerGameLogic import FroggerGameLogic
from src.Frog import Frog
from src.Game import Game
from src.Potenciador import Potenciador

class TestPotenciador(unittest.TestCase):
    def setUp(self):
        mock_animation = pygame.Surface((120,30))
        self.frog = Frog([100,400], mock_animation)
        self.game = Mock()
        mock_sprite = pygame.Surface((20,20))
        self.potenciador = Potenciador(mock_sprite)
        self.potenciador.position = [100,400]
        self.function = FroggerGameLogic()

    def test_collision(self):
        """DADO que se esta en una partida activa CUANDO la posicion de la rana
        es la misma que la del potenciador ENTONCES ambos colisionan"""
        enemys = []
        ticks_enemys = []
        ticks_plataforms = []

        self.function.ubicacion_rana( self.frog, enemys, Mock(), Mock(), self.game, Mock(), Mock(), Mock(),
                                     Mock(), self.potenciador, ticks_enemys, ticks_plataforms)

        self.game.scale_speed.assert_called_once()

    def test_disappear(self):
        """DADO que se esta en una partida activa CUANDO el jugador agarra
        un potenciador ENTONCES el potenciador desaparece"""
        enemys = []
        ticks_enemys = []
        ticks_plataforms = []

        self.function.ubicacion_rana(self.frog, enemys, Mock(), Mock(), self.game, Mock(), Mock(), Mock(),
                                     Mock(), self.potenciador, ticks_enemys, ticks_plataforms)

        self.assertEqual(self.potenciador.position, [-100, -100])

    def test_speed_reducida(self):
        """DADO que se esta en una partida activa CUANDO el jugador agarra
        un potenciador ENTONCES la velocidad del juego disminuye"""
        # Set the frog and potenciador to the same position to cause a collision
        initial_speed=3
        game = Game(initial_speed, 1)
        enemys = []
        ticks_enemys = []
        ticks_plataforms = []

        self.function.ubicacion_rana(self.frog, enemys, Mock(), Mock(), game, Mock(), Mock(), Mock(),
                                     Mock(), self.potenciador, ticks_enemys, ticks_plataforms)

        self.assertEqual(game.speed, initial_speed/2)

    def test_reset_position(self):
        """DADO que se esta en una partida activa CUANDO pasa cierto tiempo y
        el jugador no agarra el potenciador ENTONCES el potenciador cambia de posicion"""
        position_inic = self.potenciador.position

        #Forzamos que el potenciador no este activo
        self.game.potenciador_active = False

        self.potenciador.timer = 500
        self.function.resetPotenciador(self.potenciador, self.game)

        self.assertNotEqual(self.potenciador.position, position_inic)

    def test_end_boost_false(self):
        """DADO que el jugador agarra un potenciador CUANDO todavia no ha pasado el tiempo
        de accion completo ENTONCES el potenciador sigue activo"""
        self.game.potenciador_active = True
        self.potenciador.active_timer = 10

        self.function.potenciadorActive(self.potenciador, self.game)

        # Al no haber terminado no tiene que haber cambiado la velocidad
        self.game.reset_speed.assert_not_called()

    def test_end_boost_positive(self):
        """DADO que el jugador agarra un potenciador CUANDO pasa el tiempo de accion completo
        ENTONCES el potenciador termina de hacer efecto"""
        self.game.potenciador_active = True
        self.potenciador.active_timer = 0

        self.function.potenciadorActive(self.potenciador, self.game)

        # Al haber terminado tiene que haber reseteado la velocidad
        self.game.reset_speed.assert_called_once()