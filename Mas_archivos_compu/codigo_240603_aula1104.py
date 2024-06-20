from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# EJERCICIO 13 ####################################################################################
def generar_nros_al_azar (cantidad: int, desde: int, hasta: int) -> Pila [int]:
    p: Pila [int] = Pila ()

    for i in range (cantidad): # es solo para repetir cantidad de veces el cuerpo del for
        num: int = random.randint(desde, hasta)
        p.put(num)

    return p

def generarCola (cantidad: int,  desde: int, hasta: int) -> Cola [int]:
    p: Pila [int] = generar_nros_al_azar (cantidad, desde, hasta)
    c: Cola [int] = Cola()

    while not p.empty():
        num: int = p.get()
        c.put(num)

    return c

# EJERCICIO 16 ######################################################################
# 1
def armar_secuencia_de_bingo () -> Cola[int]:
    listaDeBolillas: list [int] = []
    for bolilla in range (100):
        listaDeBolillas.append(bolilla)

    random.shuffle(listaDeBolillas) # mesclamos la listaDeBolillas.

    bolillero: Cola [int] = Cola()
    for b in listaDeBolillas: # b son las bolillas que voy a meter en la cola bolillero
        bolillero.put(b)

    return bolillero

# 2
def jugar_carton_de_bingo (carton: list[int], bolillero: Cola[int]) -> int:
    cantSinMarcar: int = len (carton)
    temp: list [int] = []

    while cantSinMarcar > 0: # no hace falta ver si bolillero esta vacio
        bolilla: int = bolillero.get()
        temp.append(bolilla)
        if bolilla in carton: # Vamos a permitir que usen in en listas también. <---
            cantSinMarcar -=1

    jugadas: int = len (temp)

    while not bolillero.empty(): # vacio por completo el bolillero
        temp.append(bolillero.get())

    for num in temp: # regenero el bolillero
        bolillero.put(num)

    return jugadas

# EJERCICIO 19 ##################################################################
def agrupar_por_longitud (nombre_archivo: str) -> dict [int, int]:

    file = open (nombre_archivo, "r")
    contenido: str = file.read()
    file.close()

    listaDePalabras: list [str] = separarEnPalabras (contenido) # Ya que no podemos usar .split(), la implementamos.
    diccionario: dict [int, int] = {}

    for palabra in listaDePalabras:
        clave: int = len(palabra)
        if clave in diccionario:
            diccionario[clave] += 1
        else:
            diccionario[clave] = 1

    return diccionario


def separarEnPalabras (texto: str) -> list [str]:
    temp: str = "" # en esta variable voy ir armando y guardando temporalmente cada una de las palabras
    res: list [str] = []
    i: int = 0
    while i < len(texto):
        if esUnEspacio (texto[i]):
            res.append (temp) 
            temp = "" # vacio y dejo temp lista para comenzar a guardar la proxima palabra
            while i < len(texto) and esUnEspacio(texto[i]): # para saltearme varios espacio continuos
                i+=1
        else:
            temp += texto[i]
            i+=1
    return res

def esUnEspacio (c: str) -> bool:
    return c == " " or c == "\n" or c == "\t"

# EJERCICIO 21 ##################################################################
def la_palabra_mas_frecuente (nombre_archivo: str) -> str:

    file = open (nombre_archivo, "r")
    contenido: str = file.read()
    file.close()

    listaDePalabras: list [str] = separarEnPalabras (contenido)
    diccionario: dict [str, int] = {}

    for palabra in listaDePalabras:
        clave: int = palabra
        if clave in diccionario:
            diccionario[clave] += 1
        else:
            diccionario[clave] = 1

    palabraMasFrecuente: str
    maximaFrecuencia: int = 0

    for palabra, frecuencia in diccionario.items():
        if frecuencia > maximaFrecuencia:
            maximaFrecuencia = frecuencia
            palabraMasFrecuente = palabra

    return palabraMasFrecuente

