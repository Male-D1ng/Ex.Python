#guia6, ej4 usar max() y min ()
#peso = 3 kg por cada centímetro hasta 3 metros,2 kg por cada centímetro arriba de los 3 metros
#muebles, a la que le sirven árboles de entre 400 y 1000 kilo
#1. Definir la función peso_pino
#2. Definir la función es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica.
#3. Definir la función sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.
#4. Definir sirve_pino usando composición de funciones.

def peso_pino (altura_cm:int)-> int:
    peso: int = 0
    residual : int = 0
    if altura_cm <= 300:
        peso = altura_cm*3
    else:
        residual = altura_cm - 300
        peso = residual*2 + 900
    return peso 
#print(peso_pino(500))

def es_peso_util (peso:int) -> bool:
    if (peso>= 400 and peso<= 1000):
        return True
    else:
        return False

def sirve_pino_if_else (altura_cm : int) -> bool: # recibe la altura de un pino y si un pino de ese peso le sirve a la fábrica
    pesos = peso_pino (altura_cm)
    if es_peso_util(pesos) == True:
        return True
    else:
        return False 
    
def sirve_pino (altura_cm : int) -> bool :
    peso = peso_pino (altura_cm)
    pesos = [400,1000,peso]
    if (min(pesos) >= 400 and max (pesos) <= 1000):
        return True
    else:
        return False

#5
#5.1  que devuelve el doble del número en caso de ser par y el mismo número en caso contrario.
def devolver_el_doble_si_es_par(numero: int) -> int:
    if (numero%2 == 0):
        return numero *2 
    else:
        return numero
#5.2 que devuelve el mismo número si es par y sino el siguiente.
def es_par(numero:int) -> int:
    return numero % 2 == 0

def devolver_valor_si_es_par_sino_el_que_sigue(numero : int) -> int:
    resultado:int = 0
    if es_par(numero):
        resultado = numero
    else:
        resultado = numero +1
    return resultado

#5.3 
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero : int) -> int:
    resultado:int = 0
    if (numero%3!= 0 and numero%9 == 0):
        resultado = numero*3
    elif (numero%9 != 0 and numero%3 == 0):
        resultado = numero*2
    else:
        resultado = numero
    return resultado
    

#5.4 si la longitud es igual o mayor a 5 devolver una frase
def lindo_nombre(nombre):
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"

#5.5 a Menor a 5 si el número es menor a 5, Entre 10 y 20 si el número está
#en ese rango y Mayor a 20 si el número es mayor a 20
def elRango(numero):
    if numero <= 5:
        return "Menor a 5"
    elif 10 <= numero <= 20:
        return "Entre 10 y 20"
    else:
        return "Mayor a 20"
    
#5.6 Implemente una función que, dados los parámetros de sexo (F o M) y edad, diga cosas
def vacaciones (sexo:str,edad:int)-> str:
    vacaciones: str
    if sexo == 'F' and  edad >= 60 or edad <= 18:
        vacaciones = 'Andá de vacaciones'
    elif sexo == 'M' and edad >= 65 or edad <= 18:
        vacaciones = 'Andá de vacaciones'
    else:
        vacaciones = 'Te toca trabajar'
    return vacaciones

#Ejercicio 6.1

def numeros_1_a_10():
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1
    return

#Eejercicio 6.2

def pares_entre_numeros() -> int:
    numero = 10
    while numero <= 40:
        if numero % 2 == 0:
            print(numero)
        numero += 1
    return

#Ejercicio 6.3

def eco_10_veces():
    numero = 1
    while numero <= 10:
        print("ECO")
        numero += 1
    return

#Ejercicio 6.4

def cohete(numero:int):
    i = 0
    for i in range(i,numero,1):
    
        print(numero)
        numero -= 1
        if numero == 0:
            print("Despegue!!")

#Ejercicio 6.5

def viaje_en_el_tiempo_hacia_atras(anio_partida:int, anio_llegada:int) -> str:
    if anio_partida <= anio_llegada:
        print("El año de partida debe ser mayor que el año de llegada.")
        return
    
    while anio_llegada != anio_partida:
        print(f"“Viajo un anio al pasado, estamos en el anio: {anio_partida - 1}")
        anio_partida -= 1
    return

"""
#Ejercicio 6.6

def viaje_aristoteles(anio_partida:int, anio_llegada:int) -> str:
    if anio_partida <= anio_llegada:
        print("El año de partida debe ser mayor que el año de llegada.")
        return
    
    while anio_partida >= -384:
        print(f"“Viajo un anio al pasado, estamos en el anio: {anio_partida - 20}")
        anio_partida -= 20

    return 
"""

#Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso contrario
vocales = ['a','e','e','o','u','A','E','I','O','U']
def esVocal(letra:str) -> bool:
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    if pertenece(vocales, letra):
        return True
    return False

