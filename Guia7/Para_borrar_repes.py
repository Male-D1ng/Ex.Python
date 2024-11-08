#ej es_matriz
def es_matriz(s:list[list[int]])->bool:
    #qvq tiene igual longitud a lo ancho y alto, me conviene q primero vaya el False por que sino no recorre todo la lista
    for longitud in range(0,len(s),1):
        if len(s)>0:
            if len(s[longitud]) != len(s[0]):
                return False
    return True

#ej3.6.3 columna c/ c<len(m[0]) y es_matriz(m)
def columna(m:list[list[int]],c:int)->list[int]:
    lista_res:list[int]=[]
    for n in m:
        for l in range(0,len(n),1): #si el indice n es el nro de columna quiero q me de el nro en esa posicion
            if l == c:
                lista_res.append(n[l]) #nro en la posicion de la columna pedida
    return lista_res
colum = 2
print("la columna",colum,"es =",columna([[1,2,3],[4,5,6],[7,8,9]],colum))



#ej 3.6.5 transponer --> devuelve m^t, usar funciuon columna
def transponer (m:list[list[int]])->list[list[int]]:
    #las filas se vuelven columnas y las columnas las filas
    matriz_res:list[list[int]]=[]
    for n in range(0,len(m),1): #tengo q ver todas las filas con un indice
        if not es_matriz(m):
            return "no es valido"
        else:
            matriz_res.append(columna(m,n))
    return matriz_res

print(transponer([[1,4,7],[2,5,8],[3,6,9]]))

"""horizontal
todos los de lista iguales
vertical
los elementos de la misma posición en las listas son iguales
diagonal
primer elemento de primera lista = segundo elemento segunda lista"""



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

def columna(m:list[list[int]],c:int)->list[int]:
    lista_res:list[int]=[]
    for n in m:
        for l in range(0,len(n),1): #si el indice n es el nro de columna quiero q me de el nro en esa posicion
            if l == c:
                lista_res.append(n[l]) #nro en la posicion de la columna pedida
    return lista_res
colum = 2
print("la columna",colum,"es =",columna([[1,2,3],[4,5,6],[7,8,9]],colum))

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
    res:int=2
    n:int=0
    l:int=0
    while n<=3 and l<len(lista):
        colum = columna(lista,n)
        if todos_iguales(colum) and lista[l][0]=='O':
            res = 0
            return res
        elif todos_iguales(colum) and lista[l][0]=='X':
            res = 1
            return res 
        else:
            n+1
            l+=1
    return res 

print("caso vertical ",casos_verticales(([['X','O','X'],['X','X','O'],['X','O','0']])))



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


# def tateti ACÁ JUNTÁS LAS 3 AUXILIARES.
def quien_gana_tateti(m:list[list[chr]])->int:
    res:int=0
    #la matriz es de 3x3
    if casos_horizontales(m) == 0 or casos_verticales(m) == 0 or caso_diagonal(m) == 0:
        res = 0
    elif casos_horizontales(m) == 1 or casos_verticales(m) == 1 or caso_diagonal(m) == 1:
        res = 1
    else:
        res = 2
    return res 

print("el ganador es ",quien_gana_tateti(([['X','O','X'],['X','X','O'],['X','O','0']])))


































"""  



def casos_vertical(n:list[list[chr]])-> chr:
    if n[0][0]== n[1][0] == n[2][0] and n[0][0]== "0":
        return  'O'
    elif n[0][1]== n[1][1] == n[2][1] and n[0][1]== "X":
        return  'X'
    else:
        return "mal"

print ("el caso verical es para las =",casos_vertical([['X','0','0'],['X','0','0'],['X','0','0']]))
