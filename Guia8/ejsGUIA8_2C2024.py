# 1) PILAS

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
cantidad = 5 
desde = 1 
hasta = 10
p = generar_nros_al_azar(cantidad,desde,hasta) 
impresora(p) 

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

cantidad = 5
desde = 1
hasta = 10
p:Pila[int] = Pila()
p = generar_nros_azar (cantidad, desde, hasta)
mostrar_elems_pila(p)
print ("Mostrar de nuevos eltos pila")





# ej 1.3 buscar_el_maximo
def buscar_el_maximo(c : Pila [int]) -> int:
    maximo: int = 0
    paux:Pila[int] = Pila()
    while not c.empty():
        elem: int = c.get()
        paux.put(elem)
        if elem > maximo:
            maximo = elem
    while not paux.empty():
        e:int = paux.get()
        c.put(e)
        #c.put(paux.get())
    return maximo

def buscar_el_maximo_v2(c : Pila [int]) -> int:
    paux:Pila[int] = Pila()
    if not p.empty():
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

c = Pila()
c.put(-1)
c.put(-2)
c.put(-3)
c.put(-7)
c.put(-3)
c.put(-4)
print("el maximo es ",buscar_el_maximo(c))
print("el maximo_v2 es ",buscar_el_maximo_v2(c))


# 2)COLAS

#ej 2.13 armar_secuencia_bingo() 
from queue import Queue as Cola
def armar_secuencia_bingo() -> Cola[int]:
    cola: Cola[int] = Cola()
    lista: list[int] = list(range(0,10))
    random.shuffle(lista)
    #print("el largo de la lista es: ", len(lista))
    #print(lista)
    for i in range(len(lista)):
        cola.put(lista[i])
    return cola

def mostrar_elems_cola(p:Pila[int]): #in
    paux:Pila[int] = Cola()
    while not p.empty():
        elem: int = p.get()
        print(elem)
        paux.put(elem)
    while not paux.empty():
        e:int = paux.get()
        p.put(e)

bolillero: Cola[int] = armar_secuencia_bingo()
mostrar_elems_cola(bolillero)

# 3) DICCIONARIOS 

#ej 3.16 agrupar_por_longitud 
def lista_palabras (linea: str) -> list[str]:
    res: list[str] = []
    palabra_en_construccion = ""
    for letra in linea:
        if letra != " " or "\n":
            palabra_en_construccion = palabra_en_construccion + letra
        else:
            if len(palabra_en_construccion) > 0:
                res.append(palabra_en_construccion)
                palabra_en_construccion = ""
    res.append(palabra_en_construccion)
    return res

def agrupar_por_longitud(nombre_archivo : str) -> dict:
    res: dict[int, int] = dict()
    palabras: list [str] = lista_palabras(nombre_archivo)
    for palabra in palabras:
        long: int = len(palabra)
        if long in res.keys():
            res[long] += 1
        else:
            res[long] = 1
    return res

palabras = agrupar_por_longitud("/home/Estudiante/Descargas/hola.txt")
print(palabras)

"""
    archivo: TextIO = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    for linea in lineas:
        for palabra in linea:
            if not len(palabra) in res:
                res [len(palabra)] = 1
            else:
                res [len(palabra)] += 1
    return res
palabras = agrupar_por_longitud("/home/Estudiante/Descargas/hola.txt")
print(palabras)
"""

def obtener_palabras(texto: str) -> list[str]:
    res: list[str] = []
    palabra: str = ""
    for char in texto:
        if char != " " and char != "\n":
            palabra += char
        else:
            if palabra != "":
                res.append(palabra)
            palabra = ""
    if palabra != "":
        res.append(palabra)
    return res
print(agrupar_por_longitud("/home/Estudiante/Descargas/hola.txt"))


#OTRA FORMA DE PENSAR EL 16
def agrupar_por_long (nombre_archivo: str):
    res: dict [int, int] = {}
    archivo = open(nombre_archivo, "r")
    texto: str = archivo.read()
    archivo.close()
    palabras: list [str] = obtener_palabras(texto)
    for palabra in palabras:
        long = len(palabra)
        if long in res.keys():
            res[long] += 1
        else:
            res[long] = 1
    return res




# 4) ARCHIVOS

#ej 4.21 contar_lineas
def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo, "r")
    longitud = archivo.readlines()
    archivo.close()
    return len(longitud)

cant_lineas = contar_lineas("/home/Estudiante/Descargas/hola.txt")
print(cant_lineas)


