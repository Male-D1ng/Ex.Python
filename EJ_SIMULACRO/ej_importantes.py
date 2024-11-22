#ej_importantes.py

from queue import Queue as Cola
import random

#ej14
def cantidadElementos(c: Cola) -> int:
    res: int = 0
    cola = Cola ()
    caux: cola = Cola()

    while not c.empty():
        elem = c.get()
        caux.put(elem)
        res = res + 1
    
    while not caux.empty():
        elem = caux.get()
        c.put(elem)
        
    return res

mi_cola = Cola ()
mi_cola.put(1)
mi_cola.put(2)

print(cantidadElementos(mi_cola))



#EJ7_PARTE_A
import csv
#el archivo csv se ve como : nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
def contarlineas(lu : str) -> int:
    #primero abro el archivo
    archivo=open(lu,'r')
    #lo leo
    leo_archivo=archivo.readlines()
    archivo.close()
    return len(leo_archivo)
print("la cantidad de lineas es :", contarlineas("archivo_de_prueba.txt"))



def apariciones(notas:list[str], alumno:str) -> int:
    apariciones:int = 0
    for nota in notas:
        campos = nota.split(',')
        if campos [0] == alumno:
            apariciones += 1
    return apariciones



#ncontar las columnas de una matriz

def columna_n (matriz:list[list[int]],n:int)->list[int]:
    columna:list[int]=[]
    n:int
    for filas in range(len(matriz)):
        columna.append(matriz[filas][n])
    return columna

l =[[2,3,5],[4,6,23],[5,8,3]]
n=2
print("columna n=",columna_n(l,n))

def todas_las_columnas(matriz:list[list[int]])->list[list[int]]:
    res:list[list[int]]=[]
    for filas in range(len(matriz)):
        colum_n:list[int] = columna_n(matriz,filas)
        res.append(colum_n)
    return res

l =[[2,3,5],[4,6,23],[5,8,3]]
print("columna n=",todas_las_columnas(l))




