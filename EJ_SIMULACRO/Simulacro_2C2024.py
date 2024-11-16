#ss
"""
problema gestion_ventas (in ventas_empleado_producto: seq⟨(String x String x Z)) : dict⟨String, seq⟨(String x Z)⟩⟩ {
  requiere: { Las primeras componentes de ventas_empleado_producto tienen longitud mayor estricto a cero}
  requiere: { Las segundas componentes de ventas_empleado_producto tienen longitud mayor estricto a cero}
  requiere: { Las terceras componentes de ventas_empleado_producto son mayores estricto que 1 }
  requiere: { No hay 2 tuplas en ventas_empleado_producto que tengan la primera y segunda componente iguales (mismo empleado y mismo producto) }
  asegura: {res tiene como claves solo los primeros elementos de las tuplas de ventas_empleado_producto (o sea, un empleado)}
  asegura: {El valor en res de un empleado es una lista de tuplas donde cada tupla contiene como primera componente el nombre del producto y como segunda componente la cantidad vendida por el empleado de ese producto según ventas_empleado_producto}
  asegura: { Para toda clave (empleado) en res, en su valor (lista de tuplas) no hay 2 tuplas que tengan la misma primera componente (producto) }
}
"""
def gestion_ventas (ventas_empleado_producto:list[tuple[str,str,int]])->dict[str,list[tuple[str,int]]]:
    diccionario :dict[str,tuple[str,int]] = {}
    
    for empleado in range(len(ventas_empleado_producto)):
        persona:str = ventas_empleado_producto[empleado][0]
        producto:str = ventas_empleado_producto[empleado][1]
        cantidad_producto:int=ventas_empleado_producto[empleado][2]
        cantidad = cantidad_producto
        if not pertenece(persona,diccionario.keys()):
            cantidad = cantidad_producto
            diccionario[persona]= [(producto,cantidad)]
        #diccionario[empleado] = (producto,cantidad)
        else:
            diccionario[persona].append((producto,cantidad))
    return diccionario


def pertenece(nombre:str,lista:list[str])->bool:
    for n in lista: #agarra cada elemento de la lista
        if nombre == n:
            return True
    return False 


lista = [("eli","tupper",1),("manny","sopas",2),("eli","lapiz",3)]
#print(gestion_ventas(lista))



"""
 problema cantidad_digitos_impares (in numeros: seq⟨Z⟩) : Z {
  requiere:{Todos los elementos de numeros son mayores iguales a 0}
  asegura: {res es la cantidad total de digitos impares que aparecen en cada uno de los elementos de numeros}
}

Por ejemplo, si la lista de números es [57, 2383, 812, 246], entonces el resultado esperado sería 5 (los dígitos impares son 5, 7, 3, 3 y 1).

"""
def cantidad_digitos_impares(numeros:list[int])->int:
    cantidad:int = 0
    f = len(numeros)
    for n in range(0,f,1):
        num = numeros[n]
        while num >= 10:
            if (num%10) % 2 != 0:
                cantidad += 1
            num = (num-(num%10))/10
        if num % 2 != 0:
            cantidad += 1
        
    return cantidad

l = [57, 2383, 812, 246]
print(cantidad_digitos_impares(l))


"""
 Cada carpeta está representada por una tupla (id_carpeta, numero_paginas), donde id_carpeta es un identificador único de la carpeta y numero_paginas es el número de páginas que contiene.

Se pide implementar una función en Python llamada reordenar_cola_primero_numerosas que respete la siguiente especificación:

problema reordenar_cola_primero_numerosas(in carpetas: Cola⟨(String x Z)⟩, in umbral:Z): Cola⟨(String x Z)⟩{
  requiere: {no hay repetidos en las primeras componentes (Ids) de carpetas}
  requiere: {todos las segundas componentes (número de páginas) de carpetas son mayores estricto a cero}
  requiere: {umbral es mayor o igual a cero}
  asegura: {los elementos de res son exactamente los mismos que los elementos de carpetas}
  asegura: {|res| = |carpetas|}
  asegura: {no hay un elemento en res, cuyo número de páginas sea menor o igual que el umbral, que aparezca primero que otro elemento en res cuyo número de páginas sea mayor que el umbral)}
  asegura: {Para toda carpeta c1 y carpeta c2 cuyas número de páginas son menores o iguales que el umbral y pertenecen a carpetas, si c1 aparece primero que c2 en carpetas entonces c1 aparece primero que c2 en res}
  asegura: {Para toda carpeta c1 y carpeta c2 cuyas número de páginas son mayores que el umbral y pertenecen a carpetas, si c1 aparece primero que c2 en carpetas entonces c1 aparece primero que c2 en res}
}
"""

"""
Se desea verificar si una matriz es cuasi decreciente por columnas. Esto es que el máximo de cada columna sea mayor estricto que el máximo de la columna siguiente

Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:

matriz_cuasi_decreciente (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {todos los elementos de matriz tienen la misma longitud}
  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el máximo de la columna i de matriz > el máximo de la columna i + 1 de matriz }
}
"""
