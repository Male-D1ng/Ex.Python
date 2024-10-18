#1. Primera Parte

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

#ej2, divideATodos (in s:seq<Z>, in e: Z) : Bool, si s[i] mod e = 0)}

def divideATodos (s:list[int],e:int) -> bool:
     e != 0
     for i in s:
          if s[i] % e == 0:
               return True
     return False

#ej3,  sumaTotal (in s:seq<Z>) : Z, res es la suma de todos los elementos de s
def sumaTotal (s:list[int])->int:
     res = 0  
     for i in s: 
        res += i  
     return res

#ej4,  ordenados (in s:seq<Z>) : Bool , si (|s| − 1) → s[i] < s[i + 1]
def ordenados (s:list[int])->bool:
     for i in range (len(s)-1):
          if s[i]>s[i+1]:
               return False
     return True 
               
#ej5, Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7
def mayor_a_7 (l:list[str])->bool:
    for i in l: 
        if len(i)>=7:
            return True
    return False

#ej6, Dado un texto en formato string, devolver verdadero si se lee igual en ambos sentidos == PALINDROMO
def palabra_reverso (p:list[str])->bool:
     palabra : str = ""
     for i in range(len(p) - 1, -1, -1):
          palabra += p[i] 
     return p == palabra
print(palabra_reverso("olo"))

#ej7 contraseña : entra un string,  sale otro string con tres posibles valores: VERDE, AMARILLA y ROJA
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


def cuenta_bancaria(lista_tuplas:list[tuple[str,float]])-> float:
     saldo_actual:float = 0
     for tupla in lista_tuplas:
          if tupla[0] == "I":
               saldo_actual += tupla[1]
          elif tupla[0] == "R":
               saldo_actual -= tupla [1]
     return saldo_actual

print(cuenta_bancaria([("I",2000),("R",20),("I",20)]))


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
