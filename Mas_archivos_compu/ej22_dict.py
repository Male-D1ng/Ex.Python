#ej22_dict.py

from queue import LifoQueue as Pila

""" 
Crear un navegador web que lleve un registro de los sitios web visitados por los usuarios del sistema.
El navegador debe permitir al usuario navegar hacia atr´as y hacia adelante en la historia de navegaci´on.
1. Crea un diccionario llamado historiales que almacenar´a el historial de navegaci´on para cada usuario.
Las claves del diccionario ser´an los nombres de usuario y los valores ser´an pilas.
2. Implementa una funci´on llamada visitar sitio(historiales, usuario, sitio) que reciba el diccionario de historiales,
el nombre de usuario y el sitio web visitado. 
La funci´on debe agregar el sitio web al historial del usuario correspondiente.
3. Implementa una funci´on llamada navegar atras(historiales, usuario) que permita al usuario navegar hacia atr´as en
la historia de navegaci´on. 
Esto implica sacar el sitio web m´as reciente del historial del usuario.
4. Implementa una funci´on llamada navegar adelante(historiales, usuario) que permita al usuario navegar hacia adelante 
en la historia de navegaci´on. Esto implica volver a agregar el sitio web previamente sacado."""

"""historiales : dict = {}

def visitar_sitio (historiales: dict [str,(Pila,Pila)], usuario: str, sitio:str)-> dict:
    #la clave/keys del diccionario es justo usuario
    if usuario in historiales.keys():
   #los valores q son pilas se van a llenar con 1° el usuario, 2° los sitios
        historiales[usuario][0].put(sitio)"""

"""
# Creamos una lista para simular una pila que almacena el historial de navegación
historial = []

# Función para visitar un sitio y agregarlo al historial
def visitar_sitio(sitio):
    historial.append(sitio)

# Función para navegar hacia atrás en el historial
def navegar_atras():
    if len(historial) > 1:
        # Sacamos el sitio más reciente de la lista (pila)
        sitio_actual = historial.pop()
        # El sitio sacado se considera el "nuevo sitio actual"
        # No se vuelve a agregar al historial

# Función para navegar hacia adelante en el historial
def navegar_adelante():
    if historial:
        # Sacamos el sitio actual de la lista (pila)
        sitio_actual = historial.pop()
        # Lo volvemos a agregar para simular la navegación hacia adelante
        historial.append(sitio_actual)

# Ejemplo de uso:
visitar_sitio("sitio1")
visitar_sitio("sitio2")

print("Historial:", historial)

navegar_atras()
print("Después de navegar hacia atrás:", historial)

navegar_adelante()
print("Después de navegar hacia adelante:", historial) """

# 22
historiales = dict()

def visitar_sitio(historiales: dict[str, (Pila, Pila)], usuario:str, sitio: str) -> dict:
    if usuario in historiales.keys():
        historiales[usuario][0].put(sitio)
    else:
        historiales[usuario] = (Pila(), Pila())
        historiales[usuario][0].put(sitio)

    return historiales

def navegar_atras(historiales: dict[str,(Pila,Pila)],usuario:str) -> dict:
    sitio_atras = historiales[usuario][0].get()
    historiales[usuario][1].put(sitio_atras)
    return historiales[usuario][0].queue

def navegar_adelante(historiales: dict[str,(Pila,Pila)], usuario : str) -> dict:
    sitio_adelante = historiales[usuario][1].get()
    historiales[usuario][0].put(sitio_adelante)
    return historiales[usuario][0].queue

visitar_sitio(historiales,'martin','netflix.com')
print(historiales)
visitar_sitio(historiales,'martin','apple.com')
print(navegar_atras(historiales, 'martin'))
visitar_sitio(historiales, 'martin','youtube.com')
print(navegar_adelante(historiales,'martin'))