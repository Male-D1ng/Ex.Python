{--Programa Python
--Ejemplo
problema suma2(x : Z, y : Z) : Z{
asegura: res = x + y
}
def suma2 (x: int, y: int) -> int:
res: int = x + y
return res 
--}

{--ASIGNACIÓN : Es la operaci´on fundamental para modificar el valor de una variable.
▶ Sintaxis: variable = expresi´on;
▶ Es una operaci´on asim´etrica
▶ Lado izquierdo: debe ir una variable u otra expresi´on que represente
una posici´on de memoria.
▶ Lado derecho: una expresi´on del mismo tipo que la variable
▶ constante,
▶ variable o
▶ funci´on aplicada a argumentos.
▶ Efecto de la asignaci´on:
1. Se eval´ua la expresi´on de la derecha y se obiene un valor.
2. Ese valor se copia en el espacio de memoria de la variable.
3. El resto de la memoria no cambia.
--}

{--Instrucción Return :Termina la ejecuci´on de una funci´on.
▶ Retorna el control a su invocador.
▶ Devuelve el valor de la expresi´on como resultado.
problema suma2(x : Z, y : Z) : Z{
asegura: res = x + y
}
def suma2 (x: int, y: int) -> int:
res: int = x + y
return res
def suma2 (x: int, y: int) -> int:
return x + y 
--}


