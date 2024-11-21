#clase 23/10 guia 8, uso de pilas colas y diccionarios
# trabajo con archivos en python : para abrirla se usa la funcion open tq open ("nombre", "r") para leerle o para escribirlo ("nombre", "w") 
#lectura de archivos tq : arch.readlines() que devuelve una lista con las lineas del archivo 
#"para leer todo el archivo: arch.read
#escribir : 1°tengo q tener abierto el archivo en modo w, luego arch.write ("..")
#cerrar un archivo : arch.close ()

#ej2 : implementar una funcion que toma un archivo de entrada y genera un nuevo archivo con el mismo contenido pero sin los comentarios
#linea.strip (): funcion de string q quita todos los espacios en blanco adelante y atras

# Abrir un archivo en modo lectura
archivo = open ("archivo.txt","r")
# Leer el contenido del archivo
contenido = archivo.read()
print(contenido)
# Cerrar el archivo
archivo.close()


def ClonarSinComentarios (nombre_archivo : str): 
  archivo = open (nombre_archivo,"r") #archivo q abro para leer, ya existe
  archivo_sin_coment = open ("sinComentarios.py", "w") #archivo q abro para escribir, lo va a crear si no existe
  lineas = archivo.readlines () #funcion q llamo para leer el archivo
  #va un if : mi condicion es q si NO comienza con el # o espacios, escribe la linea --> archivo_sin_coment.write (linea)
  #if not linea.lstrip().startwith("#"): 
  for linea in lineas:
    if not linea.strip () [0] == "#":
      archivo_sin_coment.write (linea)
  archivo.close # lo cierro
  archivo_sin_coment.close #lo cierro
  
ClonarSinComentarios ("archivoComentado.py")

#Pilas y Colas. Pilas: Una pila es una lista de elementos de la cual se puede extraer el ´ultimo elemento insertado, es del tipo lista LIFO, podemos importar el modulo LifoQueue que nos da una implementacion de Pila
#
#pila = LifoQueue()
#Cola: Una cola es una lista de elementos en donde siempre se insertan nuevos elementos al final de la lista y se extraen elementos desde el inicio de la lista. Son listas tipo FIFO
  
#EJ PILA Y COLA
from queue import LifoQueue as Pila
p = Pila()
p.put(1) #apilar
p.put(2) #apilar

print(list(p.queue))
elemento = p.get() #se centra en el ultimo elemento, desapilar: devuelve y quita el ultimo elemento insertado
print(elemento) #desapilar #devuelve la lista menos el ultimo
print(p.empty()) # pregunto si esta vacia 
print(list(p.queue))

#lo mismo es con las Colas tq c = Cola() y se lo lla,a encolar PERO en el c.get() se ecentra en el PRIMER elemento, entonces dps me va devolver una lista SIN EL PRIMER elemento

#ej10 Dada una pila de enteros mplementar una funcion que devuelva el max

def buscar_max (p:Pila) -> int :
  #que la pila no sea vacia
  maximo = p.get()
  while (not p.empty()) :
    elem = p.get()
    if (elem> maximo):
      maximo = elem

  return maximo

print ("el max de la fila es :", buscar_max(p))


#forma profe 2

def buscar_max2 (p:Pila) -> Int:
  #que la pila no sea vacia
  res: int = p.get() #otra forma es q int = None, luego creo un if not.empty(). res = p.get() and paux.put(res)
  paux : Pila = Pila ()

  while not p.empty(): 
    elem: int = p.get()
    paux.put(elem)
    if elem > res:
      res = elem

  while not paux.empty():
    elem = paux.get()
    p.put(elem)

  return res

#ejemplo cantidad de elementos
from queue import Queue as Cola

def cantidadElem (c:Cola) -> int:
  res: int = 0
  caux: Cola = Cola()

  while not c.empty():
    elem = c.get()
    caux.put(elem)
    res = res + 1

  while not caux.empty():
    elem = caux.get()
    c.put(elem)

  return res 


#ej16_Bingo
#armo una lista con los num del 0 al 9
import random #lo haga para poder usar la funcion shuffle, q necesita de random
lista : list = list(range(0,10))
#desordena de forma random la lista
random.shuffle(lista)

#funcion armarSecdeBingo() -> Cola[int] que genere una cola con los num del 0 al 99 desordenados, osea son las bolillas

def armarSecdebingo() -> Cola:
  #armo la lista
  lista: list = list(range(0,99))
  #desordena
  random.shiffle(lista)
  #creo una cola
  bolillas: Cola = Cola() #la cola q representa las bolillas 
  #agrego la lista a la cola
  for elem in lista:
    bolillas.put(elem)

  return bolillas

#funcion que toma un carton de Bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la
#cantidad de jugadas de ese bolillero que se necesitan para ganar.

def jugarCartonDeBingo (carton : list[int], bolillero : cola) -> int:
   #creo el bolillero, funcion parecida a la de armarSecdeBingo, creo un bolillero aux y creo la cantidad de jugadas
   #creo el contador
    cantsinMarcar: int = len(carton)
    jugadas:int = 0
    bolilleroAux: Cola = Cola()
   #mientras no marque todos los numeros del carton saco bolillas
    while cantsinMarcar > 0:
        num:int = bolillas.get()
        bolilleroAux.put(num)
        if num in carton:
          cantsinMarcar -= 1
        jugadas += 1 #ya hice una jugada
  
    while not bolillas.empty():
      num: int = bolillas.get()
      bolilleroAux.put(num)
  
    while not bolilleroAux.empty():
      num: int = bolilleroAux.get()
      bolillas.put(num)
  
    return jugadas


#Diccionarios: Un diccionario es una estructura de datos que permite almacenar y organizar pares clave-valor
#El valor puede ser cualquier tipo de dato, en particular podrıa ser otro diccionario

#archivo = open(”PATH AL ARCHIVO”, MODO, ENCODING)
#Algunos de los modos posibles son: escritura (w), lectura (r), texto (t - es el default), El encoding se refiere a como est´a codificado el archivo: UTF-8 o
#ASCII son los m´as frecuentes

#ej19: Leer un archivo de texto y agrupar la cantidad de palabras de acuerdo a su longitud

def agruparPorLongitud(nombre_archivo : str) -> dict: 
  archivo = open(nombre_archivo,"r")
  d = dict() #me creo un diccionario vacio
  #leo el archivo
  lineas = archivo.readlines()
  for linea in lineas:
    palabras = linea.split() #itero las lineas y creo una lista con las palabras del string
    for palabra in palabras: 
      longitud = len(palabra)
      if (longitud in d): #la longitud es una clave del dic
        d[longitud] += 1 #le sumo 1, xq podria llegar a existir esa clave
      else:
        d[longitud] = 1

  archivo.close()
  return d

#ej21: funcion devuelve la palabra que m´as veces aparece en un archivo de texto.
#puedo transformar la funcion agruparPorLong como un contador de palabras y crear una segunda para poder ir comparando con la anteror palabra y ver si se repite
def laPalabraMasFrecuente (nombre_archivo : str) -> str:
  palabraMasFrec: str
  dict = agruparPorLongitud (nombre_archivo)
  freuenciaMax: int = 0
  for palabra, frecuencia in dict.items(): #items(9 es un par iterador, en cada iteracion palabra la clave se llama palabra y el valor es frecuencia, otra forma es == for palabra in dict.keys(): frecuencia = dict[palabra]
    if (frecuencia > frecuenciaMax):
      frecuenciaMax = frecuencia
      palabraMasFrec = palabra

  return palabraMasFrec
  
print ("la palabra mas frecuente es:", lapalabraMasfrecuente("archivo_palabras.txt"))



