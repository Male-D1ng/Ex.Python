# 1) PILAS

#ej 1.1 generar_nros_al_azar
from queue import LifoQueue as Pila 
from typing import TextIO
import random 

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)-> Pila[int]: 
    p:Pila[int]= Pila() 
    n = cantidad
    while n > 0:
          nro:int = random.randint(desde, hasta)
          p.put(nro)
          n -= 1
    return p

#FUNCION PARA IMPRIMIR PILAS Y COLAS 
def impresora (p:Pila[int])-> None: #tbien podria devolver una lista 
    paux:Pila[int]= Pila()
    while not p.empty(): 
       elem:int = p.get() 
       print(elem) 
       paux.put(elem)
    while not paux.empty():
       i = paux.get()
       p.put(i)


p = Pila() 
#p. put(1) #apilar 
#lemento = p.get() #desapilar 
#p.empty #bool, pregunta si es vacia 
cantidad = 5 
desde = 1 
hasta = 10
p = generar_nros_al_azar(cantidad,desde,hasta) 
impresora(p) 

# otra forma de escribir la funcion generar_nros_al_azar
def generar_nros_azar(cantidad : int, desde : int, hasta : int) -> Pila[int]:
    pila: Pila [int] = Pila()
    for _ in range(0,cantidad,1): #si lo comenzara desde el 1 seria cantidad+1
        elem: int = random.randint(desde, hasta)
        pila.put(elem)
    return pila

def mostrar_elems_pila(p:Pila[int]): #in
    paux:Pila[int] = Pila()
    while not p.empty():
        elem: int = p.get()
        print(elem)
        paux.put(elem)
    while not paux.empty():
        e:int = paux.get()
        p.put(e)

cantidad = 5
desde = 1
hasta = 10
p:Pila[int] = Pila()
p = generar_nros_azar (cantidad, desde, hasta)
mostrar_elems_pila(p)
print ("Mostrar de nuevos eltos pila")





# ej 1.3 buscar_el_maximo
def buscar_el_maximo(c : Pila [int]) -> int:
    maximo: int = 0
    paux:Pila[int] = Pila()
    while not c.empty():
        elem: int = c.get()
        paux.put(elem)
        if elem > maximo:
            maximo = elem
    while not paux.empty():
        e:int = paux.get()
        c.put(e)
        #c.put(paux.get())
    return maximo

def buscar_el_maximo_v2(c : Pila [int]) -> int:
    paux:Pila[int] = Pila()
    if not p.empty():
        maximo: int = c.get()
        paux.put(maximo)
    else:
        maximo = None
    while not c.empty():
        elem: int = c.get()
        paux.put(elem)
        if elem > maximo:
            maximo = elem
    while not paux.empty():
        e:int = paux.get()
        c.put(e)
    return maximo

c = Pila()
c.put(-1)
c.put(-2)
c.put(-3)
c.put(-7)
c.put(-3)
c.put(-4)
print("el maximo es ",buscar_el_maximo(c))
print("el maximo_v2 es ",buscar_el_maximo_v2(c))


p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(7)
p.put(3)
p.put(4)

c = Pila()
c.put(-1)
c.put(-2)
c.put(-3)
c.put(-7)
c.put(-3)
c.put(-4)
print("el maximo es ",buscar_el_maximo(p))
print("el maximo_v2 es ",buscar_el_maximo_v2(c))

#ej1.4 buscar_nota_maxima, devuelve una tupla dnde aparece la maxima nota en la segunda componente de la tupla 
def buscar_nota_maxima (p : Pila[tuple[str,int]]) -> tuple[str,int]:
    paux: Pila[tuple [str,int]] = Pila()
    if not p.empty():
        maximo: tuple[str,int] = p.get()
        paux.put(maximo)
    while not p.empty():
        elem: tuple[str,int] = p.get()
        paux.put(elem)
        if elem[1] > maximo[1]:
            maximo = elem
    while not paux.empty():
        f = paux.get()
        p.put(f)
    return maximo

#ej5 esta_bien_balanceada
#def esta_bien_balanceada (s: str) -> bool:
def formula_bien_balanceada(formula: str) -> bool:

    p:Pila[str] = Pila()

    for c in formula:
        if c == "(" or c == ")":
            p.put(c)
    
    n: int = 0

    while not p.empty() and n >= 0: #me fijo que la cantidad sea siempre 0 y eso solo pasa si hay una de cada corchetes
         parentesis = p.get()

         if parentesis == ')':
              n += 1
         elif parentesis == '(':
              n -= 1

    return n == 0
            
print("esta bien balanceada? =",formula_bien_balanceada("3*(5*5)-(5-4)"))
#formula_bien_balanceada("7((3/7)")
#formula_bien_balanceada("(10*(-1)))")
#formula_bien_balanceada("(4*(-1)))")
#formula_bien_balanceada("))9+7((")


