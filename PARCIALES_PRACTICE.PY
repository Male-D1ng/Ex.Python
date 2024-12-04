"""

3) Camas ocupadas en el hospital (2 puntos)
Queremos saber qué porcentaje de ocupación de camas hay en el hospital.
El hospital se representa por una matriz en donde las filas son los pisos, y las columnas son las camas.
Los valores de la matriz son booleanos que indican si la cama está ocupada o no.
Si el valor es verdadero (True) indica que la cama está ocupada.
 Se nos pide programar en Python una función que devuelve una secuencia de reales, indicando la proporción de camas ocupadas en cada piso.
problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: {Todos los pisos tienen la misma cantidad de camas.}
  requiere: {Hay por lo menos 1 piso en el hospital.}
  requiere: {Hay por lo menos una cama por piso.}
  asegura: {|res| = |camas_por_piso|}
  asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}
}

R es un float
"""

def ocupacion_camas(ocupadas:list[list[bool]])->list[int]:
    res:list[int]=[]
    for pisos in ocupadas: #entro por piso, len(ocupadas) me dice cuantos pisos hay 
        cantidad:int=0
        for camas in pisos: #len(pisos) = cantidad de camas
            if camas:
                cantidad +=1
        proporcion = cantidad/len(ocupadas[0])
        res.append(proporcion)
    return res

print("ocupacion 1=",ocupacion_camas([[True,True,False,False],[False,True,False,False],[True,True,False,True]]))

def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
  res : list[float] = []
  contador : int = 0
  cantidad_camas = len(camas_por_piso) #los pisos
  for fila in range(0,cantidad_camas) : #veo filas o pisos
    for elem in range(0,len(camas_por_piso[0])): #entro a los pisos y veo las camas o columnas 
      if camas_por_piso[fila][elem] == True:
        contador += 1
    res.append(contador/len(camas_por_piso[0]))
    contador = 0
  return res  

print("ocupacion 2 =",nivel_de_ocupacion([[True,True,False,False],[False,True,False,False],[True,True,False,True]]))

"""1) Alerta Enfermedades Infecciosas (3 puntos)

Necesitamos detectar la aparición de posibles epidemias. 
Para esto contamos con un lista de enfermedades infecciosas y los registros de atención por guardia dados por una lista expedientes. 
Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención.
Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporción de pacientes que se atendieron por esa enfermedad. 
En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.
problema alarma_epidemiologica (registros: seq⟨ZxString⟩, infecciosas: seq⟨String⟩, umbral: R) : dict⟨String,R⟩ {
  requiere: {0 < umbral < 1}
  asegura: {claves de res pertenecen a infecciosas}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, 
                entonces res[enfermedad] = porcentaje}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, 
                entonces enfermedad no aparece en res}
}
"""

def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    cantidad_registros: int = len(registros)
    registros_por_enfermedad: dict[str, int] = {}
    res: dict[str, float] = {}
    contar_registros_infecciosos_por_enfermedad(registros, infecciosas, registros_por_enfermedad)

    for enfermedad in registros_por_enfermedad.keys():
        porcentaje = calcular_porcentaje_de_registros(cantidad_registros, registros_por_enfermedad, enfermedad)
        agregar_enfermedad_si_supera_umbral(umbral, res, enfermedad, porcentaje)

    return res

def calcular_porcentaje_de_registros(cantidad_registros:int, registros_por_enfermedad: dict[str, int], enfermedad:str):
    porcentaje: float = registros_por_enfermedad[enfermedad] / cantidad_registros
    return porcentaje

def agregar_enfermedad_si_supera_umbral(umbral:float, res: dict[str, float], enfermedad:str, porcentaje:float):
    if porcentaje >= umbral:
        res[enfermedad] = porcentaje

def contar_registros_infecciosos_por_enfermedad(registros:list[tuple[int, str]], infecciosas: list[str], registros_por_enfermedad:dict[str, int]):
    for enfermedad in registros:
        if pertenece(infecciosas,enfermedad[1]):
            if not pertenece(registros_por_enfermedad.keys(),enfermedad[1]):
                registros_por_enfermedad[enfermedad[1]] = 0
            registros_por_enfermedad[enfermedad[1]] += 1
            
