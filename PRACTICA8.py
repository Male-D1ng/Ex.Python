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
#CONSULTAAAR, COMO LOGRAR HACER UN CARTON DE SOLO 12 NROS, HACE FALTA ACLARAR QUE LA LISTA ES DE SOLO 12 NROS?

def jugar_carton_de_bingo (carton: list[int], bolillero: Cola[int]) -> int:
    cantSinMarcar: int = len (carton)
    temp = []
    res = 0

    while cantSinMarcar > 0: # no hace falta ver si bolillero esta vacio
        bolilla: int = bolillero.get()
        temp.append(bolilla)
        if bolilla in carton: 
            cantSinMarcar -=1
        res += 1

    for num in temp: # regenero el bolillero
        bolillero.put(num)

    return res 
    
carton=[0,99]
b = armar_secuencia_bingo2()
print("Para ganar la cantidad de jugadas es ",jugar_carton_de_bingo(carton, b))

#me da el error de que int no es subscriptable
def n_pacientes_urgentes(c: Cola[(int, str, str)]) -> int:
    res: int = 0
    aux: list[(int, str, str)] = []
    while not c.empty():
        paciente: (int, str, str) = c.get()
        aux.append(paciente)
        if paciente[0] <= 3:
            res += 1
    for elem in aux:
        c.put(elem)
    return res

cola_todos_urgentes = Cola()
cola_todos_urgentes.put((1, "Paciente A", "Cardiología"))
cola_todos_urgentes.put((2, "Paciente B", "Neurología"))
cola_todos_urgentes.put((3, "Paciente C", "Pediatría"))
cola_todos_urgentes.put(1, "Paciente D", "Traumatología")


print(n_pacientes_urgentes2(cola_todos_urgentes))


"""
from queue import LifoQueue as Pila 
from queue import Queue as Cola
import random

def pertenece1(s:list, e) -> bool: 
    i:int = 0 
    while i < len(s):
        if s[i] == e:
            return True
        i += 1
    return False

def armar_secuencia_bingo2() -> Cola[int]:
    secuencia: Cola = Cola()
    elementos:list[int] = list(range(100)) # Pero se puede usar range()? igualmente sería una lista del 0 al 99
    random.shuffle(elementos) #

    #for i in range(12):
    #    algo .. <-- elementos[i]

    for elemento in elementos:
        secuencia.put(elemento)
    return secuencia

#print(de_cola_a_lista(armar_secuencia_bingo2()))



def jugar_carton_de_bingo (carton: list[int], bolillero: Cola[int]) -> int:
    cantSinMarcar: int = len (carton)
    temp = []
    res = 0

    while cantSinMarcar > 0: # no hace falta ver si bolillero esta vacio
        bolilla: int = bolillero.get()
        temp.append(bolilla)
        if bolilla in carton: 
            cantSinMarcar -=1
        res += 1

    for num in temp: # regenero el bolillero
        bolillero.put(num)

    return res 
    
#carton=[0,99] ESTO ESTA MAL

def armar_carton() -> list[int]:
    carton:list = []
    elementos:list[int] = list(range(100))
    random.shuffle(elementos)
    for i in range(12):
        carton.append(elementos[i])
    return carton 

print(armar_carton())


b = armar_secuencia_bingo2()
c = armar_carton()
print("Para ganar la cantidad de jugadas es ",jugar_carton_de_bingo(c, b))


#me da el error de que int no es subscriptable
def n_pacientes_urgentes(c: Cola[tuple[int, str, str]]) -> int:
    res: int = 0
    aux: list[(int, str, str)] = []
    while not c.empty():
        paciente: tuple [int, str, str] = c.get()
        aux.append(paciente)
        if paciente[0] <= 3:
                res += 1
    for elem in aux:
        c.put(elem)
    return res

cola_todos_urgentes = Cola()
cola_todos_urgentes.put((1, "Paciente A", "Cardiología"))
cola_todos_urgentes.put((2, "Paciente B", "Neurología"))
cola_todos_urgentes.put((3, "Paciente C", "Pediatría"))
cola_todos_urgentes.put((1, "Paciente D", "Traumatología"))


print(n_pacientes_urgentes(cola_todos_urgentes))


def invertida(l:list[int]) -> list[int]:
    invertida:list[int] = []
    i  = len(l) - 1
    while i >= 0:
        invertida.append(l[i])
        i -= 1
    return invertida
    
l = [1,2,3,4,5,6]

print (invertida(l))


"""
    requiere: {No hay valores en horas que sean listas vacías}
    asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
    asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
    asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
