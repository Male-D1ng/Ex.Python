#nuevo_ej22.py
"""
# Creamos un diccionario para almacenar el historial de navegación de cada usuario
historiales = {}

# Función para visitar un sitio y agregarlo al historial del usuario
def visitar_sitio(historiales, usuario, sitio):
    if usuario not in historiales:
        historiales[usuario] = []
    historiales[usuario].append(sitio)
    return historiales

# Función para navegar hacia atrás en el historial del usuario
def navegar_atras(historiales, usuario):
    if usuario in historiales and len(historiales[usuario]) > 1:
        historiales[usuario].pop()
    return historiales

# Función para navegar hacia adelante en el historial del usuario
def navegar_adelante(historiales, usuario):
    if usuario in historiales and len(historiales[usuario]) > 1:
        siguiente_sitio = historiales[usuario].pop(0)
        historiales[usuario].append(siguiente_sitio)
    return historiales

# Ejemplo de uso:
historiales = visitar_sitio(historiales, "usuario1", "google.com")
historiales = visitar_sitio(historiales, "usuario1", "facebook.com")

print("Historial de usuario1:", historiales["usuario1"])

historiales = navegar_atras(historiales, "usuario1")
print("Después de navegar hacia atrás:", historiales["usuario1"])

historiales = visitar_sitio(historiales, "usuario2", "youtube.com")
print("Historial de usuario2:", historiales["usuario2"])

historiales = navegar_adelante(historiales, "usuario1")
print("Después de navegar hacia adelante:", historiales["usuario1"])
"""
from queue import LifoQueue as Pila 

dict_aux = dict()

#creo la funcion: visitar sitio(historiales, usuario, sitio)
def visitar_sitio(historialesF:dict, usuarioF:str, sitioF:str) -> dict:
    #{historialesF}: diccionario con el historial de navegacion: keys = nombre_usuario, value = pilas
    #{usuario}: usuarios
    #{sitio}: url del sitio
    #branch = 'defaoult'
    #si el usuario dado esta en el diccionario
    if usuarioF in historialesF.keys():
        #branch = 'esta en dict'
        pila = historialesF[usuarioF]
        pila.append(sitioF)

    #si no existe el usuario en el diccionario
    else:
        #branch = 'no esta en el dict'
        pila : Pila = []
        #pila = historialesF[usuarioF]
        pila.append(sitioF)
        historialesF.update({usuarioF:pila})
        
    print('visitar_sitio')
    for usuario,sitio in historialesF.items():
        print ("el susuario: " , usuario, ", entro al sitio: " , sitio , ", cant. elem: ",len(sitio))

    #devuelvo el diccionario
    return historialesF

def print_dict (d:dict):
    for usuario,sitio in d.items():
        print ("el susuario: " , usuario, ", entro al sitio: " , sitio , ", cant. elem: ",len(sitio))
    

def navegar_atras (historiales, usuario)-> dict:
    #consigo la pila con los sitios
    pila_sitio = historiales[usuario]
    #guardo el ultimo elemnto de la pila
    sitio = pila_sitio[-1]
    visitar_sitio(dict_aux,usuario,sitio)
    #elimino el ultimo elem de la pila
    pila_sitio.pop()
    print('navegar_atras')
    for usuario,sitio in historiales.items():
        print ("el susuario: " , usuario, ", entro al sitio: " , sitio , ", cant. elem: ",len(sitio))
    #print_dict("devuelve en navegar_atras: ",historiales)


def navegar_adelante (historiales, usuario)-> dict:
    #consigo la pila del dic aux con los sitios
    pila_sitio = dict_aux[usuario]
    #guardo el ultimo elemnto de la pila
    sitio = pila_sitio[-1]
    visitar_sitio(historiales,usuario,sitio)
    pila_sitio.pop()
    print('navegar_adelante')
    for usuario,sitio in historiales.items():
        print ("el susuario: " , usuario, ", entro al sitio: " , sitio , ", cant. elem: ",len(sitio))