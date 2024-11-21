#intento ej practica 7

#1. Primera Parte

#ej1, pertenece, parte de una lista y el entero "e" y devuelve un bool sobre si "e" pertenece o no



#me creo una lista q vaya desde un v0 = i hasta uun vF = f, va de 1 en 1
def set_listan (i:int,f:int)-> bool: 
     lista = []
     for n in range(i,f,1):
          lista.append(n) 

def pertenece (lista:list, e:int)-> bool:
        if e in lista:
            return True
        else:
            return False

#print (pertenece(set_listan(i,f),e))

s = ["l","e"] 
def pertenece2 (s: list[str], e: str) -> bool:
    for elem in s:
        if elem == e:
            return True
    return False

#print (pertenece2 (s,"e"))

#ej2, divideATodos (in s:seq<Z>, in e: Z) : Bool, para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}

def divideATodos (s:list[int],e:int) -> bool:
     e: int = e != 0
     for i in s:
          if s[i] % e == 0:
               return True
     return False

#ej3,  sumaTotal (in s:seq<Z>) : Z, res es la suma de todos los elementos de s
def sumaTotal (s:list[int])->int:
     res = 0  
     for i in s: 
        res += i   #el operador += ==> res = res + i, y va guardando el valor hasta terminar la lista
     return res

#ej4,  ordenados (in s:seq<Z>) : Bool , i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1]
def ordenados (s:list[int])->bool:
     for i in range (len(s)-1):
          if s[i]>s[i+1]:
               return False
     return True 
               
#ej5, Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7
def mayor_a_7 (l:list[str])->bool:
    for i in l: 
        if len(i)>=7:
            return True
    return False

#ej6, Dado un texto en formato string, devolver verdadero si se lee igual en ambos sentidos
def palabra_reverso (p:list[str])->bool:
     palabra : str = ""
     for i in range(len(p) - 1, -1, -1):
          palabra += p[i] 
     return p == palabra

def palindromo (palabra:list[str])->bool:
      return palabra == palabra[::-1]

#ej7 contraseña : entra un string,  sale otro string con tres posibles valores: VERDE, AMARILLA y ROJA
def contrasena (c:str)->str:
     if len (c) < 5:
          return 'Roja'
     if len (c) > 8:
          if hayMinus(c) and hayMayus(c) and hayNum (c):
               return 'Verde'
     return 'Amarillo'


def hayMinus (m:str) -> bool:
     for letra in m:
          if 'a' <= letra <= 'z':
               return True
          return False
     
def hayMayus (m:str) -> bool:
     for letra in m:
          if 'A' <= letra <= 'Z':
               return True
          return False

def hayNum (n:int)-> bool:
     for num in n :
          if '0' <= num <= '9':
               return True
          return False
     
#ej8 :  lista de tuplas /dado el monto y una letra :“I” para ingreso, “R” para retiro, devuelvo el saldo actual
def segundos_valores (valor:list[tuple[str,int]])-> list[int]:
     monto :list = []
     for segundos in valor:
          monto.append(segundos[1])
     return monto

def primeros_valores (valor:list[tuple[str,int]])-> list[int]:
     monto :list = []
     for segundos in valor:
          monto.append(segundos[0])
     return monto

def suma_monto (monto:list[int])->int:
     suma:int= 0
     for i in monto:
          suma += i
     return suma

def resta_monto (monto:list[int])->int:
     resta:int= 0
     for i in monto:
          resta -= i
     return resta 

#ejemplo compañero
def saldo (s:list[tuple[str,int]])-> int:
     m : int = 0
     for movimiento in s:
          if movimiento [0] == 'I':
               m += movimiento[1]
          elif movimiento [0] == 'R':
               m -= movimiento[1]
     return m 

def saldo_positivo (s:list[tuple[str,int]])-> int:
     m : int = 0
     for movimiento in s:
          if movimiento [0] == 'I':
               m += movimiento[1]
          else:
               break # detiene el programa
     return m 
#NO va WHILE: Sale del bucle cuando el primer movimiento no es un ingreso ('I').
#Y si tuviera un 'R' antes de un 'I', el bucle se detiene después del primer 'R'' y no incluire los 'I' posteriores.
     
def saldo_positivoGIT (s: list[tuple[str, int]]) -> int:
    ingresos = [movimiento for movimiento in s if movimiento[0] == 'I']
    monto_ingresos = suma_monto(segundos_valores(ingresos))
    return monto_ingresos

def saldo_positivoGIT2 (s: list[tuple[str, int]]) -> int:
    ingresos = [movimiento[1] for movimiento in s if movimiento[0] == 'I']
    return suma_monto(ingresos)
