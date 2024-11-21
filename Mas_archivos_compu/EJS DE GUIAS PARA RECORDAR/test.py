#Ejemplo debug:
 
from typing import List
 
def prueba ():
    for i in range(10):
        if i % 2 == 0:
            print("es par")
            x = i/2
        else:
            x = i
        print (x)
        auxiliar(x)

def auxiliar (x:int):
    a = x - 1
    b = x - 2
    c = x - 3
    print (a+b+c)
 
#prueba()
 
#1.3
def suma_total (cadena :List[int]) -> int:
    res:int = 0
    for i in cadena:
        res += i
    return res
 
def suma_total_v2 (cadena :List[int]) -> int:
    res:int = 0
    for i in range (len(cadena)):
        res += cadena[i]
    return res
 
st = [2, 5, 0, 10]
#print (suma_total(st))
#print (suma_total_v2(st) == 17)
 
 
#1.1
def pertenece_v1 (cadena :List[int], elem: int) -> bool:
    for i in cadena:
        if i == elem:
            return True
    return False
 
def pertenece_v2 (cadena :List[int], elem: int) -> bool:
    res: bool = False
    for i in cadena:
        if i == elem:
            res = True
 
    return res
 
def pertenece_v3 (cadena :List[int], elem: int) -> bool:
    return elem in cadena
 
print (pertenece_v1([2,4,5,6], 5))
print (pertenece_v1([2,4,5,6], 7))
 
def pertenece_w(s:list[int], e:int) -> bool:
      longitud:int = len(s)
      indice_actual:int = 0
      pertenece:bool = False
 
      while indice_actual < longitud:
        if s[indice_actual] == e:
            pertenece = True
        indice_actual = indice_actual + 1
 
      return pertenece
 
def pertenece_w_2(s:list[int], e:int) -> bool:
    longitud:int = len(s)
    indice_actual:int = 0
    pertenece:bool = False
 
    while (indice_actual < longitud) and (not pertenece):
        if (s[indice_actual] == e):
            pertenece = True
        indice_actual = indice_actual + 1
 
    return pertenece
 
#1.7
def tiene_minuscula (cadena: str) -> bool :
    res: bool = False
    for c in cadena:
        if 'a' <= c and c <= 'z' :
            res = True
    return res 
 
def tiene_mayuscula (cadena: str) -> bool :
    res: bool = False
    for c in cadena:
        if 'A' <= c and c <= 'Z' :
            res = True
    return res 
 
def tiene_numeros (cadena: str) -> bool :
    res: bool = False
    for c in cadena:
        if '0' <= c and c <= '9' :
            res = True
    return res 
 
def fortaleza_PWD_v2 (cadena: str) -> str:
    tiene_min: bool = tiene_minuscula(cadena)
    tiene_may: bool = tiene_mayuscula(cadena)
    tiene_mum: bool = tiene_numeros(cadena)
    mayor_a_8: bool = len(cadena) > 8
 
    if tiene_may and tiene_mum and tiene_min and mayor_a_8 :
        return "VERDE"
    elif len(cadena) < 5 :
        return "ROJA"
    else :
        return "AMARILLA"
 
 
 
x = fortaleza_PWD_v2 ("a6$_Afghij5Dklmnopqrstuvwxyz")
x = fortaleza_PWD_v2 ("a6$_")
x = fortaleza_PWD_v2 ("Dklmnopqrstuvwxyz")
 
def fortaleza_PWD_v1 (cadena: str) -> str:
    tiene_min: bool = False
    tiene_may: bool = False
    tiene_mum: bool = False
    mayor_a_8: bool = len(cadena) > 8
 
    for c in cadena:
        if c.isalpha():
            if c.islower():
                tiene_min = True
            elif c.isupper():
                tiene_may = True
        elif c.isnumeric():
            tiene_mum = True
 
    if tiene_may and tiene_mum and tiene_min and mayor_a_8 :
        return "VERDE"
    elif len(cadena) < 5 :
        return "ROJA"
    else :
        return "AMARILLA"
 
def imprime_ecoX10(eco:str) -> str :
     ecos =  "eco \n"
     print (ecos*10)

lista = [10, 20, 30, 40, 50]
for i in range(len(lista) - 1,-1,-1):
    print(lista[i])
    #print(f"{lista[i]} y {lista[i + 1]}")

list = [10, 20, 30, 40, 50]
ultimo_elemento = list[len(list) - 1]
print(ultimo_elemento)


#EJ 4 PARCIAL/SIMULACRO 1°CUATRI 2024
"""
lista=[3,2,1]

for i in range (len(lista)-1,-1,-1)

   print(lista[i])

   

Cuantos palindromos sufijos : osea q se lee igual de izq a der y de der a izq.
Asegura que res es igual a la cantidad de palindromos que hay en el conjunto de sufijos de texto, dnde texto 

"""

#ejs 16/17/18 de la guia 8