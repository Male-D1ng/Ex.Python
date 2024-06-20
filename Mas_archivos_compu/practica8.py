#practica8.py
#ARCHIVOS = A, PILAS = P, COLAS = C, DICCIONARIOS = D

import random
import numpy as np
from queue import LifoQueue as Pila
from queue import Queue as Cola

#EJ1_PARTE_A

def contarlineas1 (nombre_archivo: str) -> int:
    file = open(nombre_archivo, "r") #abro el archivo en modo read,'r'
    lineas: list[str] = file.readlines() #readlines lee las lineas del archivo  y las devuelve como una lista
    file.close() #cierro el archivo
    return len(lineas) #en el print el nombre_archivo va entre comillas


def contarLineas(contenido: str) -> int:
    count:int = 1
    for i in range(len(contenido)):
        if contenido[i] == '\n': # el '\n' implica un salto de linea
            count+=1
    return count

archivo = open("archivos.txt","r",encoding="utf8")
contenido: str = archivo.read()
print("la cantidad de lineas es:",contarLineas(contenido))

def existe_palabra (palabra : str,  nombre_archivo : str) -> bool:
    file = open (nombre_archivo, 'r')
    for lineas in file.readlines():
        palabras : list[str] = lineas.split() #parte las lineas en palabras
        if palabra in palabras:
            return True

    file.close()
    return False 

def existePalabra(palabra:str, archivo:str) -> bool: 
    archivo = open(archivo,"r",encoding="utf8")

    for linea in archivo.readlines():
        listaDePalabras: list[str] = linea.split(" ")
        if palabra in listaDePalabras:
            return True
        
    archivo.close()
    return False

# rECORDAR Q : a la iz del print va la palabra y a la der el nombre del archivo
palabra: str = "bien"
print(existePalabra(palabra,"archivos.txt")) 

def cantidad_apariciones (nombre_archivo : str, palabra : str) -> int: 
    contador: int = 0
    archivo= open(nombre_archivo,'r')
    for linea in archivo.readlines():
        total_palabras = linea.split() 
        #split() divide las palabras usando espacios en blanco como delimitadores
        for p in total_palabras:
            if p.strip() == palabra:
 #elimina espacios en blanco u otros caracteres de espaciado al principio y al final de una cadena
                contador += 1
    archivo.close
    return contador

palabra: str = "tambien"
print(cantidad_apariciones('archivos.txt',palabra))


#como usar split y strip
#entrada = input("Ingresa una cadena: ")
#cadena_limpia = entrada.strip()
#separar = cadena_limpia.split()
#print(separar)

#EJ2_PARTE_A

def clonar_sin_comentarios(nombre_archivo : str):
    # Abro el archivo para leer
    archivo = open(nombre_archivo, "r")
    # Abro el archivo en el que voy a escribir
    arch_sin_comentarios = open("clonadoSinComentarios.txt", "w")
    # Leo todas las líneas
    lineas = archivo.readlines()
    for linea in lineas:
        # Si no una línea NO comienza con # entonces la escribo
        # if not linea.lstrip().startswith("#"):
        if not linea.strip()[0] == "#":
            arch_sin_comentarios.write(linea)
    archivo.close()
    arch_sin_comentarios.close()

clonar_sin_comentarios("archivos.txt")

#EJ8_PARTE_P

from queue import LifoQueue as Pila
p = Pila ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # vacia ?
#funci´on random.randint(< desde >, < hasta >) 
#def generar_nros_azar( n : int, desde : int, hasta : int) -> Pila:
#    return random.randint (5,20)


#ejemplo PARA INICIADOS EN LAS PILAS POR GIT

# Creamos una lista vacía para representar la pila
pila = []

# Agregamos elementos a la pila utilizando el método append()
pila.append(1) #append() es lo mismo q put
pila.append(2)
pila.append(3)

# Mostramos la pila actual
print("Pila actual:", pila)

# Eliminamos elementos de la pila utilizando el método pop() == get()
elemento = pila.pop()
print("Elemento eliminado:", elemento)

# Mostramos la pila después de la eliminación
print("Pila después de eliminar un elemento:", pila)

import random
from queue import LifoQueue 
def generar_numeros_azar(n, desde, hasta) -> Pila:
    pila = LifoQueue()  # Creamos una pila vacía

    for x in range(n):
        numero_azar = random.randint(desde, hasta)
        pila.put(numero_azar)  # Agregamos el número a la pila

    return pila

# Ejemplo de uso
n = 5  # Número de elementos en la pila
desde = 1  # Valor mínimo
hasta = 100  # Valor máximo

pila_azar = generar_numeros_azar(n, desde, hasta)

# Mostramos los números de la pila
while not pila_azar.empty():
    numero = pila_azar.get()
    print('los numeros son: ',numero)

#EJ9_PARTE_P