#no hizo falta ir a buscar los segundos elemntos de las tuplas, xq ingresos ya filtro


def saldo_positivoGIT3 (s: list[tuple[str, int]]) -> int:
    ingresos = [movimiento[1] for movimiento in s if movimiento[0] == 'I']
    return sum(ingresos)
#lo mismo q arriba, ingresos ya filtro y solo deja los montos donde hay 'I'

#ej9 : ver si tiene al menos 3 vocales distintas 
vocales = ['a','e','e','o','u','A','E','I','O','U']
def esVocal(letra:str) -> bool:
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    if pertenece(vocales, letra):
        return True
    return False

def vocales(palabra:str) -> bool:
    vocales: int = 0
    
    for letra in palabra: #esto es equivalente a for i in range(0,len(palabra),1)
        if esVocal(letra):
            vocales+=1
    
    if vocales >= 3:
        return True
    return False

#PARTE 2

#ej1: en las posiciones pares borra el valor original y coloca un cero, modifica el dato ingresado, es de tipo inout.
def ceroEnPosParInOut(l: list[int]) -> list:
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = 0
    return l

#ej2: sin modificar la lista original, devolviendo una nueva lista, es de tipo in
def ceroEnPosParIn(l:list[int])-> list:
    listaNueva: list = []
    for i in range(len(l)):
        if i % 2 == 0:
            listaNueva.append(0)
        else:
            listaNueva.append(i)
    return listaNueva

#ej3: dado una palabra la devuelve, pero sin las vocales, sin espacios agregados,osea concatena
def palabra_sin_vocales(palabra:str) ->str:

    vocales:str = 'aeiou'
    palabra_sin_vocales:str = ''
    for caracter in palabra:
        if caracter not in vocales:
            palabra_sin_vocales += caracter 

    return palabra_sin_vocales

#ej4: si hay una vocal, reemplazar por un '_'
def palabra_sin_vocales(palabra:str) ->str:

    vocales:str = 'aeiou'
    palabra_sin_vocales:str = ''
    for caracter in palabra:
        if caracter not in vocales:
            palabra_sin_vocales += caracter
        else:
             palabra_sin_vocales += '_'

    return palabra_sin_vocales

#ej5: dar vuelta la palabra, me importa el indice de las letras para asi pedir q primero ponga el ultimo indice y etc
def daVuelta (s:str)-> str:
     res: str = ""
     for i in s: 
          res += s[s- i - 1]
     return res 

def da_vuelta_str(s: str) -> str:
    res: str = ""
    for i in range(len(s)): #itero sobre el indice de s, no los elementos de s
        res += s[len(s) - i - 1]
    return res

def daVuelta_CHATGPT(s: str) -> str:
    return s[::-1]

#ej6

def quitar_letras_repetidas(s: str) -> str:
    resultado = ""
    for letra in s:
        if letra not in resultado: #agrega una letra, cuando va agregar la sig se fija si ya esta en resultado y si lo esta la omite
            resultado += letra
    return resultado

#PARTE 3
#ej1:
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
        
def aprobado(notas:list [int])->int:
    if (todasLasNotasSonMayoresQue4(notas) and promedio(notas)>=7):
        return 1
    elif (todasLasNotasSonMayoresQue4(notas) and 4<=promedio(notas)<7):
        return 2
    elif (not(todasLasNotasSonMayoresQue4(notas)) or promedio(notas)<4):
        return 3
# 
# PARTE 4
def sube()-> int:
    monto : int= 0
    tipo_carga : str= ''
    historial: list = []
    while tipo_carga != 'x':
         tipo_carga = input("OPERACION A REALIZAR: ")
         if tipo_carga == "C":
               saldo = int(input("MONTO: "))
               monto += saldo
               historial.append((tipo_carga, saldo))
         elif tipo_carga == "D":
               saldo = int(input("MONTO: "))
               monto = monto - saldo
               historial.append((tipo_carga, saldo))
    return historial 

def historial_monedero() -> "list[tuple[str, int]]":
    entrada: str = ""
    saldo:int = 0
    res: list[tuple[str, int]] = []
    while entrada != "X":
        entrada = input("Ingrese la operacion que desea realizar\n")
        if entrada == "C":
            monto: int = int(input("Ingrese el monto de la operacion: "))
            saldo += monto
            res.append((entrada, monto))
        elif entrada == "D":
            saldo = int(input("Ingrese el monto de la operacion: "))
            monto = monto - saldo
            res.append((entrada, monto))
    return res

#PARTE 5

