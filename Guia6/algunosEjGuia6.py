#Programa Python Ejemplo 
 # problema suma2(x : Z, y : Z) : Z{
  #  asegura: res = x + y
  #}
 # def suma2 (x: int, y: int) -> int:
  #res: int = x + y
  #return res  
#} 

##para ejecutar python : python3 -> import archivo -> test.funcion(), para salir es Ctrl-d 
## tengo q asignarle un tipo al dato: los de entrada van entre () y el de salida va por afuera dps de ->
  
def prueba (): 
    print ("hola")

prueba ()

def imprimir_holas ():
    print ('holas') 


def es_multiplo_de (n:int,m:int)-> bool:
    res: bool = (n % m) == 0  #significa mod 
    return res 

def es_nombre_largo (nombre:str) -> bool :
    res:bool = 3 <= len(nombre) and len(nombre)<= 8 
    return res 

## el && se escribe and y en la consola los string (str) van con doble comilla

def devolver_el_doble_si_par (par:int) -> int:
    if es_multiplo_de (par,2) :
        res: int = 2*par 
    else:
        res: int = par
    return res 

def imprimir_pares ():
    i : int = 10
    while i <= 40 :
        print (i)
        i = i + 2

## otra forma de escribirlo
def imprimir_pares ():
    i : int = 10
    while i <= 40 :
        if es_multiplo_de (i,2): 
            print (i)
        i = i + 1
def imprimir_pares_for ():
    for i in range(10,41,2) # sea range (i,n,j), devuelve hasta el j-1 
        print(i) 

def cancion (): # el '\n' significa q respeta los saltos de linea de los versos
    print ("I'am'\n'taking'\n'a'\n'ride'\n'with'\n'my'\n'best'\n'friend")

def raizDe2 (): #primero hay q hacer un import math para usar la raiz. round redondea a 4 digitos en este caso
    print (round(math.sqrt(2), 4) )

def factorial (f:int) -> int: 
    res : int = 1
    for i in range (1,f+1):
       res = res * i 
       print (res)
    return res 

def factorial_while (n:int) -> int :
    res:int = n
    i:int = n-1
    while i>0:
        res = res*i
        i = i-1
        print(res)
    return res 

def factorial2 (i:int) -> int:
    res:int = factorial (i) * 2


#perimetro: que devuelva el per´ımetro de la circunferencia de radio 1.
def perimetro ():
    print (2*math.pi) 

# esta mal, hago q r se divide x si mismo, por eso me da 1.0
def raiz_cuadrada (r :int) -> int:
    i:int = r  
    if es_multiplo_de (r,i):
        res : int = r/i
    else: 
        res :int = r
    return res 


def factorial_de2 (f:int)-> int :
    res : int = 2*factorial (f)
    return res 
  
## otro de raiz, esta mal pero ya me acerco a la correcta especificacio
def raiz_cuadrada (r :int) -> int:
    if es_multiplo_de (r,2): 
        res : int = int (r/2)
    else:
        res : int = int (r/3) # el int me da la parte entera de esa div
    return res 



