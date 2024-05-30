import unittest
from unittest.mock import Mock
from src.Game import Game
from FroggerGameLogic import FroggerGameLogic
import random
class testVelocidadAutos(unittest.TestCase):

    def setUp(self):
        self.game = Mock()
        self.function= FroggerGameLogic()


    def test_VelocidadAutos(self):
        """
        DADO que llegaron 5 ranas a destino y se finalizó un nivel
        CUANDO inicia el nuevo nivel
        ENTONCES los autos se mueven más rápido
        """

        llegadas= [Mock(), Mock(), Mock(), Mock(), Mock()]

        initial_speed = 3
        game = Game(initial_speed, 1)

        self.function.nextLevel(llegadas, Mock(), game)

        self.assertEqual(game.speed, initial_speed+1)


    def test_nextLevel(self):
        """
        DADO que se llama a la funcion de subir de nivel
        CUANDO las llegadas son iguales a 5
        ENTONCES se llama a la funcion de incrementar nivel
        """
        llegadas = []

        for i in range(5):
            # con createArrive agrega una nueva llegada a la lista
            llegadas.append(Mock())
            # en next level deberia pasar el if de len(llegadas) llamando a game.inclevel
            self.function.nextLevel(llegadas, Mock(), self.game)

        self.game.incLevel.assert_called_once()

    def test_next_many_levels(self):
        """
        DADO que se llama a la funcion de subir de nivel
        CUANDO las llegadas son iguales a 5
        ENTONCES se llama a la funcion de incrementar nivel
        """
        llegadas = []
        num = random.randint(1, 26)

        for i in range(num):
            # con createArrive agrega una nueva llegada a la lista
            llegadas.append(Mock())
            # en next level deberia pasar el if de len(llegadas) llamando a game.inclevel

            self.function.nextLevel(llegadas, Mock(), self.game)

        self.assertEqual(self.game.incLevel.call_count, int(num/5))