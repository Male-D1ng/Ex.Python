
from queue import Queue as Cola

"""
from queue import Queue as Cola

# Ejercicio 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    notas_dicc: dict[str, list[tuple[str,int]]]
    for t in notas_estudiante_materia:
        if t[0] in notas_dicc.keys() and not pertenece_a_tupla (dict[t[0]], [t[1]]) :
                dict [t[0]] = list.append (t[1],t[2])
        else:
             dict [t[0]] = {t[1],t[2]}
    return notas_dicc 
 

# funcion auxiliar para pertenece un elemento a una tupla
def pertenece_a_tupla (lista: list[tuple[str,int]], e:str):
        res:bool = False
        if e in lista:
            res = True


gestion_notas [("Jose", "ALgebra", 5),("Martin", "Fisica", 8), ("Lauti", "Algo", 9), ("Martin", "Quimica",9), ("Martin", "Fisica",6)] 


# Ejercicio 2
def cantidad_digitos_pares(numeros: list[int]) -> int:
    return 0

# Ejercicio 3
def reordenar_cola_primero_pesados(paquetes: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    return Cola()

# Ejercicio 4
def matriz_pseudo_ordenada(matriz: list[list[int]]) -> bool:
    return True

"""

# Ejercicio 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    notas_dicc: dict[str, list[tuple[str,int]]] = {}
    for t in notas_estudiante_materia:
        if t[0] in notas_dicc.keys():
            if pertenece_a_tupla (notas_dicc[t[0]], t[1]) == False:
                notas_dicc [t[0]] = notas_dicc[t[0]] + [(t[1],t[2])]
#               notas_dicc[t[0]].append((t[1],t[2])) 
        else:
             notas_dicc [t[0]] = [(t[1],t[2])]
    return notas_dicc 
 

# funcion auxiliar para pertenece un elemento a una tupla
def pertenece_a_tupla (lista: list[tuple[str,int]], e:str)-> bool:
        res: bool
        for tupla in lista:
            materia = tupla[0] 
            if e == materia:
                res = True
                return res
        return False

notas_estudiante_materia: list[tuple[str,str,int]] = [("Jose", "Algebra", 5),("Martin", "Fisica", 8), ("Lauti", "Algo", 9), ("Martin", "Quimica",9), ("Martin", "Fisica",6)] 
print(gestion_notas (notas_estudiante_materia))


# Ejercicio 2
#def cantidad_digitos_pares(numeros: list[int]) -> int:
#    suma_digitos_pares:int = 0
#    for e in numeros:
#        for i in range[len(e)]:
#                if i % 2 == 0:
#                    suma_digitos_pares = suma_digitos_pares + 1
        
#    return suma_digitos_pares

# funcion auxiliar que descomponga un numero en sus digitos

def descomponer_en_digitos (num:int) -> list[int]:
    lista: list[int] = []
    e: int = num % 10
    lista.append 

# cantidad de digitos
def cantidad_digitos (numero:int) -> int:
    cant_dig: int = 0
    while numero / 10 >= 1:
         cant_dig = cant_dig + 1
         numero = numero/10
    cant_dig = cant_dig + 1
    return cant_dig

print(cantidad_digitos (100))

#numeros:list[int] = [3,55,2,6,8,9,324]
#print (cantidad_digitos_pares(numero)
# 
str(45124124)

int('A')