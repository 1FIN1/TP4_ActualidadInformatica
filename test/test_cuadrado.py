import unittest
from app import cuadrado 

class TestCuadrado(unittest.TestCase):

    def test_cuadrado_positivo(self):
        self.assertEqual(cuadrado(4), 16)

    def test_cuadrado_cero(self):
        self.assertEqual(cuadrado(0), 0)

    def test_cuadrado_negativo(self):
        self.assertEqual(cuadrado(-3), 9)

    def test_cuadrado_uno(self):
        self.assertEqual(cuadrado(1), 1)

if __name__ == '__main__':
    unittest.main()