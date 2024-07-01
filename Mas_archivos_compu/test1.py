from queue import Queue as Cola

def orden_de_atencion(urgentes: Cola, postergables: Cola) -> Cola[int]:
    res, conservar_urg, conservar_post = crear_colas()

    while not urgentes.empty():
        agregar_elem_a_resultado_y_recordar(urgentes, res, conservar_urg)
        agregar_elem_a_resultado_y_recordar(postergables, res, conservar_post)
        
    reconstruir_colas_originales(urgentes, postergables, conservar_urg, conservar_post)

    return res

def crear_colas():
    res: Cola[int] = Cola()
    conservar_urg: Cola[int] = Cola()
    conservar_post: Cola[int] = Cola()
    return res,conservar_urg,conservar_post

def reconstruir_colas_originales(urgentes, postergables, conservar_urg, conservar_post):
    while (not conservar_urg.empty()):   
        urgentes.put(conservar_urg.get())
        postergables.put(conservar_post.get())

def agregar_elem_a_resultado_y_recordar(cola_entrada, resultado, cola_conservar):
    urg = cola_entrada.get()
    cola_conservar.put(urg)
    resultado.put(urg)

urgentes = Cola()
postergables = Cola()
urgentes = urgentes.put([-1])
postergables = postergables.put([1])

print(orden_de_atencion(urgentes.queue,postergables.queue))

