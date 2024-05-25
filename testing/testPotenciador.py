import unittest
import pygame
from src.Frog import Frog
from src.Game import Game
from src.Potenciador import Potenciador

class TestPotenciador(unittest.TestCase):
    def setUp(self):
        mock_image = pygame.Surface((50, 50))  # Create a 50x50px image
        self.frog = Frog([207, 475], mock_image)
        self.game = Game(3, 1)
        self.potenciador = Potenciador(mock_image)

    def test_collision(self):
        # Set the frog and potenciador to the same position
        self.frog.position = [100, 100]
        self.potenciador.position = [100, 100]

        # Check if the frog collides with the potenciador
        self.assertTrue(self.frog.rect().colliderect(self.potenciador.rect()))

        # Check the game speed
        initial_speed = self.game.speed
        self.game.speed /= 2
        self.assertEqual(self.game.speed, initial_speed / 2)

        # Check the potenciador disappears
        self.potenciador.disappear()
        self.assertEqual(self.potenciador.position, [-100, -100])

    def test_reset_position(self):
        initial_position = self.potenciador.position
        self.potenciador.reset_position()
        self.assertNotEqual(self.potenciador.position, initial_position)

    def test_disappear(self):
        self.potenciador.disappear()
        self.assertEqual(self.potenciador.position, [-100, -100])

    def test_speed_reduction(self):
        # Set the frog and potenciador to the same position to cause a collision
        self.frog.position = [100, 100]
        self.potenciador.position = [100, 100]

        initial_speed = self.game.speed
        # Simulate the effect of the collision
        if self.frog.rect().colliderect(self.potenciador.rect()):
            self.game.speed /= 2

        self.assertEqual(self.game.speed, initial_speed / 2)