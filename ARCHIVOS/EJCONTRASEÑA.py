# hhhh
#1.3 suma total : suma detodos los elementos de la lista de enteros s
#Python 3.9 o superior
""" Python 3.9 o superior
En esta version de Python los tipos se escriben con la primera letra
en minuscula y NO debemos importar el nombre del tipo que
queremos usar:
x : l i s t [ i n t ] = [ 1 ]
# Para d i c c i o n a r i o s debemos d e c l a r a r e l t i p o de d a t o de l a c l a v e y l o s v a l o r e s
x : d i c t [ s t r , f l o a t ] = {” c l a v e ” : 2 . 0 }
# Para l a s t u p l a s debemos d e c i r e l t i p o de d a t o de t o d o s l o s v a l o r e s
x : t u p l e [ i n t , s t r , f l o a t ] = ( 3 , ” S i ” , 7 . 5 )
"""
def suma (s: list[int]) -> int:
    suma: int = 0
    #s[i] = accede al elemento de s
    for i in s:
        suma += i
    return suma 
#print(suma([2,2,2]))


def suma2 (s: list[int]) -> int:
    suma2: int = 0 
    i : int = 0
    while i < len(s):
        suma2 += s[i]
        i+=1
    return suma2 
#print(suma2([2,2,2]))

#pertenece de 3 formas
def pertenece1 (s:list[int], i:int)-> bool:
    for n in s:
        if i == n:
            return True
    return False 
print (pertenece1 ([1,2,3],1))

def pertenece2 (s:list[int], i:int)-> bool:
    n: int = 0
    loEncontre:bool = False #valor x defecto es q no lo encontre
    while n < len(s) and not loEncontre: #while comienza a mirar desde el primer elem
        if s[n] == i:
            loEncontre = True 
        n+=1 #conviene q el iterador del vile no este dentro de un if, puede quedarse adentro  no salir
    return loEncontre 
print (pertenece2 ([1,2,3],2))

#es_nro = (caracter =< '9') and (caracter >= '0')
"""
Ejercicio 1.7: dos formas de verificar “tiene al menos un”
(forma 1)
i: int = 0
vale_condicion: bool = False
while i < len(contrasena):
    if condicion:
        vale_condicion: bool = True
    i += 1
(forma2)
i: int = 0
vale_condicion: bool = False
while i < len(contrasena) and not condicion:
    i += 1
vale_condicion: bool = i < len(contrasena)
"""
""" qvq: VERDE si:
a) longitud es mayor a 8 caracteres
b) tiene al menos una minuscula
c) tiene al menos una mayuscula
d) tiene al menos un numero (0...9)
        ROJA si:
a) longitud es menor a 5 caracteres
        AMARILLA en caso contrario 
"""

def fortaleza (contrasena:str)-> str:
    tieneMinus: bool = False
    tieneMayusc :bool = False 
    tieneNum : bool = False
    i:int = 0
    while i < len(contrasena):
        if 'a'<=contrasena[i] and contrasena <= 'z':
            tieneMinus = True
        if 'A'<=contrasena[i] and contrasena <= 'Z':
            tieneMayusc = True 
        if '0'<=contrasena[i] and contrasena <= '9':
            tieneNum = True 
        i +=1
    if tieneMayusc and tieneMinus and tieneNum and len(contrasena)> 8:
        print('verde')
    elif len(contrasena)<5:
        print('rojo')
    else:
        print('amarillo')
        
        
         



