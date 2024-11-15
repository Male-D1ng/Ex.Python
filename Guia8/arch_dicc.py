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

inventario1:dict[str,dict[str,int]]= {"camisa roja" : {"Precio" : 5000, "Cantidad" : 10}, "jean oscuro": {"Precio" : 7000,"Cantidad" : 10}}


def agregarProducto(inventario:dict[str,dict[str,int]],nombre:str,precio:int,cantidad:int) -> dict[str,dict[str,int]]:        
    d:dict[str,int] = {"Precio" : 0,"Cantidad" : 0}
    d["Precio"] += precio
    d["Cantidad"] += cantidad
    inventario[nombre] = d
    return inventario

#print(agregarProducto(inventario1,"jean",5000,5))

def actualizarStockYPrecio(nombre:str,precio:int,cantidad:int) -> dict[str,dict[str,int]]:
    if nombre in inventario1:
        inventario1[nombre]["Precio"] = precio
        inventario1[nombre]["Cantidad"] = cantidad
        return inventario1
    else:
        return "El producto no esta en el inventario"
    
#print(actualizarStockYPrecio("camisa roja",7000,5))

def calcularValorInventario(inventario:dict[str,dict[str,int]]) -> float:
    valorInventario:int=0
    for nombre, cantidadPrecio in inventario.items():
        precio= inventario[nombre]["Precio"]
        cantidad= inventario[nombre]["Cantidad"]
        producto= precio * cantidad
        valorInventario += producto
    return valorInventario


#print(calcularValorInventario(inventario1))
