#ej_importantes.py

from queue import Queue as Cola
import random

#ej14
def cantidadElementos(c: Cola) -> int:
    res: int = 0
    cola = Cola ()
    caux: cola = Cola()

    while not c.empty():
        elem = c.get()
        caux.put(elem)
        res = res + 1
    
    while not caux.empty():
        elem = caux.get()
        c.put(elem)
        
    return res

mi_cola = Cola ()
mi_cola.put(1)
mi_cola.put(2)

print(cantidadElementos(mi_cola))



#EJ7_PARTE_A
import csv
#el archivo csv se ve como : nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
def contarlineas(lu : str) -> int:
    #primero abro el archivo
    archivo=open(lu,'r')
    #lo leo
    leo_archivo=archivo.readlines()
    archivo.close()
    return len(leo_archivo)
print("la cantidad de lineas es :", contarlineas("archivo_de_prueba.txt"))

def prueba_archivos (arc:str) -> str:
    archivo = open (arc,'r')
    # Leer el contenido del archivo
    contenido = archivo.read()
    lista:list = contenido.split('\n') #devuelve una lista de listas de lo q habia en notas.csv
    print("la prueba se ve como un monton de listas con lo que habia en el archivo: ")
    for lu in lista:
        primer_valor = lu.split(',')
        print(primer_valor) #devuelve listas  de lo q habia en el archivo
    #Cerrar el archivo
    archivo.close()
prueba_archivos('notas.csv')

import csv

def promedio_Estudiante(lu: str) -> float:
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
# Prueba de la función
lu_alumno = input("nro de libreta: ")
promedio = promedio_Estudiante(lu_alumno)
print ("El promedio del estudiante con LU ",lu_alumno, "es ", promedio)



def apariciones(notas:list[str], alumno:str) -> int:
    apariciones:int = 0
    for nota in notas:
        campos = nota.split(',')
        if campos [0] == alumno:
            apariciones += 1
    return apariciones

def promedioEstudiantes() -> float:
    archivo = open("notas.csv","r",newline="", encoding="utf-8-sig") #EL ENCODING VARIA EL RTADO, QUITA ALGUNOS 
    contenido:str = archivo.read()
    notas:list[str] = contenido.split('\n') # en cada pos de la lista tenemos una "nota" con sus respectivos atributos
    diccionario:dict = {} #la estructura es {key,value}
  
    for nota in notas:
        campos = nota.split(',') #quiero poder acceder a cada campo q compone una nota
        if campos[0] in diccionario: #campos va a ser mi value
            diccionario[campos[0]] += float(campos[3]) #voy acumulando las notas
        else:
            diccionario[campos[0]] = float(campos[3]) #siempre q llamamos al campo donde esten las notas le hardcodeamos el tipo float ya que por defecto en los csv viene como str
    
    for alumno in diccionario.keys(): #recorro cada alumno y calculo su promedio
        if apariciones(notas,alumno) != 0:
            diccionario[alumno] = float(diccionario[alumno]) / apariciones(notas,alumno) #el divisor del promedio es la cant. de apariciones en las notas
        else:
            diccionario[alumno] = -1
    
    return diccionario

print("USANDO LA FUNCION DE UN COMPA: ",promedioEstudiantes())

import csv

def promedio_estudiantesGIT() -> dict:
    # Inicializamos un diccionario para almacenar los promedios
    promedios = {}

    # Abrir el archivo CSV
    with open('notas.csv', newline='') as archivo_csv:
        lector = csv.reader(archivo_csv)

        # Iterar a través de las filas del archivo CSV
        for fila in lector:
            # Verificar si la fila tiene la estructura esperada
            if len(fila) == 4:
                legajo, materia, fecha, nota = fila
                # Convertir la nota a un número flotante
                nota = float(nota)
                # Agregar la nota al promedio del estudiante
                if legajo in promedios:
                    promedios[legajo].append(nota)
                else:
                    promedios[legajo] = [nota]

    # Calcular los promedios finales
    for legajo, notas in promedios.items():
        promedios[legajo] = sum(notas) / len(notas)

    return promedios

# Ejemplo de uso
print("LOS RESULTADOS USANDO GIT SON: ",promedio_estudiantesGIT())


