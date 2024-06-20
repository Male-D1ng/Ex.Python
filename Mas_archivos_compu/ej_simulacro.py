#ej_simulacro.py

# Ejercicio 1
"""NO ESTA BIEN XQ LA VARIABLE RES SE SOBRE ESCRIBE Y SEGUN GIT :
al final solo contendrá la posición de la última aparición encontrada durante la iteración,
 no necesariamente la última en la lista
def ultima_aparicion(s: list, e: int) -> int:
    for i in range(0,len(s),1):
        if s[i] == e:
            res = i
    return res
print ("compa da: ", ultima_aparicion([1, 2, 4, 3, 2],3))"""

"""lista1 = [5, 9, 10]
for i in range(0, len(lista1)):
    print(lista1[i]) 
#print(len(lista1))"""

def ultima_aparicion(s: list, e: int) -> int:
    for i in range (len (s)-1,-1,-1):
        if s[i] == e:
            return i

#print ("mio da: ",ultima_aparicion([1, 2, 4, 3, 2],3))

"""
def ultimaaparicion(s: list, e: int) -> int:
    last_index = -1  # Inicializa la variable para almacenar la última posición.

    for i in range(len(s)):
        if s[i] == e:
            last_index = i  # Actualiza la variable si se encuentra una aparición.

    return last_index

#print ("da: ",ultimaaparicion([5,8,5,4,71,6,9,5],5))"""

#ej2 
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

#print (elementos_exclusivos([1,2,3,1,2],[1,2,3,3,4]))

#ej3 :diccionarios
def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res: int = 0
    for clave, valor in ingles.items(): # clave y valor estan en la lista como keys y values respect. del dict ingles
        if clave in aleman.keys(): # se fija si clav esta en la lista de las keys del diccionario.
            if aleman[clave] == valor: #entro al dict aleman y me fijo si el elemento en el index clave coincide con el q esta en el dict ingles
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
#print(convertir_a_diccionario([1,1,2,31,5]))

#otra forma de armar el diccionario
l = [-1, 0, 4, 100, 100, -1, -1]
def diccionario_a_mano (l : list)-> dict:
    d = dict()
    clave = list = []
    valor : int = 0
    #d = {'clave': clave,'valor':valor}
    for i in l:
        if i not in clave:
            clave.append(i) #es como la pos 0, osea la primera, asi q no tengo que acceder a ella
    for valor in l:
        d[valor] = contar(l,valor) #asi accedo al index de valor, y le digo lo que vale
    return d
print(diccionario_a_mano(l))
