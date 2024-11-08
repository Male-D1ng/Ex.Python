#1. PRIMERA 1: RECORRIDO Y BUSQUEDA EN SECUENCIAS 

#ej1, pertenece, parte de una lista y el entero "e" y devuelve un bool sobre si "e" pertenece o no

from contextlib import ContextDecorator

from numpy import char


lista = [1, 2, 3, 4, 5]
def pertenece (lista:list[int], e:int)-> bool:
        if e in lista:
            return True
        else:
            return False

#print (pertenece(lista,11))

#me creo una lista agregue de 1 en 1
def creo_lista (i:int,f:int)-> list[int]: 
     l = []
     for n in range(i,f+1,1):
          l.append(n)
          n+=1
     return l
print(creo_lista(1,5))
          

s = ["l","e"] 
def pertenece2 (s: list[str], e: str) -> bool:
    for elem in s:
        if elem == e:
            return True
    return False

#print (pertenece2 (s,"e"))


# ej 1.1
def pertenece_if (s:list [int], e: int) -> bool:
    if e in s:
        return True
    else:
        return False

def pertenece_for (s:list [int], e: int) -> bool:
    for i in s:
        if e == i:
            return True
    return False

def pertenece_bool (s:list[bool], e: bool) -> bool:
    for i in range (0,len(s),1):
        if s[i] == e:
            return True
    return False

print(pertenece_bool([True,True],False))

# ej 1.2

#ej2, divideATodos (in s:seq<Z>, in e: Z) : Bool, si s[i] mod e = 0)}

def divideATodos (s:list[int],e:int) -> bool:
     e != 0
     for i in s:
          if s[i] % e == 0:
               return True
     return False

def divide_a_todos (s: list [int], e: int) -> bool:
    for i in s:
        if i%e != 0:
            return False
    return True

def divide_a_todos_v2 (s: list [int], e: int) -> bool:
    for i in s:
        if s[i] %e != 0:
            return False
    return True


#ej3,  sumaTotal (in s:seq<Z>) : Z, res es la suma de todos los elementos de s
def sumaTotal (s:list[int])->int:
     res = 0  
     for i in s: 
        res += i  
     return res

#ej4 maximo

# ej 1.4
def maximo (s:list [int]) -> int:
    indice_del_mayor: int = 0
    for i in range (len(s)):
        if s[indice_del_mayor] < s[i]:
            indice_del_mayor = i
    return s[indice_del_mayor]

def maximo2 (s:list[int]) -> int:
    el_mas_grande = s[0]
    for elem in s:
        if el_mas_grande < elem:
            el_mas_grande = elem
    return el_mas_grande


#ej5 minimo

#ej 1.5
def minimo (s: list [int]) -> int:
    el_mas_chico: int = s[0]
    for elem in s:
        if el_mas_chico > elem:
            el_mas_chico = elem
    return el_mas_chico

#ej6,  ordenados (in s:seq<Z>) : Bool , si (|s| − 1) → s[i] < s[i + 1]
def ordenados (s:list[int])->bool:
     for i in range (0,len(s)-1,1):
          if s[i]>s[i+1]:
               return False
     return True 
print(ordenados([1,2,3,4,5,4]))


def estanOrdenados (s: list [int]) -> bool:
    anterior: int = s[0]
    for elem in s:
        if elem <= anterior:
            anterior = elem
            return True
    return False


#ej7 pos maximo

def pos_maximo (s:list [int]) -> int:
    indice_del_mayor: int = 0
    for i in range (len(s)):
        if s[indice_del_mayor] < s[i]:
            indice_del_mayor = i
    return indice_del_mayor

print("la pos es: ",pos_maximo([1,2,3]))

#ej8 pos minimo
def pos_minimo (s:list [int]) -> int:
    indice_del_menor: int = 0
    for i in range (len(s)):
        if s[indice_del_menor] > s[i]:
            indice_del_menor = i
    return indice_del_menor

print("la pos es: ",pos_minimo([1,2,3]))

               
#ej9, Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7
def mayor_a_7 (l:list[str])->bool:
    for i in l: 
        if len(i)>=7:
            return True
    return False

#ej10, Dado un texto en formato string, devolver verdadero si se lee igual en ambos sentidos == PALINDROMO
def palabra_reverso (p:list[str])->bool:
     palabra : str = ""
     for i in range(len(p) - 1, -1, -1):
          palabra += p[i] 
     return p == palabra
