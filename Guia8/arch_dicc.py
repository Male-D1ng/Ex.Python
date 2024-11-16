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

#FUNCION RE IMPORTANTE ; PERTENECE PARA DICCIONARIOS
def pertenece(elem:str,lista:list[str])->bool:
    res:bool=False
    for x in lista:
        if x == elem:
            res = True
    return res

def calcular_promedio_por_estudiante (boletin:list[tuple[str,float]])->dict[str,float]:
    promedios_estudiante:dict[str,float] = {}
    
    for estudiante in boletin:
        if not pertenece(estudiante[0],promedios_estudiante.keys()):
            calcular_promedio: float = promedio(estudiante[0],boletin)
            promedios_estudiante [estudiante[0]] = calcular_promedio #le asigno a ese estudiante el promedio
        
    return promedios_estudiante

def promedio(estudiante:str,numeros:list[tuple[str,float]])-> float:
    longitud = 0
    suma = 0
    for notas in numeros:
        if notas[0] == estudiante:
            suma = suma + notas[1]
            longitud = longitud + 1

    return suma/longitud

notas = [["p1",2],["p2",5],["p1",6],["p3",10],["p3",10]]
print(calcular_promedio_por_estudiante(notas))


#ej 18 diccionarios : la palabra mas frecuente

#FUNCION MUY IMPORTANTE PARA ARCHIVOS Y DICCIONARIOS
def obtener_palabras(texto: str) -> list[str]: # supongamos que las palabras están sólo separadas por espacios (o saltos de línea)
    palabras: list[str] = []
    palabra_actual: str = ''
    for c in texto:
        if c == ' ' or c == '\n':
            if palabra_actual != '':
                palabras.append(palabra_actual)
                palabra_actual = ''
        else:
            palabra_actual += c
    if palabra_actual != '':
        palabras.append(palabra_actual)
    return palabras


def laPalabraMasFrecuente(nombre_archivo : str) -> str:
    archivo = open(nombre_archivo,"r")
    contenido = archivo.read()
    archivo.close()
    listaPalabras :list[str] = obtener_palabras(contenido)
    diccionario :dict[str,int] = {}
    
    for palabra in listaPalabras:
        clave: int = palabra
        if clave in diccionario:
            diccionario[clave] +=1
        else:
            diccionario[clave] = 1
    
    palabraMasFrecuente :str = ""
    maximaFrecuencia:int = 0

    for palabra,frecuencia in diccionario.items():
        if frecuencia > maximaFrecuencia :
            maximaFrecuencia = frecuencia
            palabraMasFrecuente = palabra
            
    return palabraMasFrecuente

print("la palabra mas frecuente es: ", laPalabraMasFrecuente("archivos_palabras.txt"))

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
    d:dict[str,float | int] = {"Precio" : 0,"Cantidad" : 0}
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
    valorInventario:float=0
    for nombre, cantidadPrecio in inventario.items():
        precio= inventario[nombre]["Precio"]
        cantidad= inventario[nombre]["Cantidad"]
        producto= precio * cantidad
        valorInventario += producto
    return valorInventario

print(inventario1)
print(calcularValorInventario(inventario1))
