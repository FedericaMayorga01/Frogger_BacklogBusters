import unittest
from unittest.mock import Mock

from src.Rocola import Rocola


class testMusica(unittest.TestCase):

    def setUp(self):
        self.musica1 = Mock()
        self.musica2 = Mock()
        self.musicapot = Mock()
        self.rocola = Rocola(self.musica1, self.musica2, self.musicapot)


    def test_music_rotation(self):
        """
        DADO un reloj interno del juego que lleva el tiempo transcurrido desde el inicio de la partida
        CUANDO pasan 1 minuto
        ENTONCES el sistema reconoce el tiempo transcurrido y cambia la canción de manera aleatoria
        """
        self.rocola.duracionActual = 0
        self.rocola.currentMusic = 1   #si la musica actual es la 1
        self.rocola.tiempoMusica()

        self.musica1.play.assert_called_once()
        self.musica2.play.assert_called_once()  # esperamos que la musica a la que se pone play sea la 2