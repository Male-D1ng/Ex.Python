"""from queue import Queue as Cola
from queue import LifoQueue as Pila



# Ejercicio 1

def todos_consecutivos(lista:list[int])->bool:
    res:bool=True
    for e in range(len(lista)-1):
        if (lista[e] + 1) != lista[e+1] or lista[e] != (lista[e+1] - 1):
            return False
    return res 


def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
    longitud = (len(v)-1)
    indice = 0
    cantidad = 0
    lista = []
    while indice <= longitud:
        if not todos_consecutivos(lista):
            lista = []
            cantidad = 0
        if  todos_consecutivos(lista) and longitud > indice:
            lista.append(v[indice])
            longitud -=1
            indice+=1
            cantidad = len(lista)
    
    return (cantidad,indice-1)


print(subsecuencia_mas_larga([2,2,33]))

def maximo_True (examenes:list[bool])->int:
    res:int = 0
    suma:int = 0
    for e in range (len(examenes)):
        if examenes[e] == True:
            suma += 1
        res = suma
    return res


# Ejercicio 2
def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    colaux:Cola[list[bool]]=Cola()
    res:list[int]=[] 
    while not examenes.empty():
        elem:list[bool]=examenes.get()
        colaux.put(elem)
        max = maximo_True(elem)
        res.append(max)
    while not colaux.empty():
        examenes.put(colaux.get())
    return res

c= Cola()
c.put([True])
c.put([False])
print(mejor_resultado_de_ana(c))

# Ejercicio 3
def cambiar_matriz(A: list[list[int]]) -> None:
    res:list[list[int]]=[]
    minimo:int = 1
    maximo:int = (len(A))*(len(A[0]))
    return res


# Ejercicio 4
def pertenece(lista:list[str],letra:str)->bool:
    for e in range(len(lista)):
        if lista[e] == letra:
            return True

def palabras_por_vocales(texto: str) -> dict[int, int]:
    dicc:dict[int,int]={}
    cantidad_palabras = cuantas_palabras_hay(texto)
    letras:list[str] = separar_letras(texto)
    cantidad_letras = len(letras)
    for letra in dicc.keys():
        dicc[letra] = cantidad_palabras
    return dicc

def separar_letras(texto:str)->list[str]:
    res:list[str]=[]
    for e in range(len(texto)):
        res.append(texto[e])
    return res


def cuantas_palabras_hay(lista:str)->int:
    res=0
    texto = separar_letras(lista)
    e:int = 0
    cantidad_palabras = (len(texto)-1)
    if texto[e] != " ":
            res += 1
    while cantidad_palabras > 0:
        if texto[e] == " ": 
            res += 1
        e += 1
        cantidad_palabras -=1
    return res 


def vocales_por_palabra (texto:str)->list[int]:
    res = []
    lista_letras:list[str] = separar_letras(texto)
    cantidad_letras = len(lista_letras)
    vocales = ['a','e','i','o','u']
    cantidad = 0
    #cantidad_palabras = cuantas_palabras_hay(texto)-1
    for e in lista_letras:
        if pertenece(vocales,e):
            cantidad += 1
            cantidad_letras -=1
        elif e == " " :
            res.append(cantidad)
            cantidad_letras -=1
            cantidad = 0
        elif not pertenece(vocales,e):
            cantidad +=0
            cantidad_letras -=1
    return res

"""

l = [1,2,3,4]
f = l.pop()
print(f)
print(l)


#correccion

from queue import Queue as Cola
from queue import LifoQueue as Pila
from typing import List, Tuple



# Ejercicio 1
def todos_consecutivos(lista:List[int])->bool:
    res:bool=True                                        
    for e in range(len(lista)-1):
        if (lista[e] + 1) != lista[e+1] or lista[e] != (lista[e+1] - 1):
            return False
    return res 


