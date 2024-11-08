"""horizontal
todos los de lista iguales
vertical
los elementos de la misma posición en las listas son iguales
diagonal
primer elemento de primera lista = segundo elemento segunda lista"""

# def tateti ACÁ JUNTÁS LAS 3 AUXILIARES.

def todos_iguales(l:list[chr])->bool: # Función para ver si los elementos de UNA ÚNICA LISTA son todos iguales.
    n:int=len(l)
    res:bool=True
    i:int = 0
    while n>0:
        if l[i]!=l[0]:
            res = False
            n-=1
            i+=1
            return res
        else:
            n-=1
            i+=1
    return res
print(todos_iguales (['X','X','X','O']))

def casos_horizontales(lista:list[list[chr]])->int: # Función para ver si los elementos de UNA DE LAS LISTAS
# son todos iguales (acá tenés que determinar si son X u O).
    res:int
    for l in range(0,len(lista),1):
        if todos_iguales(lista[l]) and lista[l][0]=='O':
            res = 0
            return res 
        elif todos_iguales(lista[l]) and lista[l][0]=='X':
            res = 1
            return res
        else:
            res = 2 
    return res

print(casos_horizontales([['X','X','O'],['O','O','O'],['X','X','O']]))

def casos_verticales(lista:list[list[chr]])->int:
    return 0

def caso_diagonal(lista:list[list[chr]])->int: #FUNCIONA SIN RECURSIÓN.
    if (lista[0][0] == lista[1][1] == lista[2][2]) and (lista[0][0] == 'O'):
        res=0
    elif (lista[0][2] == lista[1][1] == lista[2][0]) and (lista[0][0] == 'O'):
        res=0
    if (lista[0][0] == lista[1][1] == lista[2][2]) and (lista[0][0] == 'X'):
        res=1
    elif (lista[0][2] == lista[1][1] == lista[2][0]) and (lista[0][0] == 'X'):
        res=1
    else:
        res=2
    return res
print (caso_diagonal([['X','X','X'],['X','X','X'],['X','X','O']]))
