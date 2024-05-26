import unittest
from unittest.mock import Mock
from src.Game import Game

class testVelocidadAutos(unittest.TestCase):

    def setUp(self):
        self.game = Mock()

        def nextLevel(llegadas, enemys, plataforms, frog, game):
            if len(llegadas) == 5:
                game.incLevel()
                game.incSpeed()
                game.incPoints(100)
                game.resetTime()

        self.nextLevel=nextLevel


    def test_VelocidadAutos(self):
        """DADO que llegaron 5 ranas a destino y se finalizó un nivel CUANDO inicia el nuevo nivel ENTONCES los autos se mueven mas rápido"""
        llegadas= [Mock(), Mock(), Mock(), Mock(), Mock()]

        game = Game(3, 1)
        initial_speed = game.speed
        self.nextLevel(llegadas, Mock(), Mock(), Mock(), game)

        self.assertEqual(game.speed, initial_speed+1)


    def test_nextLevel(self):
        """DADO que se llama a la funcion de subir de nivel CUANDO las llegadas son iguales a 5 ENTONCES se llama a la funcion de incrementar nivel"""
        llegadas=[]
        for i in range(5):
            # con createArrive agrega una nueva llegada a la lista
            llegadas.append(Mock())
            # en next level deberia pasar el if de len(llegadas) llamando a game.inclevel
            self.nextLevel(llegadas, Mock(), Mock(), Mock(), self.game)

        self.game.incLevel.assert_called_once()