import unittest
from unittest.mock import Mock
from src.Game import Game
from FroggerGameLogic import FroggerGameLogic
class testMusica(unittest.TestCase):

    def setUp(self):
        self.game = Mock()
        self.function = FroggerGameLogic()
        self.musica1 = Mock()
        self.musica2 = Mock()
        self.ticks_time_musica = 1800

    def test_music_rotation(self):
        """
        DADO un reloj interno del juego que lleva el tiempo transcurrido desde el inicio de la partida
        CUANDO pasan 3 minutos
        ENTONCES el sistema reconoce el tiempo transcurrido y cambia la canción de manera aleatoria
        """
        self.game.timeMusic = 0

        self.function.tiempoMusica(self.game, self.musica1, self.musica2, self.ticks_time_musica)

        self.musica1.play.assert_not_called()
        self.musica2.play.assert_called_once()
