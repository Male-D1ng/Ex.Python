#ej4: input
def estudiantes ()-> [str]:
    res:list =[]
    nombre:str = ''
    while nombre != 'listo':
        nombre = input()
        print ("pasar un nombre")
        res.append(nombre)
    return res 

estudiantes()

#ej monedero

#def monedero () -> list[tuple(str,int)]:
#    monto : int= 0
#    carga : str= ''
#    while carga != 'x':

#ej1_simulacro

def ultima_aparicion(s: list, e: int) -> int:
    s : list = []
    e : int 
    for i in range (len (s),-1):
        if s[-1] == e:
            return i




