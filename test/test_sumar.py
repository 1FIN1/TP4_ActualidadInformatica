import unittest
from app import sumar 

class TestSumar(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_con_cero(self):
        self.assertEqual(sumar(5, 0), 5)

    def test_suma_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)

    def test_suma_positivo_y_negativo(self):
        self.assertEqual(sumar(5, -3), 2)

if __name__ == '__main__':
    unittest.main()