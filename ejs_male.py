#ejs mios 


#ej 20 : actualizar stock de inventario
#inventario1:dict[str,dict[str,int]]= {"camisa roja" : {"Precio" : 5000, "Cantidad" : 10}, "jean oscuro": {"Precio" : 7000,"Cantidad" : 10}}
inventario1 = {}

def agregarProducto(inventario:dict[str,dict[str,float | int]],nombre:str,precio:float,cantidad:int) :#-> dict[str,dict[str,float | int]]:        
    d:dict[str,float | int] = {"Precio" : 0.0,"Cantidad" : 0}
    d["Precio"] += precio
    d["Cantidad"] += cantidad
    inventario[nombre] = d
    return inventario

#print(agregarProducto(inventario1,"jean",5000,5))int
agregarProducto(inventario1,"camisa",20.0,50)
agregarProducto(inventario1,"pantalon",30.0,30)

"""
def actualizarStockYPrecio(diccionario:dict[str,dict[str,float | int]],nombre:str,precio:float,cantidad:int): #-> dict[str,dict[str,float | int]]:
    if nombre in inventario1:
        inventario1[nombre]["Precio"] += precio
        inventario1[nombre]["Cantidad"] += cantidad
        return inventario1
    else:
        return "El producto no esta en el inventario"
"""
def actualizarStockYPrecio(diccionario:dict[str,dict[str,float | int]],nombre:str,precio:float,cantidad:int): #-> dict[str,dict[str,float | int]]:
    for stuff in diccionario:
        if stuff == nombre:
            inventario1[nombre]["Precio"] += precio
            inventario1[nombre]["Cantidad"] += cantidad
            return inventario1
        else:
            return "El producto no esta en el inventario"

#print(actualizarStockYPrecio("camisa roja",7000,5))
actualizarStockYPrecio(inventario1,"camisa",0.0,10)

def calcularValorInventario(inventario:dict[str,dict[str,float | int]]) -> float:
    valorInventario:float=0.0
    for nombre, cantidad in inventario.items():
        precio= inventario[nombre]["Precio"]
        cantidad= inventario[nombre]["Cantidad"]
        producto= precio * cantidad
        valorInventario += producto
    return valorInventario

print(inventario1)
print(calcularValorInventario(inventario1))


#ej 19 diccionarios : historial de navegacion

from queue import LifoQueue as Pila

historiales: dict = {}

def visitar_sitio(historiales:dict[str,Pila[str]], usuario:str, sitio:str):
    if not usuario in historiales:
        p:Pila[str] = Pila()
        historiales[usuario]= p
        
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

"""
print(navegar_atras(historiales, "anita"))
print(navegar_atras(historiales, "marcos"))
"""


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
    promedios_estudiante = {"p1":5}
    print(promedios_estudiante)
    
    for estudiante in boletin:
        if not pertenece(estudiante[0],promedios_estudiante.keys()):
            calcular_promedio: float = promedio(estudiante[0],boletin)
            promedios_estudiante [estudiante[0]] = calcular_promedio #le asigno a ese estudiante el promedio
        else:
            promedios_estudiante[estudiante[0]] = promedio(estudiante[0],boletin)
        
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





