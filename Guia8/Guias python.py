
# Guia 6 
# Ejercicio 1.1

def imprimir_hola_mundo ():
    print ("¡Hola Mundo!")

imprimir_hola_mundo ()

# Ejercicio 1.2

def imprimir_un_verso ():
    print ("Please don't go")

imprimir_un_verso ()



# Ejercicio 2.5
def es_multiplo_de (n:int, m:int) -> bool :
    return n % m == 0

# Otra forma de hacerlo
def es_multiplo_de_v2 (n:int, m:int) -> bool :
    if n % m == 0 :   # el simbolo % se usa como mod en Haskell ayuda para ver si es divisible 
       return True
    else:
        return False

#Otra forma usando ciclo
def multiplo_de_con_ciclo (n:int, m:int) -> bool:
    for k in range (0,n+1, 1):   # va hasta n+1 porque excluye ese valor y toma el anterior, o sea va hasta n
        if k*m == n:
            return True 
    return False


#Ejercicio 3.3

def es_nombre_largo (nombre: str) -> bool:
    return 3 <= len(nombre) <= 8

print (es_nombre_largo ("Sebastian"))


# otra manera de hacerlo

def es_nombre_largo_v2 (nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8


# Extra hacer funcion que mida cantidad de letras de una palabra, simil al len 

#def cantidad_letras (nombre: str) -> int:
#    for i in nombre 


# Ejercicio 5.1

def devolver_el_doble_si_es_par (numero:int):
    if numero % 2 == 0:
        return numero*2
    else:
        return numero

devolver_el_doble_si_es_par(11)


# Ejercicio 6.2

def imprimir_numeros_pares_entre_10_y_40 () :
    lista = [10]
    k = 10
    while (k < 40):
        k = k+2
        lista.append(k)
    return lista


# otra forma de hacerlo
def pares_entre_10_y_40 ():
    k = 10
    while (k <= 40) :
        if k % 2 == 0:
            print (k)
        k = k + 1 # k = k + 1


# pares_entre_10_y_40 ()

def pares_entre_10_y_40_de_a2 ():
    k = 10
    while (k <= 40) :
        print(k)
        k += 2 # k = k + 2

pares_entre_10_y_40_de_a2()


# ahora lo hago con for, no se podia, era solo con while 
def pares_entre_10_y_40_v2 ():
    for k in range (10,41,2):
        print(k)

pares_entre_10_y_40_v2()

# Ejercicio 6.4
# Pasado un número hacer la cuenta regresiva hasta 1 y que termine con un string que diga "Despegue"

def cuenta_regresiva (n:int) :
    while (n>=1) :
        print(n)
        n= n-1
    print ("Despegue")

cuenta_regresiva (10)

# Ejercicio 7
# Es implementar las del 6 pero con el for num in range (i,f,p) -- ya hicimos el 6.2 --

# Hacemos la parte del 7 que tiene que ver con el 6.5 --



# Ejemplo debugging 

def sumar (var1: int) :
    var2 : int = 8
    suma: int= var1 + var2
    return suma

var :int = sumar (3)



#Ejemplo de Codigo mal hecho para hacer debug ...

def fibonacci_no_recursivo (n:int) -> int:
    if n<= 1:
        return n
    un_fibo: int = 0
    un_fibo_sig : int = 1
    i: int = 2
    while i <= n:
        aux: int = un_fibo + un_fibo_sig
        un_fibo = un_fibo_sig
        un_fibo_sig = aux
        i = i+1
    return un_fibo  # debuggeando nos damos cuenta que el error podia venir por aca, si ponemos return un_fibo_sig da bien el modelo

print (fibonacci_no_recursivo (1))
print (fibonacci_no_recursivo (2))
print (fibonacci_no_recursivo (3))
print (fibonacci_no_recursivo (4))



#Ejemplo para debugging Es primo ...

# def es_primo (n: int) -> bool:
#    cant_divisores: int = 0
#    i : int = 1
#    while i < n and cant_divisores < 2:
#        if n % i == 0:
#            cant_divisores += 1
#            i += 1                 # esto esta mal, esto tiene que estar a la altura del if ...sino hace un loop eterno y no mueve el i 
#    return cant_divisores < 2 and i == n and n != 1 # i == n esta redundante tambien, pero igualmente el resultado da bien ...

#print (es_primo(1))
#print (es_primo(2))
#print (es_primo(3))
#print (es_primo(4))
#print (es_primo(5))
    

# Codigo corregido

def es_primo (n: int) -> bool:
    cant_divisores: int = 0
    i : int = 1
    while i < n and cant_divisores < 2:
        if n % i == 0:
            cant_divisores += 1
            i += 1 
        else: i = 1 + i                
    return cant_divisores < 2 and i == n and n != 1 

print (es_primo(1))
print (es_primo(2))
print (es_primo(3))
print (es_primo(4))
print (es_primo(5))

# Debugging con enesimo primo ...

def buscar_nesimo_primo (n:int) -> int:
    cant_primos: int = 0
    i : int = 2
    while cant_primos < n:
        if es_primo (i):
            cant_primos += 1 # esto esta mal tiene que ser += , es cant_primos = 1 + cant_primos        
    return i 


print (buscar_nesimo_primo(1))
print (buscar_nesimo_primo(2))
print (buscar_nesimo_primo(3))
print (buscar_nesimo_primo(4))
print (buscar_nesimo_primo(5))




# Ejercio por fuera de la guia, dado un input f de filas y un input c de columnas, tener en cuenta que cada posicion de la matriz es si fila es f + c, el resultado debe ser la suma de todos los valores de la matriz ...
# Pienso primero en una sola fila para simplificar el problema ... 
# Hacemos ciclos sobre las columnas

def suma_matriz (f: int, c: int) -> int:
    suma : int = 0
    i : int = 1
    k : int = 1
    while  k <= f:
        while  i <= c:
            suma = i + k + suma
            i = 1 + i
        k = k + 1 
    return suma 


suma_matriz (2,2)



# Guia 7 - Listas 

# Ejercicio 1.1

def pertenece (s:list[int], e:int) -> bool:
    resultado: bool = False
    for i in s:
        if i == e:
            resultado = True
        return resultado
    

def pertenece_2 (s:list[int], e:int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False


def pertenece_3 (s:list[int], e:int) -> bool:
    i: int = 0
    resultado: bool = False
    while i < len(s) and resultado == False:
        resultado = s[i] == e
        i +=1
    return resultado


# Ejercicio 1.3

def suma_total (s:list[int]) -> int:
    suma : int = 0
    for i in range(len(s)):   # el i en rango de len(s) me habla del indice ...
        suma = s[i] + suma  
    return suma

print (suma_total ([1,2,3]))


def suma_total_2 (s:list[int]) -> int:
    suma : int = 0
    for i in s:    # el i en s refiere a los elementos de la lista ...
        suma = i + suma
    return suma

print (suma_total_2 ([1,2,3]))


# Ejercicio 1.4 

def maximo (s:list[int]) -> int:
    max_val :int = s[0]
    for num in s[1:]:      # no esta permitida esta sintaxis en el examen de Python ...
        if num > max_val:
            max_val = num  
    return max_val

print (maximo([1,5,4,2,2,1]))


# Otra manera de hacerlo ...
def maximo_2 (s:list[int]) -> int:
    max_val :int = s[0]
    i: int = 1
    for i in range(len(s)):
        if s[i] > max_val:
            max_val = s[i]  
    return max_val

print (maximo_2([1,5,4,2,2,1]))

# Ejercicio 1.5 
# Encontrar el minimo valor en una lista 
def minimo (s:list[int]) -> int:
    min_val :int = s[0]
    for num in s[1:]:
        if num < min_val:
            min_val = num  
    return min_val

print (minimo ([1,5,4,2,2,1]))


# Ejercicio 1.6
# Ordenados

def ordenados (s:list[int]) -> bool:
    i:int = 0
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

print (ordenados([1,3,5,6,7,8,9]))

print (ordenados([3,1,5,6,7,8,9]))


# Ejercicio 1.7

def max_pos (s:list[int]) -> int:
    max_pos: int = 0
    i:int = 1
    for i in range (len(s)):
        if s[i] > s[max_pos]:
            max_pos = i
    return max_pos

print (max_pos ([1,5,4,2,2,1]))
print (max_pos ([1,2,4,5,2,1]))



# Ejercicio 2.1
# Cero en posiciones pares ...

def cero_en_posiciones_pares (s: list[int]):
    for i in range(len(s)):
        if i % 2 == 0:
           s[i] = 0
    return s

print(cero_en_posiciones_pares([1,2,3,4,5,6]))


# Ejercicio 2.2

def cero_en_posiciones_pares_2 (s: list[int]):
    lista: list[int] = s.copy()
    for i in range(len(lista)):
        if i % 2 == 0:
           lista[i] = 0
    return lista

print(cero_en_posiciones_pares_2 ([1,2,3,4,5,6]))


# Gúia 8


from queue import LifoQueue as Pila
from queue import Queue as Cola
import random


# Ejercicio 8 - Lo hicimos en clase como Pila, en la guia esta como Cola

def nros_al_azar (cantidad: int, desde:int, hasta:int) -> Pila [int]:
    pila: Pila [int] = Pila()
    for i in range (0, cantidad): # si no vamos a usar el i como en este caso que es solo el indice se usa mas el _ (guion bajo)
        elem: int = random.randint(desde, hasta) 
        pila.put (elem)

    return pila

def mostrar_elem_pila (p:Pila[int]) -> None:  
    paux : Pila [int] = Pila ()       # esta auxiliar viene bien para poder conservar la p, por si nos piden que p sea in (no puedo modoficarla)
    while not p.empty() :
        elem: int = p.get()
        print (elem)
        paux.put (elem)
    
    while not paux.empty():
        e: int = paux.get ()
        p.put(e)


cantidad = 5
desde = 1
hasta = 10
p:Pila[int] = Pila ()
p = (nros_al_azar (cantidad, desde, hasta))
mostrar_elem_pila (p)
print (("mostrar de nuevo elementos Pila"))
mostrar_elem_pila (p)


# Ejercicio 10
# Tengo que definir una funcion que me de el valor maximo, conservando la Cola del parametro c 

def buscar_el_maximo (c:Cola[int]) -> int:
    caux : Cola[int] = Cola ()
    max_value: int = c.get()
    caux.put(max_value)
    while not c.empty ():
        elem:int = c.get()
        caux.put (elem) 
        if elem >= max_value:
            max_value = elem
         
    while not caux.empty ():
       e:int = caux.get ()
       c.put (e)

    return max_value



def mostrar_elem_cola (c:Cola[int]) -> None:  
    caux : Cola [int] = Cola ()       # esta auxiliar viene bien para poder conservar la p, por si nos piden que p sea in (no puedo modoficarla)
    while not c.empty() :
        elem: int = c.get()
        print (elem)
        caux.put (elem)
    
    while not caux.empty():
        e: int = caux.get ()
        c.put(e)


# Siempre voy a necesitar crear una pila o cola para poder testear la funcion definida que tiene como input una Cola o una Pila  

cola: Cola[int] = Cola()
cola.put(5)
cola.put(10)
cola.put(-5)
cola.put(2)
cola.put(8)

print ("Elementos")

mostrar_elem_cola (cola)
print("Maximo:", buscar_el_maximo (cola))
mostrar_elem_cola (cola)



# Ejercicio 13

def armar_secuencia_bingo () -> Cola[int]:
    cola: Cola[int] = Cola()
    lista: list[int] = list(range(0,100))
    random.shuffle(lista)
    print ("el largo de la lista", len(lista))
    for i in range(len(lista)):
        cola.put (lista[i])
    print (lista)
    return cola

bolillero:Cola[int] = armar_secuencia_bingo ()
mostrar_elem_cola (bolillero)
    


# tener 2 variables en cuenta, una es lo que va sumando el bolillero como numero de salidas, la otra es "falta para ganar" que arranca con los 12 valores del carton y va restando 1 si es que el elemento del bolillero coincide con algun numero del carton
# tanto el input de carton como el del bolillero son in, es decir, se tienen que conservar despues de correr el código ...

def jugar_carton_de_bingo (carton : list[int], bolillero : Cola[int]) -> int:
    fpg: int = 12
    bolillero_aux: Cola[int] = Cola ()
    tiradas: int = 0
    while fpg > 0:
        elem:int = bolillero.get()
        bolillero_aux.put (elem) 
        tiradas = tiradas + 1
        for numero in carton:     
            if numero == elem:
                fpg = fpg - 1
    
    while not bolillero_aux.empty():
        e: int = bolillero_aux.get ()
        bolillero.put(e)

    return tiradas                

#defino un carton x, ver como definir un carton aleatoriamente, pero despues dejarlo fijo ...
carton:list[int] = [10,12,16,18,22,24,26,28,30,32,34,36]
print(carton)


print(jugar_carton_de_bingo(carton, bolillero))




# Ejercicio 16
# Nos pide abrir un archivo de texto, y de ahi obtener un diccionario que agrupe por cantidad de letras y cantidad de palabras ...

# Pruebo abrir un archivo ...

# archivo = open ("prueba_ej16.txt")

#for linea in archivo.readlines():
#    print(linea)
#    archivo.close()



def agrupar_por_longitud(nombre_archivo: str) -> dict [int,int]:
    # Inicializar un diccionario vacío para almacenar los conteos de palabras por longitud
    conteo_longitudes = {}

    # Abrir y leer el archivo
    archivo = open(nombre_archivo, "r")
        # Leer cada línea del archivo
    for linea in archivo:
            # Separar la línea en palabras, asumiendo que separamos por espacios en blanco
            palabras = linea.split()

            # Procesar cada palabra
            for palabra in palabras:
                # Calcular la longitud de la palabra
                longitud = len(palabra)

                # Actualizar el conteo en el diccionario
                if longitud in conteo_longitudes:
                    conteo_longitudes[longitud] += 1
                else:
                    conteo_longitudes[longitud] = 1
    archivo.close()
    return conteo_longitudes

nombre_archivo = "prueba_ej16.txt"
print(agrupar_por_longitud (nombre_archivo))


# Ejercicio 17
# Dado una lista de tuplas que contiene nombre del estudiante y notas en distintos examenes, que se arme un diccionario con el nombre del alumno y promedio de sus notas ...

# Armar funcion pertenece con strings (habiamos hecho una con numeros), me sirve para revisar si hay un elemento en las keys del diccionrio

def pertenece_string (s:list[str], e:str) -> bool:
    resultado: bool = False
    for i in s:
        if i == e:
            resultado = True
    return resultado


def calcular_promedio_por_estudiante (notas: list[tuple[str, float]]) -> dict [str, float] :
    suma_notas = {}
    cantidad_notas = {}
    promedio_por_alumno = {}
    for t in notas:
            e:str = t[0]
            if pertenece_string (suma_notas.keys(), e):
                suma_notas [e] = suma_notas [e] + t[1]
                cantidad_notas [e] = cantidad_notas [e] + 1
                promedio_por_alumno [e] = suma_notas [e] / cantidad_notas [e]
            else:
                suma_notas [e] = t[1]
                cantidad_notas [e] = 1 
                promedio_por_alumno [e] = suma_notas [e] / cantidad_notas [e]

    return promedio_por_alumno

notas:list[tuple[str,float]] = [("Juan", 4.0), ("Jose", 6.0), ("Juan",7.0), ("Jose", 8.0), ("Raul", 3.5)]
print (calcular_promedio_por_estudiante (notas))


# Ejercicio 18
# Dado un archivo, obtener la palabra mas frecuente ...

def palabra_mas_frecuente (nombre_archivo: str) -> str :
    archivo = open (nombre_archivo, "r")
    max_palabras:int = 0
    cantidad_palabras = {}
    for linea in archivo:
        palabras = separar_palabras (linea) # Generar funcion separar palabras ...
        for palabra in palabras:
            e:str = palabra
            if pertenece_string (cantidad_palabras.keys(), e):  # no esta permitido el in, aplicar el pertenece ...
                cantidad_palabras [e] = cantidad_palabras [e] + 1
                if cantidad_palabras [e] >= max_palabras:
                   max_palabras = cantidad_palabras [e]
                   e_max = e
            else:
                cantidad_palabras [e] = 1
    archivo.close()
    return e_max

nombre_archivo = "lista_palabras.txt"
print (palabra_mas_frecuente (nombre_archivo))



# Armar funcion auxiliar separar_palabras ...
def separar_palabras (l:str) -> list[str] :
    palabra:str = ""
    lista_nueva:list[str] = []
    for a in l:
        if a != " ":
            palabra = palabra + a  
        else:
            lista_nueva.append(palabra)
            palabra = ""
    lista_nueva.append(palabra)
    return lista_nueva

print(separar_palabras("Los señores de Parma"))


# Ejercicio 21
# Implementar una funcion que dado un archivo arroje cantidad de lineas del archivo ...


def contar_lineas (nombre_archivo:str) -> int:
    archivo = open (nombre_archivo,"r")
    cantidad_lineas:int = 0
    for linea in archivo:
        cantidad_lineas = cantidad_lineas + 1
    archivo.close()
    return cantidad_lineas

nombre_archivo = "archivo_prueba"
print(contar_lineas (nombre_archivo))


from typing import TextIO # Para tipado fuerte, defino el tipo de texto de los archivos, si no lo ponia corre igual ...


def contar_lineas_2 (nombre_archivo:str) -> int:
    archivo: TextIO = open (nombre_archivo,"r")
    cantidad_lineas:int = len(archivo.readlines())
    archivo.close()
    return cantidad_lineas

nombre_archivo: str = "archivo_prueba"
print(contar_lineas_2 (nombre_archivo))



# Ejercicio 19 
# Crear diccionario historiales 


# Ejercicio 19 
# Crear diccionario historiales 


def visitar_sitio (historiales: dict [str, Pila [str]], usuario: str, sitio:str):
    if usuario in historiales.keys():
       for t in historiales:
           if usuario == t:
               historiales[usuario].put(sitio)
    else:
       historiales[usuario] = Pila()
       historiales [usuario].put(sitio)
    print(historiales["Raul"])


historiales = dict [str, Pila [str]]
historiales = {"Martin":Pila(),"Raul": Pila(), "Jose": Pila()}
historiales ["Martin"].put("www.cap.com.ar")
historiales ["Raul"].put("www.org.com.ar")
historiales ["Jose"].put("www.afa.com.ar")

# Pruebo con un usuario que ya tengo:
visitar_sitio (historiales, "Raul", "www.loco.com.ar")
print (historiales["Raul"].get())


# Pruebo agregando un usuario nuevo:
visitar_sitio (historiales, "Ernesto", "www.favel.com.ar")
print (historiales["Ernesto"].get())


# Ejercicio 20
# Armar un sistema de inventario, es un diccionario cuya key es un producto y el valor es otro diccionario
# que contiene precio y cantidad del producto 
# 20.1


def agregar_producto (inventario: dict [str, dict[str, float | int]], nombre:str, precio:float, cantidad:int): 
    if nombre not in inventario:
        inventario[nombre] = dict[str, float | int]
        inventario[nombre] = {"precio":precio, "cantidad": cantidad}
       
       
inventario: dict [str, dict[str, float | int]] = {"Camisas": {"precio": 3.0, "cantidad": 5}, "Zapatos":{"precio": 5.0, "cantidad": 10}}
agregar_producto(inventario, "Remeras", 4.0, 3)
print (inventario)


# 20.2
# Armar una funcion que permita actualizar stock:
def actualizar_stock (inventario: dict [str, dict[str, float | int]], nombre:str, cantidad:int):
    if nombre in inventario:
        inventario [nombre]["cantidad"] = cantidad


actualizar_stock (inventario, "Camisas", 10)
print (inventario) 

#20.3
# Armar una funcion que permita actualizar precios:
def actualizar_precio (inventario: dict [str, dict[str, float | int]], nombre:str, precio:float):
    if nombre in inventario:
        inventario [nombre]["precio"] = precio


actualizar_precio (inventario, "Camisas", 6.0)
print (inventario) 


# 20.4
# Armar funcion que devuelva el valor de todo el inventario, es decir sume la multiplicacion de todos los precios x cantidad
def calcular_valor_inventario (inventario: dict [str, dict[str, float | int]]) -> float:
    suma: float = 0.0
    for nombre, datos in inventario.items():
        if "precio" in datos and "cantidad" in datos:
            datos ["valor_inventario"] = datos ["precio"] *datos ["cantidad"]
            suma = suma + datos ["valor_inventario"]
    
    return suma


inventario: dict [str, dict[str, float | int]] = {"Camisas": {"precio": 3.0, "cantidad": 5}, "Zapatos":{"precio": 5.0, "cantidad": 10}}
print(calcular_valor_inventario(inventario))
print (inventario)

# Ejercicio 22


# Ejercicio 23


# Algunos de la Guia 7, Matrices: 5.1, 6.1, 6.2, 6.5


# Casos de Test de caja blanca, cobertura en Python 

#import unittest
#from Funciones import funcion
    

#class FuncionesTest(unittest.TestCase)
#    def test_1 (self):
#        self.assertEqual (funcion(28),4 , "primer test")
    


 