def pertenece (infecciosas:list[str],enfermedad:str)->bool:
    for e in infecciosas:
        if enfermedad == e:
            return True



registros = [(1, "gripe"), (2, "covid"), (3, "gripe"), (4, "gripe"), (5, "covid")]
infecciosas = ["gripe","covid","ebola"]
umbral = 0.5
print(alarma_epidemiologica(registros,infecciosas,umbral))            
            






"""4) Quiénes trabajaron más? (2 puntos)
Dado un diccionario con la cantidad de horas trabajadas por empleado, 
en donde la clave es el ID del empleado y el valor es una lista de las horas trabajadas por día, 
queremos saber quienes trabajaron más para darles un premio. 
Se deberá buscar la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.
problema empleados_del_mes(horas:dicc⟨Z,seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: {No hay valores en horas que sean listas vacías}
  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
  asegura: {Para todo ID de claves de horas, 
  si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
}
"""

def pertenece (elem:int,lista:list[int])->bool:
    for e in range(len(lista)):
        if elem == lista[e]:
            return True


def maximo(d:dict[int,int])->list[int]:
    res:int = []
    num=0
    for id,lista in d.items():
        if num <= lista:
            res.append(id)
            num = lista 
    return res

def suma(lista:list[int])->int:
    res=0
    for e in range(len(lista)):
        res += lista[e]
    return res 

def empleados_del_mes(horas:dict[int,list[int]])->list[int]:
    dict={}
    for e in horas.keys():
        max = suma(horas[e])
        dict[e] = max
    return maximo(dict) 
    
d = {1:[2,3,54],2:[2,3,54]}
e = {1:59,2:59}
horas = {1: [5, 6, 7], 2: [8, 9, 10], 3: [2, 3, 4]}

print(maximo(e))

print(empleados_del_mes(horas))


"""
2) En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable (esto se llama hacer triage).
 A partir de dichas colas que contienen la identificación del paciente, se pide devolver una nueva cola según la siguiente especificación.
problema orden_de_atencion ( in urgentes: cola⟨Z⟩, in postergables: cola⟨Z⟩) : cola⟨Z⟩ {
  requiere: {no hay elementos repetidos en urgentes}
  requiere: {no hay elementos repetidos en postergables}
  requiere: {la intersección entre postergables y urgentes es vacía}
  requiere: {|postergables| = |urgentes|}
  asegura: {no hay repetidos en res }
  asegura: {res es permutación de la concatenación de urgentes y postergables}
  asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
  asegura: {En res no hay dos seguidos de urgentes}
  asegura: {En res no hay dos seguidos de postergables}
  asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
  asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables 
  entonces c1 aparece antes que c2 en res}
"""

from queue import Queue as Cola

def orden_de_atencion (urgentes: Cola[int], postergables: Cola[int])-> Cola[int]:
    uaux:Cola[int]= Cola()
    paux:Cola[int]=Cola()
    res:Cola[int]=Cola()
    while not urgentes.empty() and not postergables.empty():
        c1=urgentes.get()
        uaux.put(c1)
        res.put(c1)
        c2=postergables.get()
        paux.put(c2)
        res.put(c2)

    while not uaux.empty():
        urgentes.put(uaux.get())

    while not paux.empty():
        postergables.put(paux.get())

    return res 
        

def impresora (c: Cola[int])-> Cola[int]:
    uaux:Cola[int]=Cola()
    while not c.empty():
        c1=c.get()
        uaux.put(c1)
        print(c1)

    while not uaux.empty():
        c.put(uaux.get())
    

u=Cola()
u.put(1)
u.put(-3)
p=Cola()
p.put(2)
p.put(-4)


impresora(orden_de_atencion(u,p))









#recu 1c 2024

