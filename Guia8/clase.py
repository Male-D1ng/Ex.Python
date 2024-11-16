# Code by Agustín Sansone

from typing import List, TextIO

####################### Ej 21.1 #######################

def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo, 'r')
    lineas: int = len(archivo.readlines())
    archivo.close()
    return lineas

def contar_lineas_alternativo(nombre_archivo: str) -> int:
    lineas: int = 0
    archivo: TextIO = open(nombre_archivo, 'r')
    for linea in archivo:
        lineas += 1
    archivo.close()
    return lineas

####################### Ej 22 #######################

def es_comentario(linea: str) -> bool:
    for c in linea:
        if c == '#':
            return True
        if c != ' ':
            return False
    return False

def clonar_sin_comentarios(nombre_archivo : str) -> None:
    archivo: TextIO = open(nombre_archivo, 'r')
    lineas_originales: List[str] = archivo.readlines()
    archivo.close()
    archivo_nuevo: TextIO = open(nombre_archivo + '_sin_comentarios', 'w')
    for linea in lineas_originales:
        if not es_comentario(linea):
            archivo_nuevo.write(linea)
    archivo_nuevo.close()
    
####################### Ej 16 #######################

def obtener_palabras(texto: str) -> List[str]: # supongamos que las palabras están sólo separadas por espacios (o saltos de línea)
    palabras: List[str] = []
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

def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
    archivo: TextIO = open(nombre_archivo, 'r')
    palabras: List[str] = obtener_palabras(archivo.read())
    archivo.close()
    agrupadas: dict[int,int] = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud not in agrupadas:
            agrupadas[longitud] = 1
        else:
            agrupadas[longitud] += 1
    return agrupadas

####################### Ej 18 #######################

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo: TextIO = open(nombre_archivo, 'r')
    palabras: List[str] = obtener_palabras(archivo.read())
    archivo.close()
    palabra_cantidad: dict[str,int] = {}
    # Arammos un diccionario de 'palabra' -> 'cantidad de apariciones'
    for palabra in palabras:
        if palabra not in palabra_cantidad:
            palabra_cantidad[palabra] = 1
        else:
            palabra_cantidad[palabra] += 1
    # Nos quedamos con la palabra con más apariciones
    max_frecuencia: int = 0
    palabra_max_frecuencia: str = ''
    for palabra in palabra_cantidad:
        if palabra_cantidad[palabra] > max_frecuencia:
            max_frecuencia = palabra_cantidad[palabra]
            palabra_max_frecuencia = palabra
    return palabra_max_frecuencia
