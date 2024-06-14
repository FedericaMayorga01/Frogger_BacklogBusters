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
        self.ticks_time_musica = 1800 # 30 ticks == 1 segundo

    def test_music_rotation(self):
        """
        DADO un reloj interno del juego que lleva el tiempo transcurrido desde el inicio de la partida
        CUANDO pasan 1 minuto
        ENTONCES el sistema reconoce el tiempo transcurrido y cambia la canción de manera aleatoria
        """
        self.game.timeMusic = 0
        self.game.currentMusic = 1   #si la musica actual es la 1
        self.function.tiempoMusica(self.game, self.musica1, self.musica2, self.ticks_time_musica)

        self.musica1.play.assert_not_called()
        self.musica2.play.assert_called_once() # esperamos que la musica a la que se pone play sea la 2