"""
1) Gestión de notas de estudiantes [2 puntos]
En una escuela llamada "Academia Futura", se desea desarrollar un programa para gestionar las notas de los estudiantes por materia.
 El programa debe procesar una lista de tuplas donde 
 cada tupla contiene el nombre de un estudiante, el nombre de una materia y la nota final obtenida por el estudiante en esa materia.

Se pide implementar una función en python, que respete la siguiente especificación:

problema gestion_notas (in notas_estudiante_materia: seq⟨(String x String x Z)) : dict⟨String, seq⟨(String x Z)⟩⟩ {
  requiere: { Las primeras componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las segundas componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las terceras componentes de notas_estudiante_materia están entre 1 y 10, ambos inclusive }
  requiere: { No hay 2 tuplas en notas_estudiante_materia que tengan la primera y segunda componente iguales (mismo estudiante y misma materia) }
  asegura: {res tiene como claves solo los primeros elementos de las tuplas de notas_estudiante_materia (o sea, un estudiante)}
  asegura: {El valor en res de un estudiante es una lista de tuplas donde cada tupla contiene como primera componente el nombre de la materia 
  y como segunda componente la nota obtenida por el estudiante en esa materia según notas_estudiante_materia}
  asegura: { Para toda clave (estudiante) en res, en su valor (lista de tuplas) no hay 2 tuplas que tengan la misma primera componente (materia) }
}

2) Cantidad dígitos pares [2 puntos]
Se pide implementar una función en Python llamada cantidad_digitos_pares que respete la siguiente especificación:

problema cantidad_digitos_pares (in numeros: seq⟨Z⟩) : Z {
  requiere:{Todos los elementos de numeros son mayores iguales a 0}
  asegura: {res es la cantidad total de digitos pares que aparecen en cada uno de los elementos de numeros}
}
Por ejemplo, si la lista de números es [5434, 42, 811, 3139], entonces el resultado esperado sería 5 (los dígitos pares son 4, 4, 4, 2, y 8).

3) Priorizar cola de paquetes [2 puntos]
En una empresa de logística, se manejan paquetes que llegan a una bodega y deben ser procesados para su posterior distribución. Cada paquete está 
representado por una tupla (id_paquete, peso), donde id_paquete es un identificador único del paquete y peso representa el peso del paquete en kilogramos.

Se pide implementar una función en Python llamada reordenar_cola_primero_pesados que respete la siguiente especificación:

problema reordenar_cola_primero_pesados(in paquetes: Cola⟨(String x Z)⟩, in umbral:Z): Cola⟨(String x Z)⟩{
  requiere: {no hay repetidos en las primeras componentes (Ids) de paquetes}
  requiere: {todos las segundas componentes (pesos) de paquetes son mayores estricto a cero}
  requiere: {umbral es mayor o igual a cero}
  asegura: {los elementos de res son exactamente los mismos que los elementos de paquetes}
  asegura: {|res| = |paquetes|}
  asegura: {no hay un elemento en res, cuyo peso sea menor o igual que el umbral, que aparezca primero que otro elemento en res cuyo peso sea mayor que 
            el umbral)}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son menores o iguales que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en 
            paquetes entonces p1 aparece primero que p2 en res}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son mayores que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en paquetes entonces 
            p1 aparece primero que p2 en res}
}

4) Matriz pseudo ordenada [2 puntos]
Se desea verificar si una matriz está pseudo ordenada por columnas. Esto es que el mínimo de cada columna sea menor estricto que el mínimo de la columna siguiente

Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:

matriz_pseudo_ordenada (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {todos los elementos de matriz tienen la misma longitud}
  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el mínimo de la columna i de matriz < el mínimo de la columna i + 1 de matriz }
}

5) Preguntas teóricas (2 puntos)
Conteste marcando la opción correcta.

A) ¿Cuál es el principal objetivo del testing de caja blanca? (0.75 punto)
 ○ Evaluar la funcionalidad del software desde la perspectiva del usuario final.
 ○ Verificar la lógica interna del código, estructuras de control, condiciones y flujo de datos.
 ○ Garantizar que la interfaz de usuario sea intuitiva y fácil de usar.
B) ¿Qué es un "alcance" (scope) en Python? (0.5 punto)
 ○ El contexto en el cual una variable es accesible.
 ○ El número de variables definidas en un programa.
 ○ El número de funciones definidas en un programa.
C) ¿Cuál es la principal diferencia entre una lista y una tupla en Python? (0.75 punto)
 ● Las listas permiten agregar y eliminar elementos después de su creación, mientras que las tuplas no.
 ○ Las listas se ordenan automáticamente, mientras que las tuplas mantienen el orden de inserción.
 ○ Las listas pueden contener elementos duplicados y las tuplas no.


"""

