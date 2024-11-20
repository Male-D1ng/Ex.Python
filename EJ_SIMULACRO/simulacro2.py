from queue import Queue as Cola


# Ejercicio 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    notas_estudiantes : dict[str,list[tuple[str, int]]] = {}
    for t in notas_estudiante_materia:
        if not pertenece_dic(notas_estudiantes,t[0]):
            lista_notas = []
            lista_notas.append((t[1], t[2])) 
            notas_estudiantes[t[0]] = lista_notas
        else:
            lista_notas = notas_estudiantes[t[0]]
            lista_notas.append((t[1], t[2]))
            
    
    return notas_estudiantes

def pertenece_dic(diccionario:dict, llave:str)-> bool:
    for i in list(diccionario.keys()):
        if llave == i:
            return True
    
    return False


# Ejercicio 2
def cantidad_digitos_pares(numeros: list[int]) -> int:
    lista_nros : list[int] = []
    for n in numeros:
        n = str(n)
        for i in n:
            lista_nros.append(int(i))
    cant : int = 0
    for nn in lista_nros:
        if nn % 2 == 0:
            cant += 1
    return cant

# Ejercicio 3

def reordenar_cola_primero_pesados(paquetes: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    lista_paquetes : list[tuple[str, int]] = []
    paquetes_ordenados : Cola[tuple[str, int]] = Cola()
    while not paquetes.empty():
        item = paquetes.get()
        lista_paquetes.append(item)
    
    for t in lista_paquetes:
        if t[1] > umbral:
            paquetes_ordenados.put(t)

    for t in lista_paquetes:
        if t[1] <= umbral:
            paquetes_ordenados.put(t)

    for i in lista_paquetes:
        paquetes.put(i)
    return (paquetes_ordenados)



paquetes = Cola()
paquetes.put(("a",1))
paquetes.put(("a",8))
paquetes.put(("a",6))
paquetes.put(("a",5))
paquetes.put(("a",4))
paquetes.put(("a",3))
paquetes.put(("a",2))
reordenar_cola_primero_pesados(paquetes, 3)


# Ejercicio 4
def matriz_pseudo_ordenada(matriz: list[list[int]]) -> bool:
    matriz_t : list[list[int]] = []
    i : int = 0
    for l in matriz:
        lista : list[int] = []
        for t in range(len(matriz)):
            lista.append(matriz[t][i])
        matriz_t.append(lista)
        t = 0
        i += 1
    
    minimo:int = -1
    
    for i in matriz_t:
        minimo_actual = i[0]
        for n in i:
            if n <= minimo_actual:
                minimo_actual = n 


            
        if minimo_actual > minimo:
            minimo = minimo_actual
        else: 
            return False
    return True

        
    
    
    
    





