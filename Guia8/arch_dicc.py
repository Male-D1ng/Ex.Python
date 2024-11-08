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