#1
def gestion_notas(notas_estudiante_materia: list[tuple[str,str,int]]) -> dict[str, list[tuple[str,int]]]:
    res:dict[str, list[tuple[str,int]]] = {}
    for n, p, c in notas_estudiante_materia:
        if not pertenece_dicc (n,res):
            res[n] = [(p, c)]
        else:
            res[n].append((p, c))
    
    return res

def pertenece_dicc(n:str,d:dict[str, list[tuple[str,int]]]):
    for claves in d.keys():
        if n == claves:
            return True


d = [("Juan","mate",5),("Juan","lengua",8),("Sara","lengua",8)]

print(gestion_notas(d))


#2
""") Cantidad dígitos pares [2 puntos]
  asegura: {res es la cantidad total de digitos pares que aparecen en cada uno de los elementos de numeros}
}
Por ejemplo, si la lista de números es [5434, 42, 811, 3139], entonces el resultado esperado sería 5 (los dígitos pares son 4, 4, 4, 2, y 8)."""

def cantidad_dig_pares (numeros:list[int])->int:
    res:int = 0
    for n in numeros:
        while (n > 0):
            d:int = n%10
            if d%2 == 0:
                res += 1
            n = n//10
    return res


print("la cantidad es :",cantidad_dig_pares([4,42]))

#4
"""4) Matriz pseudo ordenada [2 puntos]
Se desea verificar si una matriz está pseudo ordenada por columnas. Esto es que el mínimo de cada columna sea menor estricto que el mínimo de la columna siguiente

Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:

matriz_pseudo_ordenada (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {todos los elementos de matriz tienen la misma longitud}
  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el mínimo de la columna i de matriz < el mínimo de la columna i + 1 de matriz }
}"""

def minimo (columna :list[int])->int:
    minimo = columna[0]
    for n in range(1,len(columna)):
        if columna[n]< minimo:
            minimo = columna[n]
    return minimo

print("el min es :",minimo([45, 55, 11]))

def obtener_columna_n (matriz:list[list[int]],n:int):
    res=[]
    for i in range(len(matriz)):
        res.append(matriz[i][n])
    return res 

print("columnas :",obtener_columna_n([[5434,33,23],[747,42,87],[811,90,3139]],1))

def columnas(matriz:list[list[int]])->list[list[int]]:
    res=[]
    columnas = len(matriz[0])
    for n in range(columnas):
        columna = obtener_columna_n(matriz, n)
        res.append(columna)
    return res 

print("columnas :",columnas([[52,81,45],[60,42,55],[74,90,11]]))


def matriz_pseudo_ordenada(matriz:list[list[int]])->bool:
    res:bool=True
    colum: list[list[int]] = columnas(matriz)
    minimo_col_i: int = minimo(colum[0])
    col_actual: int = 1
    while (col_actual < len(colum)):
        minimo_col_i_mas_1: int = minimo(colum[col_actual])
        res = (minimo_col_i < minimo_col_i_mas_1)
        col_actual += 1
        minimo_col_i = minimo_col_i_mas_1
    return res 
    
print("columnas :",matriz_pseudo_ordenada([[11,81,45],[60,42,55],[74,90,52]]))
#[[1,4,7],[2,5,8],[3,6,9]] si da True

























#################################################PARCIAL 1C2024 COMISION D###################################################

def pertenece_d(n:str,d:dict[str, list[tuple[int,int]]]):
    for claves in d.keys():
        if n == claves:
            return True