def vocales(palabra:str) -> bool:
    vocales: int = 0
    
    for letra in palabra: 
        if esVocal(letra):
            vocales+=1
    
    if vocales >= 3:
        return True
    return False

#GUIA 7, EJERCICIO 3

#PARTE 3
#ej1: quiero conocer el estado de aprobacion
def promedio(notas:list[int])->float:
    sumaNotas:int=0
    for nota in notas:
        sumaNotas+=nota
    promedio:float=sumaNotas/len(notas)
    return promedio

def todasLasNotasSonMayoresQue4(notas:list[int])->bool:
    for nota in notas:
        if nota<4:
            return False
    return True
        
def aprobado(notas:list[int])->int:
    if (todasLasNotasSonMayoresQue4(notas) and promedio(notas)>=7):
        return 1
    elif (todasLasNotasSonMayoresQue4(notas) and 4<=promedio(notas)<7):
        return 2
    elif (not(todasLasNotasSonMayoresQue4(notas)) or promedio(notas)<4):
        return 3

#ej corregido del 3.1
def aprobado(notas: list[int]) -> int:
    total_notas: int = 0

    for nota in notas:
        total_notas += nota

        if nota < 4:
            return 3  # Si alguna nota es menor a 4, el estudiante no aprueba de inmediato.

    promedio: float = total_notas / len(notas)

    if promedio < 4:
        return 3
    elif promedio >= 7:
        return 1
    else:
        return 2
    
#GUIA 7, EJERCICIO 4
"""
ej4.1 -> estudiantes
ej4.2 -> monedero
ej4.3 -> juego 7_medio
"""

# 5.2
def esMatriz(s: list[list[int]]) -> bool:
    for i in range(1,len(s)):
        if len(s[i]) != len(s[0]):
            return False
    return True

print("esMatriz da ",esMatriz([[0,1,2],[3,4]]))





















def long_mayor_a_8 (x:str)-> bool:
    return len (x) > 8

def long_menor_a_5 (x:str) -> bool:
    return len (x) < 5 

def hay_minuscula (x:str) -> bool:
    for letra in x:
        if (letra >= 'a' and letra <= 'z'): 
            return True
    return False

def hay_mayuscula (x:str) -> bool:
    for letra in x:
        if (letra >= 'A' and letra <= 'Z'): 
            return True
    return False   

def hay_numeros (x:str) -> bool:
    for letra in x:
        if (letra >= '0' and letra <= '9'): 
            return True
    return False             
        

def seguridad_contraseña (x:str)-> str:
    if (long_mayor_a_8(x) and hay_mayuscula(x) and hay_minuscula(x) and hay_numeros(x)):
        return "Verde"
    elif (long_menor_a_5(x)):
        return "Rojo"
    else:
        return "Amarillo" 

def cero_en_pares(x:list[int]):
    for i in range (0,len(x),2):
        x[i] = 0 

def pertenece (x:list[int], e:int)->bool:
    for i in x:
        if (i == e): 
            return True
    return False

def pertenece_a_cada_uno_v2 (s:list[list[int]], e:int, res:list[bool]):
    res.clear()
    for lista in s: 
        if pertenece (lista, e): 
            res.append(True)
        else:
            res.append(False)     

s = [[1,2,3],[4,2,3],[8,8,8]]
e = 2 
res = []

pertenece_a_cada_uno_v2(s,e,res)
print(res)

#GUIA NUEVA: ARCHIVOS

#.read() = te lee todo el archivo
#.readline() = lee el archivo hasta el momento que pongo enter

def contarlineas(nombre_archivo: str) -> int:
    f = open (nombre_archivo) # f es EL archivo abierto, cuando lo llame por consola es test.contarlineas('nombre_archivo')
    lineas : list[str] = f.readlines() # lee a f y devuelve una lista de str q son las lineas
    cantidad : int = len(lineas)
    f.close() # cierro el archivo abierto
    return cantidad


def clonarsincoment (nombre_archivo:str):
    f = open (nombre_archivo) # f es EL archivo abierto
    sin_comentarios: list [str] = [] # me creo un archivo vacio donde clono el original
    for linea in f.readlines(): # leo a f
        if not linea[0] == "#": # si no hay #, que agregue al archivo nuevo la linea esa
            sin_comentarios.append(linea)
        for caracter in linea:
            if not caracter == " ": # caso si la linea comienza con espacios
                if not caracter == "#":
                    sin_comentarios.append(linea)
                break # si hay espacios no sigo viendo si hay numeral, sigo de largo
    res = open("sin_comentarios"+nombre_archivo,"w") #concateno las listas_archivos pero como va primero sin_comentarios me quita los #
    res.writelines (sin_comentarios) #ya existe y esta abierto mi archivo sin_coment, ahoar escribo en él
    res.close()
    f.close()