# ejemplo de Pila

from queue import LifoQueue as Pila

p = Pila ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # vacia ?


# contar elementos de una pila

def cantidadElementos(p: Pila) -> int:
    res: int = 0
    paux: Pila = Pila()

    while not p.empty():
        elem = p.get()
        paux.put(elem)
        res = res + 1
    
    while not paux.empty():
        elem = paux.get()
        p.put(elem)
        
    return res


# version con especificacion que garantiza que la pila no es vacia
# Ejemplo de uso
mi_pila = LifoQueue()
mi_pila.put(1)
mi_pila.put(2)
mi_pila.put(3)

cantidad = cantidadElementos(mi_pila)
print("Cantidad de elementos en la pila:", cantidad)


#EJ13_PARTE_C

#ejemplo 1
#c = Cola ()
#c . put (1) # encolar
#elemento = c . get () # desencolar ()
#c . empty () # vacia ?

from queue import Queue as Cola
import random
"""def  generar_nros_al_azar_1(c:int,desde:int,hasta:int)-> Cola:
    #generar y llenar cola
    cola = Cola () 
    for y in range(c):
        res = random.randint(desde,hasta)
        cola.put(res) 

    #recorrer cola e imprimir valores
    while not cola.empty():
        numero = cola.get()
        print('los nuevos numeros son: ',numero)"""
     

#ejemplo 2
def  generar_nros_al_azar2(c:int,desde:int,hasta:int)-> Cola:
    cola = Cola () 
    for y in range(c):
        res = random.randint(desde,hasta)
        cola.put(res) 
    return cola

c = 5
desde = 5
hasta = 100

cola_azar = generar_nros_al_azar2(c,desde,hasta)

while not cola_azar.empty():
    numeros = cola_azar.get()
    print('los nuevos numeros son',numeros)

# contar elementos de una cola

#EJ14_PARTE_C
def cantidadElementos(c: Cola) -> int:
    res: int = 0
    caux = Cola()

    while not c.empty():
        elem = c.get()
        caux.put(elem)
        res = res + 1
    
    while not caux.empty():
        elem = caux.get()
        c.put(elem)
        
    return res


# version con especificacion que garantiza que la pila no es vacia

#EJ19_PARTE_D
#ej19: Leer un archivo de texto y agrupar la cantidad de palabras de acuerdo a su longitud


# diccionario

def agruparPorLongitud(nombre_archivo : str) -> dict:
    archivo = open(nombre_archivo, "r")
    d: dict = {} # inicializando/creando el diccionario

    for linea in archivo.readlines(): # ['a hola chau\n', 'otra linea\n']
        palabras = linea.split()      # ['a', 'hola', 'chau']
        for palabra in palabras:
            clave = len(palabra)
            if clave in d:
                # la clave ya existe
                # entonces incremento en 1
                # el valor
                d[clave] = d[clave] + 1
            else:
                # la clave no existe
                # la creo
                d[clave] = 1
    
    archivo.close()
    return d

print("se lee como cantidad_palabras:longitud",agruparPorLongitud("archivo_palabras.txt"))

#EJ7_PARTE_A
import csv
#el archivo csv se ve como : nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
def contarlineas (lu : str) -> float:
    #primero abro el archivo
    archivo=open("notas.csv",'r')
    #lo leo
    leo_archivo=archivo.readlines()
   #NO HACE FALTA PARA CSV : saco_ceros = leo_archivo.strip()
    #NO HACE FALTA PARA CSV: creo_lineas = saco_ceros.split ()
    archivo.close()
    return len (leo_archivo)

def promedioEstudiante(lu: str) -> float:
    # Inicializamos variables para llevar el total y la cantidad de notas
    total_notas = 0
    cantidad_notas = 0
    
    # Abrir el archivo CSV
    archivo = open ('notas.csv','r')
     # Leer el contenido del archivo
    contenido = archivo.read()
    lista:list = contenido.split('\n')
        # Iterar a través de las filas del archivo CSV
    for fila in lista:
            if len(fila) == 4 and fila[0] == lu:
                # Verificar si la fila tiene 4 index/elementos
                # y si coincide con el número de LU proporcionado
                nota = float(fila[3])  # La nota es la cuarta columna (índice 3)
                total_notas += nota
                cantidad_notas += 1
        # Calcular el promedio final
    if cantidad_notas > 0:
        promedio = total_notas / cantidad_notas
        return promedio
    else:
        return 0.0  # Devolver 0 si no se encontraron notas
    

#EJ20_PARTE_D
#diccionario {libreta universitaria : promedio} con los promedios de todos los alumnos

import csv

def apariciones(notas:list[str], alumno:str) -> int:
    apariciones:int = 0
    for nota in notas:
        campos = nota.split(',')
        if campos [0] == alumno:
            apariciones += 1
    return apariciones

