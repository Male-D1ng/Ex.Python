#1. PRIMERA 1: RECORRIDO Y BUSQUEDA EN SECUENCIAS 

#ej1, pertenece, parte de una lista y el entero "e" y devuelve un bool sobre si "e" pertenece o no

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


def pertenece_f (s:list [int], e: int) -> bool:
    for i in range (len(s)):
        if s[i] == e:
            return True
    return False


def perteneceExtra (s: list[str], e: str) -> bool:
        for i in range(0,len(s),1):
                if s[i] == e:
                        return True
        return False


#pertenece3
def pertenece3 (s: list[str], e: str) -> bool:
        i = 0
        res = False
        while i < len(s) and res == False:
                res = s[i]==e
                i+=1
        return res
        
#pertenece4 NO ES VALIDA PARA EL PARCIAL
def pertenece4 (s: list[str], e: str) -> bool:
        return e in s


# ej 1.2 divideATodos (in s:seq<Z>, in e: Z) : Bool, si s[i] mod e = 0)}

def divideATodos (s:list[int],e:int) -> bool:
     e != 0
     for i in s:
          if s[i] % e == 0:
               return True
     return False
        
def divide_a_todos_v2 (s: list [int], e: int) -> bool:
    for i in s:
        if s[i] %e != 0:
            return False
    return True
        

#ej 1.3  sumaTotal (in s:seq<Z>) : Z, res es la suma de todos los elementos de s
def sumaTotal (s:list[int])->int:
     res = 0  
     for i in s: 
        res += i  
     return res


# ej 1.4 maximo
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


#ej 1.5 minimo
def minimo (s: list [int]) -> int:
    el_mas_chico: int = s[0]
    for elem in s:
        if el_mas_chico > elem:
            el_mas_chico = elem
    return el_mas_chico

#ej 1.6,  ordenados (in s:seq<Z>) : Bool , si (|s| − 1) → s[i] < s[i + 1]
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


#ej 1.7 pos maximo

def pos_maximo (s:list [int]) -> int:
    indice_del_mayor: int = 0
    for i in range (len(s)):
        if s[indice_del_mayor] < s[i]:
            indice_del_mayor = i
    return indice_del_mayor

print("la pos es: ",pos_maximo([1,2,3]))

#ej 1.8 pos minimo
def pos_minimo (s:list [int]) -> int:
    indice_del_menor: int = 0
    for i in range (len(s)):
        if s[indice_del_menor] > s[i]:
            indice_del_menor = i
    return indice_del_menor

print("la pos es: ",pos_minimo([1,2,3]))

               
#ej 1.9, Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7
def mayor_a_7 (l:list[str])->bool:
    for i in l: 
        if len(i)>=7:
            return True
    return False

#ej 1.10, Dado un texto en formato string, devolver verdadero si se lee igual en ambos sentidos == PALINDROMO
def palabra_reverso (p:list[str])->bool:
     palabra : str = ""
     for i in range(len(p) - 1, -1, -1):
          palabra += p[i] 
     return p == palabra
print(palabra_reverso("olo"))


#ej 1.11 True si hay 3 nros iguales consecutivos, en cualquier posicion
#tentativo
def nros_consecutivos_3 (lista:list[int])->bool:
    nro_repe:int=lista[0]
    contador:int = 0
    for e in range(0,len(lista)-1,1):
        if nro_repe == lista[e] and contador == 3:
            nro_repe = lista[e]
            contador +=1
        return True
    return False 

print("hay 3 nros seguidos? = ",nros_consecutivos_3([1,2,3,3,4,5]))



#ej 1.12 True si una palabra tiene al menos 3 vocales distintas


#ej 1.13 devolver la posicion dnde inicia la sec de nros ordenada mas larga
#si hay dos subsec de igual longitud devolver la pos dnde empieza la primera


#ej 1.14 cantidad de digitos impares


#PARTE 2: RECORRER, FILTRAR, MODIFICAR Y PROCESAR SECUENCIAS

# ej 2.1 ejercicio inout
def ceroEnPosicionesPares (s:list[int]):
        for i in s:
                if i%2 == 0:
                        s[i] = 0:
                else:
                       s[i]
s =[1,2,3,4]
ceroenPosicionesPares (s)
print(s)

#ej con append, pero no cumple q sea in out
def ceroEnPosPares (s:list[int])->list[int]:
        lista:list[int]=[]
        for i in range(0,len(s),1):
                if i%2 == 0:
                        lista.append(0)
                else:
                        lista.append(s[i])
        return lista


def CerosEnPosicionesPares_v2 (s: list [int]):
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0
        else:
            s[i]

s_prueba = [1,2,3]
CerosEnPosicionesPares_v2(s_prueba)
print(s_prueba)


# ej 2.2 CerosEnPosicionesPares2 (s:list [int]) -> list [int]:
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

#ej 2.4 cuenta bancaria

def cuenta_bancaria(lista_tuplas:list[tuple[str,float]])-> float:
     saldo_actual:float = 0
     for tupla in lista_tuplas:
          if tupla[0] == "I":
               saldo_actual += tupla[1]
          elif tupla[0] == "R":
               saldo_actual -= tupla [1]
     return saldo_actual

print(cuenta_bancaria([("I",2000),("R",20),("I",20)]))

#PARTE 3: MATRICES

# ej 3.1
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


# ej 3.2
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

#PARTE 4: Programas interactivos usando secuencias

#ej 4.4 contraseña : entra un string,  sale otro string con tres posibles valores: VERDE, AMARILLA y ROJA
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
