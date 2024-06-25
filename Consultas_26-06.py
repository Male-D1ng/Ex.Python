# Online Python - IDE, Editor, Compiler, Interpreter
from queue import LifoQueue as Pila 
from queue import Queue as Cola
import random
from typing import List

"""
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila:
     p = Pila()
     n = cantidad
     while n > 0:
          nro:int = random.randint(desde, hasta)
          p.put(nro)
          n -= 1
     return p
     
c = 2
desde = 5
hasta = 6

cola_azar = generar_nros_al_azar(c,desde,hasta)

def buscarElMaximo(p: Pila) -> int:
    res: int = 0
    paux: Pila = Pila()

    while not p.empty():
        elem: int = p.get()
        paux.put(elem)
        if elem > res:
            res = elem
    
    while not paux.empty():
        elem = paux.get()
        p.put(elem)

    return res
    
#print (buscarElMaximo(cola_azar))


def formula_bien_balanceada(formula: str) -> bool:

    p:Pila[str] = Pila()

    for c in formula:
        if c == "(" or c == ")":
            p.put(c)
    
    n: int = 0

    while not p.empty() and n >= 0:
         parentesis = p.get()

         if parentesis == ')':
              n += 1
         elif parentesis == '(':
              n -= 1

    return n == 0
            
print(formula_bien_balanceada("3*(5*5)-(5-4)"))
#formula_bien_balanceada("7((3/7)")
#formula_bien_balanceada("(10*(-1)))")
#formula_bien_balanceada("(4*(-1)))")
#formula_bien_balanceada("))9+7((")



#EJ11_PARTE_P
def esta_bien_balanceada (s:str)-> bool:
    p = Pila ()
    for str in s: 
        if str == '(':
            p.put(str)
        elif str == ')':
            if p.empty():
                return False
            p.get(str)
    if p.empty():
        return True
    else:
        return False
print('la formula esta balanceada: ',esta_bien_balanceada('1 + (2 x 3 - (20 / 5))'))



def invertida(l:[int]) -> [int]:
    invertida:[int] = []
    i  = len(l) - 1
    while i >= 0:
        invertida.append(l[i])
        i -= 1
    return invertida
    
l = [1,2,3,4,5,6]

print (invertida(l))



def  generar_nros_al_azar(c:int,desde:int,hasta:int)-> Cola:
    cola = Cola () 
    for _ in range(c):
        res = random.randint(desde,hasta)
        cola.put(res) 
    return cola

c = 5
desde = 5
hasta = 100

cola_azar = generar_nros_al_azar(c,desde,hasta)

while not cola_azar.empty():
    numero = cola_azar.get()
    print(numero)
    
    
def de_cola_a_lista(c:Cola) -> list:
    l:list = []
    while not c.empty():
        elemento = c.get()
        l.append(elemento)
    
    for i in l:
        c.put(i)

    return l
    
print(de_cola_a_lista(cola_azar))

"""
def generar_nros_al_azar_cola(cantidad:int, desde:int, hasta:int) -> Cola:
    n:int = cantidad
    c = Cola()

    while n > 0:
        elemento = random.randint(desde, hasta)
        c.put(elemento)
        n -= 1

    return c

mi_colita = generar_nros_al_azar_cola(5, 1, 10)

while not mi_colita.empty():
    numero = mi_colita.get()
    print(numero)
    

#Hago esta función que para algo va a servir más adelante    
def de_cola_a_lista(c:Cola) -> list:
    l:list = []
    while not c.empty():
        elemento = c.get()
        l.append(elemento)
    
    for i in l:
        c.put(i)

    return l

mi_colita = generar_nros_al_azar_cola(5, 1, 10)
print(de_cola_a_lista(mi_colita))
#función para imprimirme la cola

def cantidad_elementos_cola(c:Cola) -> int:
    copia:Cola[int] = Cola ()
    res:int = 0
    while not c.empty():
        elemento = c.get()
        copia.put(elemento)
        res += 1
    
    while not copia.empty():
        elem = copia.get ()
        c.put(elem)
    
    return res
cola_hecha = generar_nros_al_azar_cola(5, 1, 10)
print(cantidad_elementos_cola(cola_hecha))


def maximo_cola (c:Cola)-> int:
    copia:Cola[int] = Cola()
    res:int = c.get() #el maximo_cola, que sera el primer elemento de la cola
    copia.put(res)
    while not c.empty ():
        elemento = c.get() #el nuevo elem
        copia.put(elemento)
        if res < elemento:
            res = elemento
    while not copia.empty():
        c.put(copia.get())
    return res 
    
otra_cola = generar_nros_al_azar_cola(5, 1, 10)
print(maximo_cola(otra_cola))



def pertenece1(s:list, e) -> bool: 
    i:int = 0 
    while i < len(s):
        if s[i] == e:
            return True
        i += 1
    return False

def armar_secuencia_bingo2() -> Cola(int):
    secuencia: Cola = Cola()
    elementos:list(int) = list(range(100)) # Pero se puede usar range()? igualmente sería una lista del 0 al 99
    random.shuffle(elementos)

    for elemento in elementos:
        secuencia.put(elemento)
    return secuencia

#print(de_cola_a_lista(armar_secuencia_bingo2()))

"""
def jugar_carton_de_bingo(carton:[int], bolillero:Cola(int)) -> int:
    res:int = 0
    n:int = len(carton)
    while n > 0:
        bolilla:int = bolillero.get()
        if pertenece1(carton, bolilla): 
            n -= 1
        res += 1
    return res 
"""
#CONSULTAAA
def jugar_carton_de_bingo (carton: [int], bolillero: Cola(int)) -> int:
    cantSinMarcar: int = len (carton)
    temp = []
    res = 0

    while cantSinMarcar > 0: # no hace falta ver si bolillero esta vacio
        bolilla: int = bolillero.get()
        temp.append(bolilla)
        if bolilla in carton: # Vamos a permitir que usen in en listas también. <---
            cantSinMarcar -=1
        res += 1

    for num in temp: # regenero el bolillero
        bolillero.put(num)

    return res 
    
carton=[0,99]
b = armar_secuencia_bingo2()
#print(de_cola_a_lista(b))
print("Para ganar la cantidad de jugadas es ",jugar_carton_de_bingo(carton, b))

