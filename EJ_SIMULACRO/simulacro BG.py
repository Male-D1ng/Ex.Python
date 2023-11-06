# Ejercicio 1
def ultima_aparicion(s: list, e: int) -> int:
    for i in range(len(s)):
        if s[i] == e:
            res = i
    return res

# Ejercicio 2
def elementos_exclusivos(s: list, t: list) -> list:
    lista_nueva:list = []
    for i in s:
        if i not in t:
            lista_nueva.append(i)
    for j in t:
        if j not in s:
            lista_nueva.append(j)
    lista_sin_repetidos: list = []
    for k in lista_nueva:
        if k not in lista_sin_repetidos:
            lista_sin_repetidos.append(k)
    return lista_sin_repetidos

# Ejercicio 3

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res:int = 0
    for clave, valor in ingles.items():
        if clave in aleman.keys():
           if aleman[clave] == valor:
               res += 1
    return res

# Ejercicio 4

def cuento (e:int, lista:list) -> int:
    res = 0
    for i in lista:
        if i == e:
            res +=1
    return res
def convertir_a_diccionario(lista: list) -> dict:
    d = {}
    lista_de_claves = []
    for i in lista:
        if i not in lista_de_claves:
            lista_de_claves.append(i)
    for clave in lista_de_claves:
        d[clave] = cuento(clave, lista)
    return d
        
