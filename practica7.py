#intento ej practica 7

#1. Primera Parte

#ej1, pertenece, parte de una lista y el entero "e" y devuelve un bool sobre si "e" pertenece o no

lista = [1, 2, 3, 4, 5]
def pertenece (lista:list, e:int)-> bool:
        if e in lista:
            return True
        else:
            return False

#print (pertenece(lista,11))

#me creo una lista q vaya desde un v0 = i hasta uun vF = f, va de 1 en 1
def set_listan (i:int,f:int)-> bool: 
     for n in range(i,f,1):
          lista.append(n) 
          

s = ["l","e"] 
def pertenece2 (s: list[str], e: str) -> bool:
    for elem in s:
        if elem == e:
            return True
    return False

#print (pertenece2 (s,"e"))

#ej2, divideATodos (in s:seq<Z>, in e: Z) : Bool, para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}

def divideATodos (s:list[int],e:int) -> bool:
     e: int != 0
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
               break
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
