import unittest
from unittest.mock import Mock, patch
from src.Frog import Frog

class testFrog(unittest.TestCase):

    def setUp(self):
        self.animacion = Mock()
        self.position_inic = [207, 475]
        self.frog = Frog(self.position_inic, self.animacion)

    @patch('src.Frog.pygame')
    # Vamos a utilizar el decorador patch para simular el modulo pygame con un objeto Mock
    # Lo hacemos para que no se ejecute la parte de pygame en el metodo mover_rana
    def test_mover_rana_arriba(self, mock_pygame):
        """DADO que se esta en una partida activa CUANDO el jugador presiona la flecha para arriba ENTONCES la rana avanza un lugar hacia arriba"""
        self.frog.mover_rana('up', 1)
        self.assertEqual(self.frog.position, [207, 462])

    @patch('src.Frog.pygame')
    def test_mover_rana_abajo(self, mock_pygame):
        """DADO que se esta en una partida activa CUANDO el jugador presiona la flecha para abajo ENTONCES la rana avanza un lugar hacia arriba"""
        # Test rana se mueve para abajo
        self.frog.mover_rana('down', 1)
        self.assertEqual(self.frog.position, [207, 475])

    @patch('src.Frog.pygame')
    def test_mover_rana_izq(self, mock_pygame):
        """DADO que se esta en una partida activa CUANDO el jugador presiona la flecha para la izquierda ENTONCES la rana avanza un lugar hacia arriba"""
        # Test rana se mueve hacia la izquierda
        self.frog.mover_rana('left', 1)
        self.assertEqual(self.frog.position, [193, 475])

    @patch('src.Frog.pygame')
    def test_mover_rana_der(self, mock_pygame):
        """DADO que se esta en una partida activa CUANDO el jugador presiona la flecha para la derecha ENTONCES la rana avanza un lugar hacia arriba"""
        # Test rana se mueve hacia la derecha
        self.frog.mover_rana('right', 1)
        self.assertEqual(self.frog.position, [221, 475])

    @patch('src.Frog.pygame')
    def test_mover_rana_tecla_no_valida(self, mock_pygame):
        """DADO que se esta en una partida activa CUANDO el jugador presiona cualquier otra tecla ENTONCES la rana no se mueve"""
        # Test rana se mueve hacia la derecha
        self.frog.mover_rana('space', 1)
        self.assertEqual(self.frog.position, self.position_inic)