def esta_bien_balanceada (s:str)-> bool:
    p = Pila ()
    for str in s: 
        if str == '(':
            p.put(str)
        elif str == ')':
            if p.empty():
                return False
            p.get(str)
    if p.empty():
        return True
    else:
        return False
print('la formula esta balanceada: ',esta_bien_balanceada('1 + (2 x 3 - (20 / 5))'))

#ej6 buscar_minimo, version min de buscar maximo
def buscar_minimo (p:Pila[int])->int:
    paux:Pila[int]=Pila() #creo una p aux vacia
    minimo:int=p.get()
    paux.put(minimo) #ya lo voy guardando en la auxiliar
    while not p.empty():
        elem:int=p.get()
        paux.put(elem)
        if elem<minimo:
            minimo = elem
    while not paux.empty():
        p.put(paux.get())

    return minimo

p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(7)
p.put(3)
p.put(4)

print("el minimo es", buscar_minimo(p))

#ej7 intercalar dos pilas en una sola, el tope de la pila rta sera el tope de la pila2, hay q recorrer dos veces para que queden en el orden apropiado
def intercalar (p:Pila[int],q:Pila[int])-> Pila[int]:
    paux:Pila[int]=Pila()
    qaux:Pila[int]=Pila()
    s:Pila[int]=Pila()
    while not p.empty() and not q.empty():
        m = q.get()
        qaux.put(m)
        s.put(m)
        e = p.get()
        paux.put(e)
        s.put(e)
        
    while not paux.empty():
        g = paux.get()
        p.put(g)

    while not qaux.empty():
        h = qaux.get()
        q.put(h)

    return s


p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(7)
p.put(3)
p.put(4)

q = Pila()
q.put(-1)
q.put(-2)
q.put(-3)
q.put(-7)
q.put(-3)
q.put(-4)

s=intercalar(p,q)
mostrar_elems_pila(s)

#ej auxiliar MUY IMPORTANTE, LA INVERTIDA DE LAS PILAS
def invertida(p:Pila[int])->Pila[int]:
    paux:Pila[int]=Pila()
    q:Pila[int]=Pila()
    n:int=0
    while not p.empty():
        e=p.get(n)
        paux.put(e)
        q.put(e)
        n+=1
    while not paux.empty():
        e=paux.get()
        p.put(e)

    return q

p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(7)
p.put(3)
p.put(4)


h = invertida(p)
mostrar_elems_pila(h)
f = h.get(1)
print("el primero ahora es:",f)
print("y la original se ve asi:")
mostrar_elems_pila(p)
y = p.get(1)
print("el primero ahora es:",y)



# 2)COLAS
from queue import Queue as Cola

#ej8 generar_nros_al_azar version Cola
def generar_azar_de_nros(cantidad:int,desde:int,hasta:int)->Cola[int]:
    c:Cola[int]=Cola() #inicio una cola vacia
    while cantidad != 0:
        elem = random.randint(desde,hasta)
        c.put(elem)
        cantidad -=1
        print(elem)
    return c

c=Cola()
desde = 1
hasta = 9
cantidad = 5
print("asi se ve una cola :")
h = generar_azar_de_nros(cantidad,desde,hasta)
f = h.get(1)
print("el primero es : ",f)


#ej9 cantidad_de_elementos
def cantidad_elementos(c:Cola[int])->int:
    caux:Cola[int]=Cola()
    cantidad:int = 0
    while not c.empty():
        elem=c.get()
        caux.put(elem)
        cantidad += 1

    while not caux.empty():
        e = caux.get()
        c.put(e)

    return cantidad

c = Cola()
c.put(5)
c.put(3)
c.put(6)
c.put(9)
c.put(8)
c.put(6)
print("la cantidad de elementos es:",cantidad_elementos(c))


#ej10 buscar el maximo de una cola y que devuelva un int


def buscar_maximo (c: Cola[int])->int:
    caux:Cola[int]=Cola()
    maximo:int=c.get()
    caux.put(maximo)
    while not c.empty():
        elem=c.get()
        caux.put(elem)
        if maximo<elem:
            maximo=elem
    while not caux.empty():
        c.put(caux.get())
    return maximo

c=Cola()
c.put(2)
c.put(58)
c.put(5)
c.put(6)
c.put(7)
print("el maximo de la cola es",buscar_maximo(c))

