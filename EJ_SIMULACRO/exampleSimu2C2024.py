from queue import Queue as Cola

# Ejercicio 1
def gestion_ventas(ventas_empleado_producto: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    return {} 
 

# Ejercicio 2
def verfica_si_es_impar(num: int) -> bool:
    if(not num % 2 == 0):
        return True
    else:
        return False
    
def cantidad_digitos_impares(numeros: list[int]) -> int:
    res: list[int] = []
    cont: int = 0
    for i in range(len(numeros)):
        evalua: int = numeros[i]
        while(evalua > 1):
            variable = evalua % 10
            if(verfica_si_es_impar(int(variable))):
                res.append(int(variable))
            evalua = evalua / 10
    return res 

# Ejercicio 3
def reordenar_cola_primero_numerosas(carpetas: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:

    return Cola()

# Ejercicio 4
def dice_cual_es_maximo(numeros : list[int]) -> int:
    max: int = numeros[0]
    for i in range(len(numeros)):
        if(numeros[i] > max):
            max = numeros[i]
    return max

def matriz_cuasi_decreciente(matriz: list[list[int]]) -> bool:
    cont:int = 0
    maximo_matriz: int = dice_cual_es_maximo(matriz[0])
    for i in range(len(matriz)):
        if(maximo_matriz <= dice_cual_es_maximo(matriz[i])):
            cont+=1
    if(cont > 1):
        return False
    return True


    
