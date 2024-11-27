from queue import Queue as Cola
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

    