#EJ1: DADO s:seq<seq<Z>> Y UN e:Z, DEVOLVER res: seq<Bool>
#def perteneceACadaUno (s:list[list[int]],e:int)-> bool:
#     lista:list = s[0]
#     for lista[0] in lista:
#          pertenece(s,lista[0]) 
#     return False 

def perteneceACadaUnoGIT (s: list[list[int]],e:int)-> bool: 
    # Itera a través de las listas en s
    for lista in s:
        # Verifica si e está en la lista actual
        if e not in lista:
            # Si e no está en alguna de las listas, retorna False
            return False
    # Si e está en todas las listas, retorna True
    return True

# Ejemplo de uso
s = [[1, 2, 3], [3, 4, 5], [2, 6, 7]]
e = 3

if perteneceACadaUnoGIT(s, e):
    print ( e ,"pertenece a todas las listas.") #Para concatenar una variable en una cadena de texto se usan la coma o el +. 
else:
    print (e ," no pertenece a todas las listas.")


#ej2 esMatriz : dado una lista de listas de int devuelve un bool.
#es una matriz válida con al menos una fila y todas las filas de la misma longitud. 
#la matriz s no esté vacía
#El número de elementos en la primera secuencia de s debe ser mayor que cero. 
#Esto garantiza que al menos la primera fila de la matriz no esté vacía.
#todas las filas de la matriz tengan la misma longitud.

def esmatriz(s:list[list[int]])->bool:
    primera_fila = s[0]
    longitud_primera_fila = len(primera_fila)
    if len(s)==0: #verificó primero si la matriz está vacía
        return False
       
    if len(primera_fila) == 0: #verifico que la primera fila no esté vacía.
        return False
    for fila in s:
        if len(fila) != longitud_primera_fila: #verifico que todas las filas tengan la misma longitud 
            return False
        
    return True
   
print(esmatriz(s))

#ej3 filasOrdenadas : entre una lista de listas de int y sale lista de bool
#MAL HECHO: EL WHILE ESTA DEMAS, EL ASEGURA DE LA MATRIZ NO HACIA FALTA PONERLO Y SOBRECOMPLIQUE EL APPEND
#def filasOrdenadas(m:list[list[int]])-> list[bool]:
#lista_bool : list[bool] = []
#primera_fila : list[int] = s[0]
#while esmatriz(m) == True:
# for fila in m:
# if ordenados(fila) == True:
#  primera_fila = True
# res = lista_bool.append(primera_fila)
#return res  
# else:
# primera_fila = False
#res = lista_bool.append(primera_fila)
# return res
            
def filasOrdenadas(m:list[list[int]])-> list[bool]:
    lista_bool = []
    if esmatriz(m) != True: #si no cumple el asegura, hace un break
        return lista_bool
    for fila in m:
          if ordenados(fila): #se fija si cumple con lo q pide ordenados()
               lista_bool.append(True) #si cumple, agrega un True a la lista_bool

          else:
               lista_bool.append(False) #si no cumple, agrega un False a la lista_bool

    return lista_bool




#ej4  elevarMatriz
import numpy as np

d: int = 2
m = np.random.random((d,d))**2
p: float = int(74)

def multiplicacion(m:list[list[float]]) -> list[list[float]]:
    filas: int = len(m)
    columnas: int = len(m[0])
    res: list[list[float]] = np.zeros((d, d)) #iniciar el res en 0


    for i in range(0,filas,1):
        for j in range(0,columnas,1):
            for k in range(0,columnas,1):
                res[i][j] += m[i][k] * m[k][j]

    return res

def elevarMatriz(m:list[list[float]],p:float) -> list[list[float]]:
    res = m

    for i in range(0,p-1):
        res = multiplicacion(m)
    return res

import numpy as np

def elevar_matriz(matriz, p):
    if not isinstance(matriz, np.ndarray) or matriz.shape[0] != matriz.shape[1]:
        raise ValueError("La matriz debe ser cuadrada y de tipo ndarray de NumPy.")
    
    if p < 0:
        raise ValueError("El exponente debe ser un número no negativo.")
    
    return np.linalg.matrix_power(matriz, p)

# Ejemplo de uso:
d = 3  # Tamaño de la matriz cuadrada (3x3 en este caso)
p = 2  # Potencia a la que se elevará la matriz

# Generar una matriz cuadrada aleatoria de tamaño d
matriz_cuadrada = np.random.rand(d, d)

# Elevar la matriz a la potencia p
resultado = elevar_matriz(matriz_cuadrada, p)

print("Matriz original:")
print(matriz_cuadrada)
print("\nMatriz elevada a la potencia", p, ":")
print(resultado)



