#ejemplo while

numero: int = int(input('Ingresa un número. 0 para terminar: '))

while(numero != 0):
    print('Usted ingresó: ', numero)
    numero = int(input('Ingresa un número. 0 para terminar: '))
   
print('Fin del programa.')

#ejemplo scope refer
# problema duplicar(in x: seq<int>, out y: seq<int>) 
#     asegura: y = x ++ x

def duplicar(x: list, y: list): 
    y = x
    y *= 2 

x: list = ['a', 'b', 'c'] 
y: list = ['d', 'e'] 
print("ANTES: ") 
print("x: " + str(x))  
print("y: " + str(y))
duplicar(x, y)
print("DESPUES: ") 
print("x: " + str(x))  
print("y: " + str(y))

#ejemplo scope python
def outer():
    
    enclosed: int = 1

    def inner():
        local: int = 2
        print("INNER: variableGlobal declarada fuera de todo: ", variableGlobal)
        print("INNER: enclosed declarada en outer: ", enclosed)
        print("INNER: local declarada en inner: ", local)
    
    inner()
     
    print("OUTER: variableGlobal declarada fuera de todo: ", variableGlobal)
    print("OUTER: enclosed declarada en outer: ", enclosed)        
    print("OUTER: local declarada en inner: ", local)
    
variableGlobal: int = 3
outer()
print("GLOBAL: variableGlobal declarada fuera de todo: ", variableGlobal)
print("GLOBAL: enclosed declarada en outer: ", enclosed)        
print("GLOBAL: local declarada en inner: ", local)

#ejemplo localscope
def ejemploLocalScope():
    x: int = 19
    print("x: " + str(x))
     

ejemploLocalScope()
print("x: " + str(x))

#ejemplo if scope
x: int = 10
if(x > 5):
    y: int = 6
else:
    y: int = 12

print("y = " + str(y))

#ejemplo if 
def elegirMayor(x: int, y: int) -> int:
    z: int
    print("x = " + str(x) + " | y = " + str(y) )
    if x > y :
        print("x es mayor que y")
        z = x
        print("(Se cumple B) -> z toma el valor de x")
    else:   
        print("y es mayor o igual que x")
        z = y
        print("(No se cumple B) -> z toma el valor de y")
        
    return z

x: int = 4
y: int = 12

mayor: int = elegirMayor(x, y)
print("z = " + str(mayor))

#ejemplo identacion

def suma(a: int, b: int)->int:
    resultado: int = a + b
    return resultado

print(suma(2,3))

#ejemplo global scope
def ejemploGlobalScope():
    print("x: " + str(x))
     
def sumarEnElGlobal():
    global x
    x = x + 120
    print("x: " + str(x))

x: int = 20
ejemploGlobalScope()
sumarEnElGlobal()
ejemploGlobalScope()
print("x: " + str(x))

#ejemplo for

for i in range(500, 1000, 100):
    print(i)

#ejemplo break
while(True):
    numero = int(input('Ingresa un número. 0 para terminar: '))
    print('Usted ingresó: ', numero)
    if(numero==0):
        break
   
print('Fin del programa.')

#ejemplo duplicar salida por consola
def duplicar(valor: str, referencia: list):  
    valor *= 2
    print("Dentro de la función duplicar: str: " + valor)
    referencia *= 2
    print("Dentro de la función duplicar:  referencia: " + str(referencia)) 


x: str = "abc"
y: list = ['a', 'b', 'c'] 
print("ANTES: ") 
print("x: " + x)  
print("y: " + str(y))
duplicar(x, y)
print("DESPUES: ") 
print("x: "  + x)
print("y: " + str(y))

#ejemplo duplicar inout
# problema duplicar(inout x: seq<int>) 
#     modifica x 
#     asegura: x = x@pre ++ x@pre

def duplicar(x: list): 
    x *= 2

x: list = ['a', 'b', 'c'] 
print("ANTES: ") 
print("x: " + str(x))  
duplicar(x)
print("DESPUES: ") 
print("x: " + str(x))  

#ejemplo duplicar in return
# problema duplicar(in x: seq<int>): seq<int>
#     asegura: res = x ++ x

def duplicar(x: list): 
    y: list = x.copy()
    y *= 2 
    return y


x: list = ['a', 'b', 'c'] 
print("ANTES: ") 
print("x: " + str(x))  
y: list = duplicar(x)
print("DESPUES: ") 
print("x: " + str(x))  
print("y: " + str(y))

#ejemplo duplicar inout
# problema duplicar(in x: seq<int>, out y: seq<int>) 
#     asegura: y = x ++ x

def duplicar(x: list, y: list): 
    y.clear()
    y += x
    y *= 2 

x: list = ['a', 'b', 'c'] 
y: list = ['d', 'e'] 
print("ANTES: ") 
print("x: " + str(x))  
print("y: " + str(y))
duplicar(x, y)
print("DESPUES: ") 
print("x: " + str(x))  
print("y: " + str(y))