def stock_productos_version_2(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int,int]]:
    res: dict[str, tuple[int, int]] = dict()

    for (producto, cantidad) in stock_cambios:
        if not pertenece_d(producto,res):
            res[producto] = (cantidad, cantidad)
        elif res[producto][0] > cantidad:                   #si hay nuevo mínimo
            res[producto] = (cantidad, res[producto][1])    #actualizo el mínimo y conservo el máximo
        elif res[producto][1] < cantidad:                   #si hay nuevo máximo
            res[producto] = (res[producto][0], cantidad)    #actualizo el máximo y conservo el mínimo

    return res


##################################################################################################################

def ordenados (s:list[int])->bool:
     for i in range (0,len(s)-1,1):
        if s[i]>s[i+1]:
               return False
     return True 
print(ordenados([1,2,3,4,5,4]))


##############################################PARCIAL 1C2024 COMISION C#########################################################################

def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
  res: dict[str, tuple[int, float]] = {}
  for clave in registro.values():
    salas_escapadas:list[int] = salas_con_salidas(registro[clave])
    cantidad_salidas:int = len(salas_escapadas)
    promedio:float = promedio_salas(salas_escapadas)
    res[clave] = (cantidad_salidas, promedio)
  return res
 
def salas_con_salidas(tiempos_salidas:list[int]) -> list[int]:
  res:list[int] = []
  for elem in tiempos_salidas:
    if (elem > 0 and elem < 61):
      res.append(elem)
  return res
  
def promedio_salas(tiempos_salidas:list[int]) -> float:
  suma:int = 0
  res: float = 0.0
  for elem in tiempos_salidas:
    suma += elem
  if (suma > 0):
    res = (suma / len(tiempos_salidas))
  return res


#####################################################PARCIAL 1C2024 COMISION B##########################################################################

"""3) Sufijos que son palíndromos (2 puntos)
Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.

problema cuantos_sufijos_son_palindromos(in texto:String) : Z {
  requiere: -
  asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto}
}
Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el al final de la palabra. 
Ej: "Diego", el conjunto de sufijos es: "Diego", "iego","ego","go", "o". Para este ejercicio no consideraremos a "" como sufijo de ningun texto."""

def es_palindromo(p:str) -> bool:
    res:bool = True
    inversa:str=""
    for n in range(len(p)-1,-1,-1):
        inversa += (p[n])
    if p != inversa:
        res = False
    return res 

print("palindromo ? =",es_palindromo("ododo"))

def cuantos_sufijos_son_palindromos (texto:str)->int:
    res:int=0
    indice = len(texto)-1
    i = 0
    inversa :str = ""
    for n in range(len(texto)-1,-1,-1):
        inversa += (texto[n])

    n:str=inversa[i]
    while i < indice:
        if es_palindromo(n):
                res += 1
        i+=1
        n+=inversa[i]
    if i == indice:
        if es_palindromo(n):
            res+=1
        """if texto[0] != texto[(len(texto)-1)]:
            res -=1"""
    return res

print(" cuantos palindromo ? =",cuantos_sufijos_son_palindromos("alas"))

#if texto[0] == texto[len(texto)-1]:

########################PARCIAL DE 2C2024 NOCHE #########################
"""1)dada una lista v de int devolver un diccionario tal q sus claves son nros primos y sus valores
son la cantidad de nros en v q divide ese nro primo
"""

def pertenece (lista:list[int],n:int)->bool:
    res:bool=True
    for n in range(len(lista)):
        if lista[n] != n:
            res = False
    return res


def buscar_divisores (nro:int)->list[int]:
    res= []
    divisor = nro
    while nro >= divisor and divisor != 0:
        if nro % divisor == 0:
            res.append(divisor)
        divisor -=1
    return res 

print("los divisores son",buscar_divisores(30))

def divisores_primos (lista:list[int])-> list[int]:
    res=[]
    for n in lista:
        if len(buscar_divisores(n)) == 2:
            res.append(n)
    return res 

print("los divisores son",divisores_primos(buscar_divisores(14)))