def promedio_estudiante(lu: str) -> dict:
    # Abrir el archivo CSV
    archivo = open ('notas.csv','r')
     # Leer el contenido del archivo
    contenido = archivo.read()
    lista:list = contenido.split('\n')
    #creo un diccionario
    d : dict = {} 
        # Iterar a través de las filas del archivo CSV
    for nota in lista:
         campos = nota.split(',') #quiero poder acceder a cada campo q compone una nota
         if campos[0] in d:
            d[campos[0]] += float(campos[3]) #voy acumulando las notas
         else:
            d[campos[0]] = float(campos[3]) #siempre q llamamos al campo donde esten las notas le hardcodeamos el tipo float ya que por defecto en los csv viene como str
    
    for alumno in d.keys(): #recorro cada alumno y calculo su promedio
        if apariciones(lista,alumno) != 0:
            d[alumno] = float(d[alumno]) / apariciones(lista,alumno) #el divisor del promedio es la cant. de apariciones en las notas
        else:
            d[alumno] = -1
    
    return d

print("USANDO EL EJ DE UN COMPA: ",(promedio_estudiante("notas.csv")))


#EJ3_PARTE_A

# problema invertirTexto(in nombreArchivo: string, archivoDestino: string) {
    # requiere: existe el archivo origen
    # asegura: se crea un archivo llamado archivoDestino cuyo contenido será el resultado
    #              de hacer un reverse en cada una de sus filas
    # asegura: si el archivo archivoDestino existia, se borrará todo su contenido anterior
# }

#LITERAL INVIERTE Y LO DEVUELVE TIPO ESPEJO Y EN REVERSO
def invertirTexto(archivoOrigen: str, archivoDestino: str):
    contenido = []
    archivo = open(archivoOrigen, "r", encoding='utf8')

    for linea in archivo.readlines():
        contenido.insert(0, linea)

    archivo.close()

    destino = open(archivoDestino, "w", encoding='utf8')
    destino.truncate() #Borra todo el contenido de un archivo

    for linea in contenido:
        linea = linea [::-1] #Esto se llama slicing: permite extraer una subcadena linea[inicio:fin:paso] [::-1] extrae todo de atras para adelante
        destino.write(linea)

    destino.close()


#ESTE ESTA BIEN BIEN
def reverso(nombre_archivo:str) -> str:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.readlines()
    contenido_reverso = []
    for i in range(0,len(contenido)):
        contenido_reverso.append(contenido[-1-i])
    reverso = open('reverso.txt', 'w', encoding='utf8')
    for linea in contenido_reverso:
        reverso.writelines(linea)
    archivo.close()
    reverso.close()

reverso('archivo_de_prueba.txt')

#EJ4-PARTE_A

def agrega_frase(nombre_archivo:str, frase:str) -> str:
    archivo = open(nombre_archivo, 'a')
    archivo.write('\n' + frase)
    archivo.close()
# print(agrega_frase('archivo_palabras.txt', 'esto es una frase'))

#EJ21_PARTE_D

def frecuencias(nombre_archivo : str) -> dict:
    archivo = open(nombre_archivo, "r",encoding='utf8')
    d: dict = {} # inicializando/creando el diccionario

    for linea in archivo.readlines(): # ['a hola agruparPorLongitud\n', 'otra linea\n']
        palabras = linea.split()      # ['a', 'hola', 'chau']
        for palabra in palabras:
            if palabra in d:
                # la palabra ya existe
                # entonces incremento en 1 la cantidad de apariciones
                d[palabra] = d[palabra] + 1
            else:
                # aparece por primera vez palabra
                # la agrego al diccionario
                d[palabra] = 1

    archivo.close()
    return d
    

def laPalabraMasFrecuente(nombre_archivo : str) -> str:
    d = frecuencias(nombre_archivo)
    palabraMasFrecuente: str
    frecuenciaMax: int = 0
    
    for palabra, frecuencia in d.items():
        if frecuencia > frecuenciaMax:
            frecuenciaMax = frecuencia
            palabraMasFrecuente = palabra
    
    return palabraMasFrecuente

print('la palabra mas frecuente es: ' + laPalabraMasFrecuente("archivo_palabras.txt"))

#EJ5_PARTE_A
def agrega_frase_principio (nombre_archivo,frase:str)->str:
    #primero abrir el archivo
    archivo = open (nombre_archivo,'r')
    #leo el contenido y lo cierro
    lineas = archivo.read()
    archivo.close()
    # ya leido lo puedo 'actualizar'
    nuevo_contenido = frase + '\n' + lineas
    #re abro el archivo y ahora si escribo la frase 
    file = open(nombre_archivo,'w')
    file.write (nuevo_contenido)
    file.close()
     
#EJ6_PARTE_A

    

    






    
        
        

