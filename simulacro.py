#ej1_simulacro

def pertenece2 (s: [int], e: int) -> bool:
    for elem in s:
        if elem == e:
            return True
    return False

print (pertenece2 ([1,2,3,1,2],1))


def quitar_num_repetidos(s: [int]) -> [int]:
    resultado :list = []
    for num in s:
        if num not in resultado: 
            resultado.append(num)
    return resultado

print (quitar_num_repetidos ([1,2,3,1,2]))

def ultima_aparicion(s: list, e: int) -> int:
    for i in range (len (s)-1,-1,-1):
        if s[i] == e:
            return i

print (ultima_aparicion([1,2,3,1,2],1))

#ej2:_simulacro

def elementos_exclusivos(s: list, t: list) -> list:
    res: list = []
    for num in s:
        if num not in t: 
            if num not in res: 
                res.append(num)
        for num in t:
            if num not in s: 
                if num not in res:
                    res.append(num)
    return res

print (elementos_exclusivos([1,2,3,1,2],[1,2,3,3,4]))

#ej3 :diccionarios
def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res: int = 0
    for clave, valor in ingles.items():
        if clave in aleman.keys():
            if aleman[clave] == valor:
                res += 1
    return res 

#ej4: diccionarios
def contar (lista:[int],e:int)-> int:
    contador: int = 0
    for l in lista:
        if l == e:
            contador += 1
    return contador

def convertir_a_diccionario(lista: list) -> dict:
    d = dict()
    clave : list= []
    for i in lista:
        if i not in clave:
            clave.append(i)
    for valor in lista:
        d[valor] = contar(lista,valor)
    return d
print(convertir_a_diccionario([1,1,2,31,5]))






