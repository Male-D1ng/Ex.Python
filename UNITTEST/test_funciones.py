# Este archivo puede usarse como template para testear funciones. 
import unittest
from funciones import triangle # Reemplazar por el import correspondiente para testear las funciones deseadas

# La clase puede tener otro nombre pero es necesario mantener el unittest.TestCase
class FuncionesTest(unittest.TestCase):

    # Definimos uno o más casos de test
    def test_1(self):
        self.assertEqual(triangle(1,1,0), 4, "cond 1 - alguno = 0")

    def test_2(self):
        self.assertEqual(triangle(1,1,-1), 4, "cond 1 - alguno <0")

    def test_3(self):
        self.assertEqual(triangle(1,1,-1), 4, "cond 1 - alguno <0")

    def test_4(self):
        self.assertEqual(triangle(1,1,1), 1, "triangulo equilatero")

    def test_5(self):
        self.assertEqual(triangle(5,4,2), 3, "triangulo escaleno")

    def test_6(self):
        self.assertEqual(triangle(5,5,5), 1, "triangulo equilatero")

    def test_7(self):
        self.assertEqual(triangle(2,1,4), 4, "invalido")

    def test_8(self):
        self.assertEqual(triangle(4,-9,1), 4, "invalido negativo")

    def test_9(self):
        self.assertEqual(triangle(1,6,6), 2, "isosceles")

    def test_10(self):
        self.assertEqual(triangle(7,10,12), 3, "escaleno")

    def test_11(self):
        self.assertEqual(triangle(8,5,14), 4, "invalido")

if __name__ == '__main__':
    unittest.main(verbosity=2)



   
