import unittest
from app import cuadrado_binomio 

class TestCuadradoBinomio(unittest.TestCase):

    def test_cuadrado_binomio_positivos(self):
        # (2 + 3)^2 = 5^2 = 25
        # a^2 + 2ab + b^2 = 2^2 + 2*2*3 + 3^2 = 4 + 12 + 9 = 25
        self.assertEqual(cuadrado_binomio(2, 3), 25)

    def test_cuadrado_binomio_con_cero(self):
        # (5 + 0)^2 = 5^2 = 25
        # a^2 + 2ab + b^2 = 5^2 + 2*5*0 + 0^2 = 25 + 0 + 0 = 25
        self.assertEqual(cuadrado_binomio(5, 0), 25)

    def test_cuadrado_binomio_negativos(self):
        # (-1 + -2)^2 = (-3)^2 = 9
        # a^2 + 2ab + b^2 = (-1)^2 + 2*(-1)*(-2) + (-2)^2 = 1 + 4 + 4 = 9
        self.assertEqual(cuadrado_binomio(-1, -2), 9)

    def test_cuadrado_binomio_positivo_y_negativo(self):
        # (4 + -2)^2 = (2)^2 = 4
        # a^2 + 2ab + b^2 = 4^2 + 2*4*(-2) + (-2)^2 = 16 - 16 + 4 = 4
        self.assertEqual(cuadrado_binomio(4, -2), 4)

if __name__ == '__main__':
    unittest.main()