#ej11 buscar nota minima de una cola y devolver la tupla donde esta la nota minima
def buscar_nota_minima (c:Pila[tuple[str,int]])->tuple[str,int]:
    caux:Pila[tuple[str,int]]=Pila()
    minimo:tuple[str,int]=c.get()
    caux.put(minimo)
    while not c.empty():
        elem=c.get()
        caux.put(elem)
        if minimo>elem:
            minimo=elem
    while not caux.empty():
        c.put(caux.get())
    return minimo

c=Cola()
c.put(("fisica",58))
c.put(("mate",5))
c.put(("arte",2))
c.put(("geo",6))
c.put(("lengua",7))
print("el minimo de la cola es",buscar_nota_minima(c))

#ej12 intercalar dos colas, el primer elemento de la rtado es el primer elem de la c1
def intercolar(c: Cola[int], d: Cola[int])->Cola[int]:
    caux:Cola[int]=Cola()
    daux:Cola[int]=Cola()
    res:Cola[int]=Cola()
    while not c.empty() and not d.empty():
        elem1=c.get()
        res.put(elem1)
        print(elem1)
        caux.put(elem1)
        elem2=d.get()
        res.put(elem2)
        print(elem2)
        daux.put(elem2)
    while not caux.empty() and not daux.empty():
        c.put(caux.get())
        d.put(daux.get())
    return res
    

c=Cola()
c.put(2)
c.put(58)
c.put(5)
c.put(6)
c.put(7)

d=Cola()
d.put(26)
d.put(58)
d.put(55)
d.put(68)
d.put(57)

print("cola intercalado por c y d =")
intercolar(c,d)


#ej13 armar_secuencia_bingo() 
from queue import Queue as Cola
def armar_secuencia_bingo() -> Cola[int]:
    cola: Cola[int] = Cola()
    lista: list[int] = list(range(0,100)) #lo transforma en una lista
    random.shuffle(lista) #siempra da nuevos nros
    #print("el largo de la lista es: ", len(lista))
    #print(lista)
    for i in lista:
        cola.put(i)
    return cola

 
def jugarCartonDeBingo(carton: list[int], bolillero: Cola[int]) -> int:
    res: int = 0
    bolillasCarton: int = 0
    bolAux: Cola[int] = Cola()
    while bolillasCarton < len(carton):
        bolilla: int = bolillero.get()
        bolAux.put(bolilla)
        if pertenece(bolilla, carton):
            bolillasCarton = bolillasCarton + 1
        res = res + 1

    while not bolillero.empty():
        bolAux.put(bolillero.get())
    
    while not bolAux.empty():
        bolillero.put(bolAux.get())

    return res

def pertenece(elem: int, lista: list[int]) -> bool:
    res: bool = False
    for x in lista:
        if x == elem:
            res = True
    return res 

def mostrar_elems_cola(p:Cola[int]): #in
    paux:Cola[int] = Cola()
    while not p.empty():
        elem: int = p.get()
        print(elem)
        paux.put(elem)
    while not paux.empty():
        e:int = paux.get()
        p.put(e)

bolillero: Cola[int] = armar_secuencia_bingo()
mostrar_elems_cola(bolillero)
# si queremos mostrar los valores, en orden, del bolillero
carton = [20,10,5,7,99,15,25,30,42,11,47,69] #creamos un carton con 12 elementos
res:int = jugarCartonDeBingo(carton, bolillero)
print("Para ganar con el carton ", carton, "se necesitaron ", res, "jugadas")

#ej14 n_pacientes_urgentes
"""Ejercicio 14. Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atenci´on
para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la mas urgente
y requiere atenci´on inmediata) junto con su nombre y la especialidad m´edica que le corresponde.
Implementar la funci´on n pacientes urgentes(in c : Cola[tuple[int, str, str]]) → int que devuelve la cantidad de pacien-
tes de la cola que tienen prioridad en el rango [1, 3]
"""
from queue import Queue as Cola

def n_pacientes_urgentes(c : Cola[tuple[int, str, str]])-> int:
    caux:Cola[tuple[int, str, str]]=Cola()
    res:int=0
    while not c.empty():
        elem:tuple[int, str, str]=c.get()
        caux.put(elem)
        if elem[0]==1 or elem[0]==2 or elem[0]==3:
            res +=1
    while not caux.empty():
        c.put(caux.get())
    return res

c=Cola()
c.put((1,"gg","hh"))
c.put((2,"gg","hh"))
c.put((5,"gg","hh"))
c.put((7,"gg","hh"))
c.put((1,"gg","hh"))
c.put((3,"gg","hh"))
c.put((2,"gg","hh"))
c.put((9,"gg","hh"))
c.put((10,"gg","hh"))
c.put((3,"gg","hh"))
c.put((2,"gg","hh"))

print("la cantidad de pacientes urgentes es =",n_pacientes_urgentes(c))