"""
"""     
def empleados_del_mes(horas: dict[int,list[int]])->list[int]:
    lista_empleados_del_mes:list[int]= []
    maximo:int = 0
    lista_id = list[horas.keys()]
    lista_de_listahoras = list[horas.values()]
    lista_horas_sumadas = horas_hechas
"""

"""
    for id in horas.keys():
        id[horas] = horas_hechas(horas)
        if maximo < horas:
            maximo = horas
            lista_empleados_del_mes.append(maximo)
    return lista_empleados_del_mes
    """
ESTA RARO, NO ANDA LO DE EMPLEADOS DEL MES, REHACER

def horas_hechas(lista:list[int])->int:
    res:int = 0 
    i:int = 0
    while i < len(lista):
        res +=lista[i]
        i += 1
    return res 
print('horas_hechas es ',horas_hechas([2,2,2]))

def maximo(lista:list[int])->int:
    res: int = 0
    for i in lista:
        if res < i:
            res = i
    return res

print('el max es ', maximo([1,2,3]))

 

dict = {1:'hola',2:'hol',3:'ola'}
print(list(dict.values()))
"""
#-------------------------------------------------------------------------------------------------------------------------------------DICCIONARIOS, SOLO EJ 22 Y 23
#EJ 22
from queue import Queue as Cola
import random
from queue import LifoQueue as Pila

historiales: dict = {}

def visitar_sitio(historiales:dict, usuario:str, sitio:str) -> None:
    if not usuario in historiales:
         historiales[usuario] = Pila ()
        
    for usuario in historiales.keys():
         historiales[usuario].put(sitio)
        
    return historiales

print(visitar_sitio(historiales, "anita", "Sitio1"))
print(visitar_sitio(historiales, "marcos", "Sitio1"))
print(visitar_sitio(historiales, "anita", "Sitio3"))
print(visitar_sitio(historiales, "marcos", "Sitio2"))
"""
#print(navegar_atras(historiales, "anita"))
#print(navegar_atras(historiales, "marcos"))
"""

def navegar_atras(historiales:dict, usuario:str) -> None:
    for pilas in historiales.values():
        paux = Pila()
        while not pilas.empty():
            p:Pila[str] = historiales[usuario]
            sitio_actual:str = p.get()
            sitio_anterior:str = p.get()
            paux.put(sitio_actual)
            paux.put(sitio_anterior)
        while not paux.empty():
            pilas.put(paux.get())
    return historiales
#----------------------------------------------------------------------------------VERSION TOMAS, OSEA ANDA PERO ES MUYY RARA
#EJ 22
from queue import LifoQueue as Pila

