#prueba_cola
#ej 13
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

#ej14
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


#EJ10_PARTE_C

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