#ej15 
"""a gerencia de un banco nos pide modelar la atenci´on de los clientes usando una cola donde se van registrando
los pedidos de atenci´on. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que est´a a la
entrada: Nombre y Apellido, DNI, tipo de cuenta (si es preferencial o no) y si tiene prioridad por ser adulto +65, embarazada o
con movilidad reducida (prioridad si o no).
La atenci´on a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
bancaria preferencial y por ´ultimo el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
1. Dar una especificaci´on para el problema planteado.
2. Implementar atencion a clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que da-
da la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos."""

def impresora(c:Cola[int])->Cola[int]:
    caux:Cola[int]=Cola()
    while not c.empty():
        elem=c.get()
        caux.put(elem)
        print(elem)
    return c

def atencion_a_clientes(c : Cola[tuple[str, int, bool, bool]])-> Cola[tuple[str, int, bool, bool]]:
    caux:Cola[tuple[str, int, bool, bool]]=Cola()
    colaP:Cola[tuple[str, int, bool, bool]]=Cola()
    colaBP:Cola[tuple[str, int, bool, bool]]=Cola()
    colaResto:Cola[tuple[str, int, bool, bool]]=Cola()
    res:Cola[tuple[str, int, bool, bool]]=Cola()
    while not c.empty():
        elem:tuple[str, int, bool, bool]=c.get()
        caux.put(elem)
        if elem[3]==True:
            colaP.put(elem)
        elif elem[2] == True:
            colaBP.put(elem)
        else:
            colaResto.put(elem)

    #impresora(colaP)
    #impresora(colaBP)
    #impresora(colaResto)

    while not colaP.empty():
        res.put(colaP.get())
    while not colaBP.empty():
        res.put(colaBP.get())
    while not colaResto.empty():
        res.put(colaResto.get())
    while not caux.empty():
        c.put(caux.get())
     
    return res 


c=Cola()
c.put(("gg",1,True,True))
c.put(("pg",8,True,False))
c.put(("Ug",2,False,True))
c.put(("gg",3,True,True))
c.put(("gE",4,True,True))
c.put(("Kg",5,False,True))
c.put(("Ñg",9,True,False))
c.put(("Dg",11,False,False))
c.put(("Sg",6,True,True))
c.put(("Qg",10,True,False))
c.put(("Vg",7,False,True))

print("la cola res se ve asi =")
f = atencion_a_clientes(c)
impresora(f)


# 3) DICCIONARIOS 

#ej 3.16 agrupar_por_longitud 
def lista_palabras (linea: str) -> list[str]:
    res: list[str] = []
    palabra_en_construccion = ""
    for letra in linea:
        if letra != " " or "\n":
            palabra_en_construccion = palabra_en_construccion + letra
        else:
            if len(palabra_en_construccion) > 0:
                res.append(palabra_en_construccion)
                palabra_en_construccion = ""
    res.append(palabra_en_construccion)
    return res

def agrupar_por_longitud(nombre_archivo : str) -> dict:
    res: dict[int, int] = dict()
    palabras: list [str] = lista_palabras(nombre_archivo)
    for palabra in palabras:
        long: int = len(palabra)
        if long in res.keys():
            res[long] += 1
        else:
            res[long] = 1
    return res

palabras = agrupar_por_longitud("/home/Estudiante/Descargas/hola.txt")
print(palabras)

"""
    archivo: TextIO = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    for linea in lineas:
        for palabra in linea:
            if not len(palabra) in res:
                res [len(palabra)] = 1
            else:
                res [len(palabra)] += 1
    return res
palabras = agrupar_por_longitud("/home/Estudiante/Descargas/hola.txt")
print(palabras)
"""

def obtener_palabras(texto: str) -> list[str]:
    res: list[str] = []
    palabra: str = ""
    for char in texto:
        if char != " " and char != "\n":
            palabra += char
        else:
            if palabra != "":
                res.append(palabra)
            palabra = ""
    if palabra != "":
        res.append(palabra)
    return res
print(agrupar_por_longitud("/home/Estudiante/Descargas/hola.txt"))


#OTRA FORMA DE PENSAR EL 16
def agrupar_por_long (nombre_archivo: str):
    res: dict [int, int] = {}
    archivo = open(nombre_archivo, "r")
    texto: str = archivo.read()
    archivo.close()
    palabras: list [str] = obtener_palabras(texto)
    for palabra in palabras:
        long = len(palabra)
        if long in res.keys():
            res[long] += 1
        else:
            res[long] = 1
    return res




# 4) ARCHIVOS

#ej 4.21 contar_lineas
def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo, "r")
    longitud = archivo.readlines()
    archivo.close()
    return len(longitud)

cant_lineas = contar_lineas("/home/Estudiante/Descargas/hola.txt")
print(cant_lineas)