"""
historiales: dict = {}

def visitar_sitio(historiales:dict, usuario:str, sitio:str):
    if not usuario in historiales:
        historiales[usuario] = Pila()
    
    for usuario in historiales.keys():
      historiales[usuario].put(sitio)
    

#Cambiar la pila por lista para probar con los siguientes casos
#print(visitar_sitio(historiales, "anita", "Sitio1"))

#print(visitar_sitio(historiales, "anita", "Sitio3"))

"""
#print(navegar_atras(historiales, "anita"))
#print(navegar_atras(historiales, "marcos"))
"""

def navegar_atras(historiales:dict, usuario:str) -> None:
    for pilas in historiales.values():
        paux = Pila()
        while not pilas.empty():
            p:Pila[str] = historiales[usuario]
            sitio_actual:str = p.get()
            sitio_anterior:str = p.get()
            #paux.put(sitio_actual)
            #paux.put(sitio_anterior)
            pilas.put(sitio_actual)
            pilas.put(sitio_anterior)

def navegar_atras(historiales:dict, usuario:str) -> None:
   for user in historiales.keys():
      if user == usuario:
          p:Pila[str] = historiales[user]
          sitio_actual:str = p.get()
          sitio_anterior:str = p.get()
          historiales[user].put(sitio_actual)
   

#LOS BENDITOS CASOS DE TEST
visitar_sitio(historiales, "marcos", "Sitio1")
visitar_sitio(historiales, "marcos", "Sitio2")
print(historiales["marcos"].queue)
navegar_atras(historiales, "marcos")
print(historiales["marcos"].queue)

#-------------------------------------------------------------------------------------------

#23
"""
1. Implementa una funcion llamada agregar producto(inout inventario, in nombre, in precio, in cantidad) que
permita agregar un nuevo producto al inventario. El nombre del producto debe ser la clave del diccionario, y el valor debe
ser otro diccionario con las claves “precio” y “cantidad”. Como requisito de esta funcion el producto a agregar no esta en
el inventario.
2. Implementa una funcion llamada actualizar stock(inout inventario, in nombre, in cantidad) que permita actua-
lizar la cantidad de un producto existente en el inventario.
3. Implementa una funcion llamada actualizar precios(inout inventario, in nombre, in precio) que permita actua-
lizar el precio de un producto existente en el inventario.
4. Implementa una funcion llamada calcular valor inventario(in inventario) → float que calcule el valor total del
inventario multiplicando el precio por la cantidad de cada producto y sumando los valores de todos los productos.
"""
inventario = {}

def agregar_producto (inventario: dict, nombre:str, precio : int, cantidad:int)-> dict[str,dict[str,int]]:
    #dictAux : dict [str,int]= {}
    if not nombre in inventario:
        inventario[nombre] = {'precio':precio, 'cantidad':cantidad}
    return inventario

def actualizar_stock (inventario:dict,nombre:str, cantidad:int)-> dict[str,dict[str,int]]:
    for producto in inventario:
        if producto == nombre:
            inventario[nombre]['cantidad']= cantidad
    return inventario

def actualizar_precios (inventario:dict,nombre:str, precio:int)-> dict[str,dict[str,int]]:
    for producto in inventario:
        if producto == nombre:
            inventario[nombre]['precio']= precio
    return inventario
    
def calcular_inventario (inventario:dict[str,dict[str,int]])-> float:
    res:float=0
    cantidad: float
    precio:float
    for nombre in inventario:
        cantidad=float(inventario[nombre]['cantidad'])
        precio=float(inventario[nombre]['precio'])
        res += float(cantidad*precio)
    return res 



item1 = input ("el item1 es: ")
precio1 = input ("el item1 vale: ")
cantidad1 = input ("cantidad del item1: ")
item2 = input ("el item2 es: ")
precio2 = input("el item2 vale: ")
cantidad2 = input ("cantidad del item2: ")
agregar_producto(inventario, item1, precio1, cantidad1)
agregar_producto(inventario, item2, precio2, cantidad2) 
"""
print("el inventario es: ", inventario)
nombre = input("Actualizo el stock de ")
cantidad = input ("Ahora tengo: ")
print("ahora el stock es :", actualizar_stock(inventario,nombre,cantidad))
nombre = input("Actualizo el precio de ")
precio = input ("Ahora vale: ")
print("ahora el producto vale :", actualizar_precios(inventario,nombre,precio))
"""
print("el valor del inventario es : ", calcular_inventario(inventario))