print(palabra_reverso("olo"))


#ej11 True si hay 3 nros iguales consecutivos, en cualquier posicion
def nros_consecutivos_3 (s:list[int])->bool:
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return True
    return False
              
print("hay 3 nros seguidos? = ",nros_consecutivos_3([1,5,4,4,4]))

#version mas parecida a lo q queria hacer
def num_iguales(s: list[int]) -> bool:
    indice: int = 0
    indice_mayor: int = 1
    contador_iguales: int = 0

    while indice_mayor < len(s):
        if s[indice] == s[indice_mayor]:
            contador_iguales += 1
            if contador_iguales == 2:
                return True
            indice += 1
            indice_mayor += 1
        else:
            contador_iguales = 0
            indice += 1
            indice_mayor += 1
    return False
    
print(num_iguales([1,1,1,56,2]))
print(num_iguales([1,2,4,4,2,56,2]))

#ej12 True si una palabra tiene al menos 3 vocales distintas
#letras vocales son 'a','e','i','o','u'. qvq halla 3 de ellas
def vocales_diferentes (palabra :str)->bool:
    vocales = ['a','e','i','o','u']
    vocales_en_palabra =[]
    contador = 0
    for letras in range (0,len(palabra)-1,1):
        #quiero q encuentre la primera vocal y dps sigo buscando, pero tengo q guardarla en algun lugar para seguir buscando
        if pertenece2(vocales,palabra[letras]) and not pertenece2 (vocales_en_palabra,palabra[letras]):
            vocales_en_palabra.append(palabra[letras])
            contador += 1
        elif not pertenece2(vocales,palabra[letras]) and not pertenece2 (vocales_en_palabra,palabra[letras]): #si no cumple no suma nada, no quiero q se reinicie
            contador += 0
    if contador == 3:
            return True
    else:
            return False 

print("da false = ",vocales_diferentes("arbol"))
print("da true = ",vocales_diferentes("arboles"))
print("da false = ",vocales_diferentes("ardilla"))


#ej13 devolver la posicion dnde inicia la sec de nros ordenada mas larga
#si hay dos subsec de igual longitud devolver la pos dnde empieza la primera
#def sec_nros_ordenados (lista:list[int])->int:
#print("posicion ",sec_nros_ordenados())


#ej14 cantidad de digitos impares
def separador_nros(lista:list[int])->list[int]:
    lista_aux = [] #lista de todoos los nros en lista
    for i in range(0,len(lista),1):
        separador = str(lista[i]) #los int no los puedo separar como los str o list asi q por ahora lo transformo
        indice = 0
        while len(separador)>indice:
            digito = int(separador[indice]) #para esta cuenta me conviene volver al int
            lista_aux.append(digito)
            indice+=1
    return lista_aux

def cantidad_impares(lista:list[int])->int:
    contador = 0
    lista_aux = separador_nros(lista)
    for i in range(0,len(lista_aux),1):
        if lista_aux[i] %2 != 0 :
            contador += 1
        else:
            contador += 0
    return contador 

print("cantidad impares = ",cantidad_impares([57, 2383, 812, 246]))


#PARTE 2: RECORRER, FILTRAR, MODIFICAR Y PROCESAR SECUENCIAS

# ej 2.2.1

def CerosEnPosicionesPares_v2 (s: list [int]):
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0
        else:
            s[i]

s_prueba = [1,2,3]
CerosEnPosicionesPares_v2(s_prueba)
print(s_prueba)


# ej 2.2.2
#def CerosEnPosicionesPares2 (s:list [int]) -> list [int]:
def CerosEnValoresPares (s: list [int]):
    lista: list [int] = []
    for i in s:
        if i % 2 == 0:
            lista.append(0)
        else:
            lista.append(i)
    return lista
"""
def CerosEnPosicionesPares (s: list [int]):
    lista: list [int] = []
    for i in range(len(s)):
        if i % 2 == 0:
            lista.append(0)
        else:
            lista.append(s[i])

print(CerosEnPosicionesPares ())
"""

#ej 2.2.3 Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales ni espacios.
def cadena_sin_vocales (frase:str)-> str:
    vocal = ['a','e','i','o','u']
    nueva_cadena: str = ""
    for letras in range(0,len(frase),1):
        if not pertenece2(vocal,frase[letras]):
            nueva_cadena += frase[letras] #agrego a la nueva cadena la letra q va
        else:
            frase[letras+1]
    return nueva_cadena

