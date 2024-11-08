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




































"""  



def casos_vertical(n:list[list[chr]])-> chr:
    if n[0][0]== n[1][0] == n[2][0] and n[0][0]== "0":
        return  'O'
    elif n[0][1]== n[1][1] == n[2][1] and n[0][1]== "X":
        return  'X'
    else:
        return "mal"

print ("el caso verical es para las =",casos_vertical([['X','0','0'],['X','0','0'],['X','0','0']]))
