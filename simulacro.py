# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s: list, e: int) -> int:
    pass

##########################################################################
##########################################################################

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def elementos_exclusivos(s: list, t: list) -> list:
    pass

##########################################################################
##########################################################################

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    pass

##########################################################################
##########################################################################

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def convertir_a_diccionario(lista: list) -> dict:
    pass

# Para testear el código

import unittest
from solucion import elementos_exclusivos, ultima_aparicion, contar_traducciones_iguales, convertir_a_diccionario

class Ej1Test(unittest.TestCase):
    def test_trivial(self):
        res = ultima_aparicion([1],1)
        self.assertEqual(res, 0)

    def test_ejemplo(self):
        res = ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1],0)
        self.assertEqual(res, 7)

class Ej2Test(unittest.TestCase):
    def test_trivial(self):
        res = elementos_exclusivos([],[])
        self.assertEqual(res, [])

    def test_ejemplo(self):
        resEsperado = [[3,4,5],[3,5,4],[4,3,5],[4,5,3],[5,3,4],[5,4,3]]
        res = elementos_exclusivos([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5])
        self.assertIn(res, resEsperado)

class Ej3Test(unittest.TestCase):
    def test_trivial(self):
        res = contar_traducciones_iguales({},{})
        self.assertEqual(res,0)

    def test_ejemplo(self):
        aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
        ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
        res = contar_traducciones_iguales(ingles,aleman)
        self.assertEqual(res,2)

class Ej4Test(unittest.TestCase):
    def test_trivial(self):
        res = convertir_a_diccionario([])
        self.assertEqual(res, {})
    
    def test_ejemplo(self):
        resEsperado = {-1:3, 0:1, 4:1, 100:2}
        res = convertir_a_diccionario([-1,0,4,100,100,-1,-1])
        self.assertEqual(res,resEsperado)



if __name__ == '__main__':
    unittest.main(verbosity=2)

