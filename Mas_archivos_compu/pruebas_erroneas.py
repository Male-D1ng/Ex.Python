#pruebas_erroneas.py
#otra forma de poner comentarios = """ bloque cod """

#EJ6_PARTE_A

def palabras_legibles(nombre_archivo: str) -> list:
    palabrasLegibles = []
    f = open(nombre_archivo, mode="rb")
    palabra = ""
    for lines in f.readlines():
        for letter in lines:
            letter = chr(letter)
            if (letter.isalpha() == True) or (letter.isalnum() == True) or (letter == "_") or (letter == " "):
                palabra += letter
            else:
                if len(palabra) >= 5:
                    palabrasLegibles.append(palabra)
                palabra = ""
    f.close()
    return palabrasLegibles

# print(palabras_legibles('binary.wav'))


"""esta mal : if len(fila)==4 and fila[0]==lu:
            nota = float(fila[3])  # La nota es la cuarta columna (índice 3)
            total_notas += nota
            cantidad_notas += 1
            legajo = fila[0]
            # Calcular el promedio final  
            for libreta,nota_total in d.items():
                libreta = legajo
                nota_total = promedio
    if cantidad_notas > 0:
        promedio = total_notas / cantidad_notas
        return d"""

