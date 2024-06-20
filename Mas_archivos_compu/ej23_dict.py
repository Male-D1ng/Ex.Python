#ej23_dict.py
#FORMA DIRECTA, NO USA NI KEYS NI VALUES NI ITEMS
#DIRECTAMENTE ACCEDE A LOS ELEMENTOS DEL DICCIONARIOS CON LAS LLAVES 
#UNA VEZ QUE DEFINO EN AGREGAR_PRODUCTO QUE PRECIO Y CANTIDAD SON CLAVES,
# PUEDO ACCEDER A ELLAS Y AGREGAR CUANTO VALEN
""" DEF : Se puede acceder a sus elementos con [] o también con la función
        Para modificar un elemento basta con usar [] con el nombre del key 
        y asignar el valor que queremos.
        Si el key al que accedemos no existe, se añade automáticamente A LO ULTIMO."""
# 23
inventario = {}
def agregar_producto(inventario: dict, nombre:str, precio:float, cantidad: int) -> dict:
    inventario[nombre] = {'precio': precio, 'cantidad': cantidad} #declaro el dict
    return inventario

def actualizar_stock(inventario, nombre, cantidad) -> dict:
    inventario[nombre]['cantidad'] = cantidad
    return inventario

def actualizar_precios(inventario,nombre,precio) -> dict:
    inventario[nombre]['precio'] = precio
    return inventario

def calcular_valor_inventario(inventario) -> float:
    total = 0
    for producto in inventario:
        total += float(inventario[producto]['precio']) * float(inventario[producto]['cantidad'])
    return total


item1 = input ("el item1 es: ")
precio1 = input ("el item1 vale: ")
cantidad1 = input ("cantidad del item1: ")
item2 = input ("el item2 es: ")
precio2 = input("el item2 vale: ")
cantidad2 = input ("cantidad del item2: ")
agregar_producto(inventario, item1, precio1, cantidad1)
agregar_producto(inventario, item2, precio2, cantidad2) 
print("el inventario es: ", inventario)
print("el valor del inventario es : ", calcular_valor_inventario(inventario))
nombre = input("Actualizo el stock de ")
cantidad = input ("Ahora tengo: ")
print("ahora el stock es :", actualizar_stock(inventario,nombre,cantidad))
precio = input ("Ahora valen: ")
actualizar_precios(inventario,nombre,float(precio))
print("el valor del inventario es : ", calcular_valor_inventario(inventario))

