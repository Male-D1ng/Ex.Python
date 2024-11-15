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


def buscar_maximo (p:Pila[int])-> int:
    paux:Pila[int]=Pila() #asi puedo sacar loe elems de la original y poder usarlos como quiera
    maximo = p.get()
    paux.put(maximo)
    while not p.empty():
        elem = p.get()
        paux.put(elem)
        if elem>maximo:
            maximo = elem
        else:
            p.get()
            paux.put(p.get())

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










