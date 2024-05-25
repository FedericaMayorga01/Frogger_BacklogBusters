import unittest
from unittest.mock import Mock, patch
from src.Frog import Frog

class testFrog(unittest.TestCase):

    def setUp(self):
        self.animacion = Mock()
        self.frog = Frog([207, 475], self.animacion)

    @patch('src.Frog.pygame')
    # Vamos a utilizar el decorador patch para simular el modulo pygame con un objeto Mock
    # El objeto Mock se pasa como argumento a la funcion test_mover_rana

    def test_mover_rana(self, mock_pygame):
        # Test rana se mueve para arriba
        self.frog.mover_rana('up', 1)
        self.assertEqual(self.frog.position, [207, 462])
        print("Prueba para mover la rana hacia arriba aprobada")

        # Test rana se mueve para abajo
        self.frog.mover_rana('down', 1)
        self.assertEqual(self.frog.position, [207, 475])
        print("Prueba para mover la rana hacia abajo aprobada")

        # Test rana se mueve hacia la izquierda
        self.frog.mover_rana('left', 1)
        self.assertEqual(self.frog.position, [193, 475])
        print("Prueba para mover la rana hacia la izquierda aprobada")

        # Test rana se mueve hacia la derecha
        self.frog.mover_rana('right', 1)
        self.assertEqual(self.frog.position, [207, 475])
        print("Prueba para mover la rana hacia la derecha aprobada")