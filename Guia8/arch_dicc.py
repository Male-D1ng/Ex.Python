from typing import TextIO 
import csv
#el archivo csv se ve como : nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
def contarlineas(lu : str) -> int:
    #primero abro el archivo
    archivo=open(lu,'r')
    #lo leo
    leo_archivo=archivo.readlines()
    archivo.close()
    return len(leo_archivo)
print("la cantidad de lineas es :", contarlineas("archivo.txt"))

#agrupar_por_longitud 7 longitud_en_letras:cantidad_de_palabras

def sumar_uno_dicc (palabra:str,diccionario:dict[int,int]):
    if len(palabra) in diccionario.keys():
        diccionario[len(palabra)] +=1
    else:
        diccionario[len(palabra)] = 1

#ej 16 diccionarios: agrupar por longitud
def agrupar_por_longitud (nombre:str)->dict:
    diccionario:dict[int,int] = {}
    archivo:TextIO = open(nombre,'r')
    leo_archivo = archivo.read()
    archivo.close()
    acumulado:str = "" #palabra
    for linea in leo_archivo: #este tipo de in SI esta permitido, NO esta permitida el if linea in algo
        if linea == " " or linea == "\n":
            sumar_uno_dicc(acumulado,diccionario)
            acumulado = ""
        else:
            acumulado += linea

    if acumulado != "" and "\n":
        sumar_uno_dicc (acumulado,diccionario)

    return diccionario

print(agrupar_por_longitud("archivo.txt"))

#ej 17 calcular promedio por estudiante

def calcular_promedio_por_estudiante (boletin:list[tuple[str,float]])->dict[str,float]:
    notas_estudiantes:dict[str,list[int]] = {}
    promedios_estudiante:dict[str,float] = {}

    for estudiante in boletin:
        if estudiante[0] in notas_estudiantes:
            notas_estudiantes[estudiante[0]].append(estudiante[1])
        else:
            notas_estudiantes[estudiante[0]] = [estudiante[0]]
        
    for estudiante,notas in notas_estudiantes.items():
        promedios_estudiante[estudiante] = promedio(notas)

    return promedios_estudiante

def promedio(numeros:list[int])-> int:
    longitud = len(numeros)
    suma = 0

    for numero in numeros:
        suma += numero

    return suma/longitud

#ej 18 diccionarios : la palabra mas frecuente

#ej 19 diccionarios : historial de navegacion

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

print(navegar_atras(historiales, "anita"))
print(navegar_atras(historiales, "marcos"))


#ej 20 diccionarios : actualizar stock

#inventario1:dict[str,dict[str,int]]= {"camisa roja" : {"Precio" : 5000, "Cantidad" : 10}, "jean oscuro": {"Precio" : 7000,"Cantidad" : 10}}
inventario1 = {}

def agregarProducto(inventario:dict[str,dict[str,float | int]],nombre:str,precio:float,cantidad:int) :#-> dict[str,dict[str,float | int]]:        
    d:dict[str,int] = {"Precio" : 0,"Cantidad" : 0}
    d["Precio"] += precio
    d["Cantidad"] += cantidad
    inventario[nombre] = d
    return inventario

#print(agregarProducto(inventario1,"jean",5000,5))
agregarProducto(inventario1,"camisa",20.0,50)
agregarProducto(inventario1,"pantalon",30.0,30)

def actualizarStockYPrecio(diccionario:dict[str,dict[str,float | int]],nombre:str,precio:float,cantidad:int): #-> dict[str,dict[str,float | int]]:
    if nombre in inventario1:
        inventario1[nombre]["Precio"] += precio
        inventario1[nombre]["Cantidad"] += cantidad
        return inventario1
    else:
        return "El producto no esta en el inventario"
    
#print(actualizarStockYPrecio("camisa roja",7000,5))
actualizarStockYPrecio(inventario1,"camisa",0.0,10)

def calcularValorInventario(inventario:dict[str,dict[str,float | int]]) -> float:
    valorInventario:int=0
    for nombre, cantidadPrecio in inventario.items():
        precio= inventario[nombre]["Precio"]
        cantidad= inventario[nombre]["Cantidad"]
        producto= precio * cantidad
        valorInventario += producto
    return valorInventario

print(inventario1)
print(calcularValorInventario(inventario1))
