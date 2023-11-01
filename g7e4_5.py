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

def monedero () -> list[tuple(str,int)]:
    monto : int= 0
    tipo_carga : str= ''
    historial: list = []
    while tipó_carga != 'x':
         tipo_carga = input("OPERACION A REALIZAR: ")
        if tipo_carga == "C":
            saldo = int(input("MONTO: "))
            monto += saldo
            historial.append((tipo_carga, saldo))
        elif tipo_carga == "D":
            saldo = int(input("MONTO: "))
            monto = monto - saldo
            historial.append((tipo_carga, saldo))
    return historial

#ej1_simulacro

def ultima_aparicion(s: list, e: int) -> int:
    s : list = []
    e : int 
    for i in range (len (s),-1):
        if s[-1] == e:
            return i




