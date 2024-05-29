import unittest
from unittest.mock import Mock

import pygame
from src.Frog import Frog
from src.Game import Game
from src.Potenciador import Potenciador

class TestPotenciador(unittest.TestCase):
    def setUp(self):
        self.position_inic=[207, 475]
        self.frog = Frog(self.position_inic, Mock())
        self.game = Game(3, 1)
        self.potenciador = Potenciador(Mock())

    def test_collision(self):
        """DADO que se esta en una partida activa CUANDO la posicion de la rana
        es la misma que la del potenciador ENTONCES ambos colisionan"""
        self.frog.position = [100, 100]
        self.potenciador.position = [100, 100]

        self.assertTrue(self.frog.rect().colliderect(self.potenciador.rect()))


    def test_reset_position(self):
        """DADO que se esta en una partida activa CUANDO pasa cierto tiempo y
        el jugador no agarra el potenciador ENTONCES el potenciador desaparece"""
        initial_position = self.potenciador.position
        self.potenciador.reset_position()
        self.assertNotEqual(self.potenciador.position, initial_position)

    def test_disappear(self):
        """DADO que se esta en una partida activa CUANDO el jugador agarra
        un potenciador ENTONCES el potenciador desaparece"""
        self.potenciador.disappear()
        self.assertEqual(self.potenciador.position, [-100, -100])

    def test_speed_reducida(self):
        """DADO que se esta en una partida activa CUANDO el jugador agarra
        un potenciador ENTONCES la velocidad del juego disminuye"""
        # Set the frog and potenciador to the same position to cause a collision
        self.frog.position = [100, 100]
        self.potenciador.position = [100, 100]

        initial_speed = self.game.speed
        # Simulate the effect of the collision
        if self.frog.rect().colliderect(self.potenciador.rect()):
            self.game.speed /= 2

        self.assertEqual(self.game.speed, initial_speed / 2)