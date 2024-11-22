#ej_importantes.py

#encontar las columnas de una matriz

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




