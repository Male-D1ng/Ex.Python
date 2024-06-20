#prueba_cola
#ej 13_PARTE_C
from queue import Queue as Cola
from queue import LifoQueue as Pila
import random


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

# contar elementos de una cola

#ej14_PARTE_C
def cantidadElementos(c: Cola) -> int:
    res: int = 0
    cola = Cola ()
    caux: cola = Cola()

    while not c.empty():
        elem = c.get()
        caux.put(elem)
        res = res + 1
    
    while not caux.empty():
        elem = caux.get()
        c.put(elem)
        
    return res


#EJ10_PARTE_P

# version con especificacion que garantiza
# que la pila no es vacia

def buscarElMaximo(p: Pila) -> int:
    res: int = p.get()
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


#EJ15_PARTE_C
def buscar_el_maximo_cola(c: Cola) -> int:
    aux: Cola = Cola()
    maximo = c.get()
    aux.put(maximo)
    while not c.empty():
        elem_actual = c.get()
        aux.put(elem_actual)
        if maximo < elem_actual:
            maximo = elem_actual

    while not aux.empty():
        c.put(aux.get())
    return maximo




#EJ16_PARTE_C

from queue import Queue as Cola
import random

def armarSecuencideBingo() -> Cola:
    #armo una lista con los numeros del 0 al 9
    lista: list = list(range(0,9))
    #desordena de forma random la lista
    random.shuffle(lista)
    #creo una cola y la lleno con los elementos de la lista
    bolillero: Cola = Cola()
    for bolilla in lista:
        bolillero.put(bolilla)
    return bolillero

#determina cual es la cantidad de jugadas de ese bolillero que se necesitan para ganar.
def jugarCartonDeBingo(carton: list, bolillero: Cola) -> int:
    cantSinMarcar: int = len(carton)
    jugadas: int = 0
    bolilleroAux: Cola = Cola()
    #mientras no marque todos los numeros del carton saco bolillas
    while cantSinMarcar > 0:
        num: int  = bolillero.get()
        bolilleroAux.put(num)
        if num in carton:
            cantSinMarcar -= 1
        jugadas += 1
    
    while not bolillero.empty():
        num: int  = bolillero.get()
        bolilleroAux.put(num)
        
    while not bolilleroAux.empty():
        num: int  = bolilleroAux.get()
        bolillero.put(num)
    
    return jugadas


bolillero = armarSecuencideBingo()
carton = [1,5]

print("EL BOLILLERO :",list(bolillero.queue))
print(jugarCartonDeBingo(carton,bolillero))
#print(list(bolillero.queue))

        