print("nueva cadena =",cadena_sin_vocales("arbol"))

#ej 2.2.4 problema reemplaza vocalespor '_'
def reemplazo_vocales (frase: str)-> str:
    vocal = vocal = ['a','e','i','o','u']
    nueva_frase:str = ""
    for l in range(0,len(frase),1):
        if not pertenece2(vocal,frase[l]):
            nueva_frase += frase[l] #agrego a la nueva cadena la letra q va
        else:
            nueva_frase += '_'
    return nueva_frase

print("nueva frase =",reemplazo_vocales("arbol"))

# ej 2.2.5 problema da vuelta str
#res[i] = s[|s| − i − 1]}
def dar_vuelta_str (frase:str)-> str:
    nueva_frase:str = ""
    for l in range(len(frase)-1,-1,-1):
        nueva_frase += frase[l]
    return nueva_frase

print("al reves =",dar_vuelta_str("abol"))

#ej 2.2.6 . problema eliminar repetidos
def sin_repetidos (frase:str)->str:
    nueva_frase:str = frase[0]
    for l in range(1,len(frase),1):
        if not pertenece2(nueva_frase,frase[l]): 
#como la primera letra de nueva_frase es la de frase, el range comoenza en la posicion 1, pero el fin tiene q ser la longitud de la frase sino 
#no veo todas las letras
            nueva_frase += frase[l]
    return nueva_frase
print("sin repes =",sin_repetidos("areno"))

# ej 2.3 resultados Materia
"""
problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
requiere: {|notas| > 0}
requiere: {Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10)}
asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7}
asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
"""
def promedio(notas: list[int])->int:
    suma_notas = 0
    for n in range(0,len(notas),1):
        suma_notas += notas[n]
    return suma_notas/len(notas)

print("resultado materia =",promedio([7,7,7,7]))

def resultadoMateria (notas:list[int])->int:
    lista: list[bool] = []
    for n in range(0,len(notas),1):
        if notas[n] >= 4:
            lista.append(True)
        else:
            lista.append(False)
    if pertenece_bool(lista,False) or promedio(notas)<4:
        return 3
    elif not pertenece_bool(lista,False) and 4<=promedio(notas)<7:
        return 2
    else:
        return 1
    
print("resultado materia 1 =",resultadoMateria([7,7,7,7]))
print("resultado materia 2 =",resultadoMateria([7,4,6,5]))
print("resultado materia 3 =",resultadoMateria([7,7,7,3]))


#ej 2.4 saldo/cuenta bancaria

def cuenta_bancaria(lista_tuplas:list[tuple[str,float]])-> float:
     saldo_actual:float = 0
     for tupla in lista_tuplas:
          if tupla[0] == "I":
               saldo_actual += tupla[1]
          elif tupla[0] == "R":
               saldo_actual -= tupla [1]
     return saldo_actual

print(cuenta_bancaria([("I",2000),("R",20),("I",20)]))


#PARTE 3 : MATRICES

# ej 3.5.1
def pertenece_a_cada_uno_version_1 (s: list [list [int]], e: int, res: list[bool]):
    i: int = 0
    res.clear()
    while (i < len(s)):
        res.append (pertenece_if (s[i], e))
        i += 1

s = [[1,2], [3,4]]
e = 1
t = [False, False]

pertenece_a_cada_uno_version_1(s,e,t)
print (t)


# ej 3.5.2 y ej 3.5.2
def pertenece_a_cada_uno_v2 (s:list[list[int]],e:int, res:list[bool]):
     for i in range(0, len(s), 1):
          if pertenece(s[i],e):
               res[i] = True
          else:
               res[i] = False 

res: list[bool] = [True, False, False]
print(res)

pertenece_a_cada_uno_v2([[1,2],[2,3],[3]], 3, res)

print(res)

"""
for lista in listas:
     len(listas[0])== len (lista)
"""

#ej 3.5.4 es de pensar teoria y la rta es q lo q cambia es como son parametros de entrada vs los de salida

#ej 3.6.1 problema es_matriz : { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|)}

