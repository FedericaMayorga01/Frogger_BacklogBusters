from unittest.mock import Mock

import pytest
from src.Game import Game
from src.Frog import Frog
from src.Potenciador import Potenciador

class TestBonusFeature:
    def setup_method(self, method):
        self.game = Game()
        self.frog = Frog([250, 475], Mock())
        self.bonus = Potenciador([250, 475], Mock())

    def test_bonus_collision(self):
        initial_speed = self.game.speed

        # Simulate a game tick where the bonus is visible and the frog is at the same position
        self.bonus.show()
        if self.bonus.get_rect().colliderect(self.frog.get_rect()):
            self.bonus.hide()
            self.game.speed *= 0.9  # Reduce the speed of the cars by 10%

        # Check if the speed of the cars has been reduced
        assert self.game.speed == initial_speed * 0.9