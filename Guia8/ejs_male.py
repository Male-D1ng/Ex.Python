#ej 1.1 generar_nros_al_azar
from queue import LifoQueue as Pila 
from typing import TextIO
import random 

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)-> Pila[int]: 
    p:Pila[int]= Pila() 
    n = cantidad
    while n > 0:
          nro:int = random.randint(desde, hasta)
          p.put(nro)
          n -= 1
    return p

#FUNCION PARA IMPRIMIR PILAS Y COLAS 
def impresora (p:Pila[int])-> None: #tbien podria devolver una lista 
    paux:Pila[int]= Pila()
    while not p.empty(): 
       elem:int = p.get() 
       print(elem) 
       paux.put(elem)
    while not paux.empty():
       i = paux.get()
       p.put(i)


p = Pila() 
#p. put(1) #apilar 
#lemento = p.get() #desapilar 
#p.empty #bool, pregunta si es vacia 
"""
cantidad = 5
desde = 10 
hasta = 20
p = generar_nros_al_azar(cantidad,desde,hasta) 
impresora(p) 
"""

# otra forma de escribir la funcion generar_nros_al_azar
def generar_nros_azar(cantidad : int, desde : int, hasta : int) -> Pila[int]:
    pila: Pila [int] = Pila()
    for _ in range(0,cantidad,1): #si lo comenzara desde el 1 seria cantidad+1
        elem: int = random.randint(desde, hasta)
        pila.put(elem)
    return pila

def mostrar_elems_pila(p:Pila[int]): #in
    paux:Pila[int] = Pila()
    while not p.empty():
        elem: int = p.get()
        print(elem)
        paux.put(elem)
    while not paux.empty():
        e:int = paux.get()
        p.put(e)

"""
cantidad = 5
desde = 1
hasta = 10
p:Pila[int] = Pila()
p = generar_nros_azar (cantidad, desde, hasta)
mostrar_elems_pila(p)
"""

#ej2 cantidad_elementos
def cantidad_elementos(p:Pila[int])-> int: #es de tipo in asi q los parametros de entrada si se pueden modificar pero dps hay q restaurarlos
    paux:Pila[int]=Pila()#paso para restaurarla
    cantidad:int = 0
    while not p.empty(): #paso para poder recorrer la lista mientras no este vacia
        elemento = p.get()
        cantidad +=1
        paux.put(elemento)
    while not paux.empty():
        p.put(paux.get())
    return cantidad 



#ej 3 buscar_el_maximo
def generar_nros(cantidad:int,desde:int,hasta:int)-> Pila[int]: 
    p:Pila[int]= Pila() 
    n = cantidad
    nro:int=desde
    while n > 0 and nro < hasta:
        p.put(nro)
        nro +=1
        n -= 1
    return p
    

#ej 1.3 buscar_maximo
#razonamiento
def buscar_maximo (p:Pila[int])-> int: 
    paux:Pila[int]=Pila() #saco los elems de la original y los modifico, dps se usa para restaurar la original
    maximo = p.get() #asumo q el maximo es el primer elemento
    paux.put(maximo) #lo guardo
    while not p.empty():
        elem = p.get() #saco el segundo elem y lo guardo
        paux.put(elem)
        if elem>maximo: #comienzo la comparacion entre el max y el resto de los elementos de la pila
            maximo = elem
        else:
            p.get() 
            paux.put(p.get()) #siempre q saco un nuevo elemento primero lo guardo en la auxiliar

    while not paux.empty():
        p.put(paux.get()) 

    return maximo 

def buscar_el_maximo_v2(c : Pila [int]) -> int:
    paux:Pila[int] = Pila()
    if not c.empty():
        maximo: int = c.get()
        paux.put(maximo)
    else:
        maximo = None
    while not c.empty():
        elem: int = c.get()
        paux.put(elem)
        if elem > maximo:
            maximo = elem
    while not paux.empty():
        e:int = paux.get()
        c.put(e)
    return maximo

p:Pila[int] = Pila()
cantidad = 6
desde = 1
hasta = 10
#p = generar_nros (cantidad, desde, hasta)
#mostrar_elems_pila(p)
h = generar_nros_al_azar(cantidad,desde,hasta)
mostrar_elems_pila(h)
print("la cantidad de elementos es ",cantidad_elementos(h)) 
print("el maximo es ",buscar_el_maximo_v2(h))



#ej 1.4 buscar_nota_maxima, devuelve una tupla dnde aparece la maxima nota en la segunda componente de la tupla 
def buscar_nota_maxima (p : Pila[tuple[str,int]]) -> tuple[str,int]:
    paux: Pila[tuple [str,int]] = Pila()
    if not p.empty():
        maximo: tuple[str,int] = p.get()
        paux.put(maximo)
    while not p.empty():
        elem: tuple[str,int] = p.get()
        paux.put(elem)
        if elem[1] > maximo[1]:
            maximo = elem
    while not paux.empty():
        f = paux.get()
        p.put(f)
    return maximo


def buscar_nota_minima(c : Cola[str,int]) -> int:
    paux: Cola[str,int] = Cola()
    if not c.empty():
        maximo: tuple [str,int] = c.get()
        paux.put(maximo)
    while not c.empty():
        elem: tuple[str, int] = c.get()
        paux.put(elem)
        if elem < maximo:
            maximo = elem
    while not paux.empty():
        aux = paux.get()
        c.put(aux)
    return maximo[1]




#EJ11_PARTE_P

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