def subsecuencia_mas_larga(v: List[int]) -> Tuple[int,int]:
    longitud = (len(v)-1)
    indice = 0
    lista = []
    mas_larga = []
    indice_max = 0
    i = 0
    while indice <= longitud:
        
        if not todos_consecutivos(lista):
            lista.pop()                                 
            indice=indice-1
            if (len(lista)>len(mas_larga)):
                mas_larga = lista
                indice_max = i
            i = indice 
            lista = [] 

        if  todos_consecutivos(lista):
            lista.append(v[indice])  

        indice+=1

    if todos_consecutivos(lista) and len(lista)>len(mas_larga):
        mas_larga = lista
    
    return (len(mas_larga),indice_max)

print(subsecuencia_mas_larga([2,2,33]))

# Ejercicio 2
def cant_repetidos(lista:List[bool], e:bool)->int:
    res = 0
    for i in range(len(lista)):
        if (lista[i]==e):
            res+=1
    return res

def modulo(n:int)->int:
    if (n<0):
        return (n*(-1))
    else:
        return n

def mejor_resultado_de_ana(examenes: Cola) -> List[int]:
    colaux:Cola=Cola()
    res:List[int]=[]
    correctas = 0 
    cant_true =0
    cant_false=0
    while not examenes.empty():
        elem:List[bool]=examenes.get()
        colaux.put(elem)

        cant_true=cant_repetidos(elem, True)
        cant_false=cant_repetidos(elem, False)
        correctas = len(elem)-modulo(cant_true-cant_false)/2
        res.append(correctas)
        
    while not colaux.empty():
        examenes.put(colaux.get())
    return res

c= Cola()
c.put([True, False,True, False]) #4
c.put([False, False])  #1
c.put([False, True, True, False, True, True, True, True]) #6
print(mejor_resultado_de_ana(c))



# Ejercicio 3
def cambiar_matriz(A: List[List[int]]) -> None:
    maximo_elemento: int = len(A) * len(A[0])
    for i in range(len(A)):                                             
        for j in range(len(A[i])):
            A[i][j] = (A[i][j] % maximo_elemento) + 1   

def cambiar_filas(A: List[List[int]]) -> None:
    primer_fila: List[int] = A[0]
    for i in range(len(A)-1):                 
        A[i] = A[i+1]
    A[len(A)-1] = primer_fila
        
A= [[1,2,3], [11,4,5], [8,9,7], [15,14,10], [6, 12, 13]] 
cambiar_matriz(A)
print(A) 

A= [[1,2,3], [11,4,5], [8,9,7], [15,14,10], [6, 12, 13]] 
cambiar_filas(A)
print(A)


# Ejercicio 4
def pertenece(lista:List[str],letra:str)->bool:
    for e in range(len(lista)):
        if lista[e] == letra:
            return True

def palabras_por_vocales(texto: str) -> dict:
    dicc:dict={}
    cant_vocales_por_palabra:List[int] = vocales_por_palabra(texto)
    for cant in cant_vocales_por_palabra:
        if (cant in dicc.keys()):
            dicc[cant]+=1
        else:
            dicc[cant]=1
    return dicc


def vocales_por_palabra (texto:str)->List[int]:
    res = []
    vocales = ["a",'e',"i",'o','u', 'A', "E", 'I', "O", 'U']
    cantidad = 0
    indice=0 

    while (texto[indice]==" "):
        indice+=1

    for i in range(indice,len(texto)-1):             #for i in range(len(texto)), uso texto[i] para ver cada caracter                                 
        if pertenece(vocales,texto[i]):
            cantidad += 1
        elif texto[i] == " " and texto[i+1]!=" ":
            res.append(cantidad)
            cantidad = 0                            
    
    if pertenece(vocales,(texto[len(texto)-1])):
        cantidad+=1
    if (cantidad>0):
        res.append(cantidad)
        
    return res

entrada: str = "aa e   ri F Xrtfgc   i M W    uu"
"""entrada_copia: str = "a e  i F X i M W u"
 salida: dict[int,int] = {0: 4, 1: 3, 2:2}"""

print(palabras_por_vocales(entrada))