def es_matriz(s:list[list[int]])->bool:
    #qvq tiene igual longitud a lo ancho y alto, me conviene q primero vaya el False por que sino no recorre todo la lista
    for longitud in range(0,len(s),1):
        if len(s)>0:
            if len(s[longitud]) != len(s[0]):
                return False
    return True

print("es matriz? =",es_matriz([[1,2,3],[4,5,6],[7,8,9],[1,2,3]]))

#ej 3.6.2 problema filas ordenadas :  { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }

def filas_ordenadads(s:list[list[int]])->bool:
    for longitud in range(0,len(s),1):
        if es_matriz(s):
            if not ordenados(s[longitud]): #si no estan ordenados directamente da mal y no tiene q seguir recorriendo
                return False
    return True

print("estan ordenadas las filas? =",filas_ordenadads([[1,2,3],[4,5,6],[7,8,9]]))

def f_ordenadas (s:list[list[int]], res:bool):
    res:bool = True
    for longitud in range(0,len(s),1):
        if es_matriz(s):
            if not ordenados(s[longitud]): #si no estan ordenados directamente da mal y no tiene q seguir recorriendo
                res = False
    return res

s = [[1,2,3],[4,5,6],[7,8,1]]
res = True
print(f_ordenadas(s,res))

#ej 3.6.3 problema columna : { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en
#el mismo orden que aparecen}
#c < |m[0]|, es_matriz(s), c ≥ 0
def columna(m:list[list[int]],c:int)->list[int]:
    lista_res:list[int]=[]
    for n in m:
        for l in range(0,len(n),1): #si el indice n es el nro de columna quiero q me de el nro en esa posicion
            if l == c:
                lista_res.append(n[l]) #nro en la posicion de la columna pedida
    return lista_res
colum = 2
print("la columna",colum,"es =",columna([[1,2,3],[4,5,6],[7,8,9]],colum))


#ej 3.6.4 problema columnas ordenadas : → (res[c] = true ↔ ordenados(columna(m, c))) 
def columnas_ordenadas (s:list[list[int]])->bool:
    indice:int
    lista_colum = columna(s,indice)
    res:int = True
    for longitud in range(0,len(s),1): #el indice me dice q nro de columna es
        if es_matriz(s):
            if longitud == indice:
            #lista_colum.append(s[longitud][0])
                if not ordenados(lista_colum): #me fijo si la columna 0 coincide con la siguiente
                    res = False
    return res 

print("estan ordenadas las columnas? =",columnas_ordenadas([[1,4,7],[2,5,8],[3,6,9]]))


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

#ej 3.6.6 Ta-Te-Ti tradicional 
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


#PARTE 4: Programas interactivos usando secuencias

#ej 4.7.1 lista_estudiantes con input
def lista_estudiantes()->list[str]:
    lista = []
    entrada = input("Nombre del alumno: ")
    while entrada != "terminar" and entrada!= "":
        lista.append(entrada)
        entrada = input("Nombre del alumno: ")
    return lista
print(lista_estudiantes())


#ej 4.7.2 monedero_electrónico, C = cargar,D = descontar, X = finalizar
def monedero_electronico ()-> list[(str,int)]:
    lista:list[tuple[str,int]] = []
    accion = input("Acción realizada = ")
    monto = input ("Ingrese el monto = ")
    nro:int = 0
    while accion != "X":
        if accion == "C":
            nro = monto
            lista.append((accion,nro))
        elif accion == "D":
            nro = monto
            lista.append((accion,nro))
        
        accion = input("Acción realizada = ")
        monto = input("Ingrese el monto = ")

    return lista

print(monedero_electronico())

#EJ 4.7.3 NO TENGO GANAS DE HACERLO PERO ES MEDIO LO MISMO

#ej 4.7.4 contraseña : entra un string,  sale otro string con tres posibles valores: VERDE, AMARILLA y ROJA
def contrasena (c:str)->str:
     if len (c) < 5:
          return 'Roja'
     if len (c) > 8:
          if hayMinus(c) and hayMayus(c) and hayNum (c):
               return 'Verde'
     return 'Amarillo'


def hayMinus (m:str) -> bool:
     for letra in m:
          if 'a' <= letra <= 'z':
               return True
          return False
     
def hayMayus (m:str) -> bool:
     for letra in m:
          if 'A' <= letra <= 'Z':
               return True
          return False

def hayNum (n:int)-> bool:
     for num in n :
          if '0' <= num <= '9':
               return True
          return False

