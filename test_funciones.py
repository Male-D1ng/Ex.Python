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

if __name__ == '__main__':
    unittest.main(verbosity=2)



   