"""
def divisores_en_v (una_de_lista_divisores:list[int],v:list[int])->bool:
    res:bool
    for numeros in v:
        divisores_primos:list[int] = divisores_primos(buscar_divisores(numeros))
    for divisores in divisores_primos:
        if pertenece (divisores,una_de_lista_divisores):
            res=True
    return res """

def multiplos_de_primos(v:list[int])->dict[int,int]:
    res:dict[int,int]={}
    for n in v:
        sus_divisores:list[int] = buscar_divisores(n)
        divisores:list[int] = divisores_primos(sus_divisores)
        for d in divisores:
            if d in res.keys():
                res[d] +=1
            else:
                res[d] = 1

    return res 


print("q funcione porfa ",multiplos_de_primos([30,14]))


##2)

def mas_1 (v:list[list[int]])->int:
    longitud_actual = 0
    for n in v:
        es_1 = 0
        longitud = len(n)
        no_1 = 0
        for j in range(longitud):
            if n[j] == 1:
                es_1 +=1
            else:
                no_1 +=1
        if es_1 > longitud_actual:
            longitud_actual = len(n)-no_1

    return longitud_actual

print("mas1 ",mas_1([[1],[1,1,1,1,1,11],[1,1,1,1,1,1,1,1,7,77,7,7,7,7,7,7,7,77],[1,1,1,11,12,12,13]]))


from queue import LifoQueue as Pila

#3) 

"""
def esta_bien_formada (s:str)->bool:
    res:bool=True
    suma = '+'
    resta = '-'

    if (s[0] == suma or s[0]== resta):
        res = False
    elif (s[len(s)-1] == suma or s[len(s)-1] == resta):
        res = False
    else:
        res

    for i in range(0,len(s)-1):
        if (s[i] == suma and s[i+1] == suma) or (s[i] == resta and s[i+1] == resta) or (s[i] == suma and s[i+1] == resta) or (s[i] == resta and s[i+1] == suma):
            res = False
        else:
            res

    return res 

print("cuenta bien ",esta_bien_formada("2+2-3"))


def resolver_cuentas (p:Pila[str])-> list[int]:
    paux:Pila[str] = Pila()
    res=[]
    while not p.empty():
        elem = p.get()
        paux.put(elem)
        if esta_bien_formada(elem):
            res.append(elem) 
    while not paux.empty():
        p.put(paux.get())

    return res

p = Pila()
p.put("2+2+2")
rta = resolver_cuentas(p)
print("da? =",rta)"""



# Ejercicio 3
def resolver_cuentas(p: Pila [str]) -> list[str]:
    p_copia: Pila[str] = Pila()
    res: list[str] = []

    while not p.empty():
        cuenta:str = p.get()
        p_copia.put(cuenta)
        res.append(calcular(cuenta)) 

    #restauro pila
    while not p_copia.empty():
        p.put(p_copia.get())
    return res

def calcular(cuenta: str):
    res = 0
    numero_actual = 0
    signo = 1  # 1 para suma, -1 para resta

    for caracter in cuenta:
        if caracter == "+" or caracter == "-":
            # agrego el número actual al resultado acumulado
            res += signo * numero_actual
            numero_actual = 0
            if caracter == "+":
                signo = 1
            else:
                signo = -1
        else:
            numero_actual = numero_actual * 10 + int(caracter)

    # agrego el último número al resultado
    res += signo * numero_actual
    return res


p = Pila()
p.put("2+2+2")
rta = resolver_cuentas(p)
print("da? =",rta)



from queue import LifoQueue as Pila
import math
#4)dame el que falta, 
"""el menor nro de alguna tupla es 1, n el maximo nro en elaguna tupla 
tal q longitud (s) = n*n-1, no hay repetida, y quiero una tupla q son los 2 nros q faltan en todas las tuplas, 
res no pertenece a la lista de tuplas"""

# Ejercicio 4
def dame_el_que_falta(s: list[tuple[int, int]]) -> tuple[int, int]:
    max: int = int(math.sqrt(len(s) + 1))
    for i in range(1, max + 1):
        for j in range(1, max + 1):
            if not pertenece(s, (i, j)):
                return (i, j)