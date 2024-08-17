# Plegado de un texto - Escribir una función que reciba un párrafo de texto (palabras separadas por espacios) y una longitud 𝑛, y devuelva una lista conteniendo líneas de texto de longitud máxima 𝑛. Las líneas deben ser cortadas correctamente en los espacios (sin cortar las palabras). Asumir que ninguna palabra tiene longitud mayor a 𝑛.

def dividir_en_n(s:str,n:int):
    resultado = []
    acumulador = []
    for palabra in s.split():
        if (len(' '.join(acumulador)) + len(palabra)+ 1) > n:
           resultado.append(' '.join(acumulador))
           acumulador = []
        acumulador.append(palabra)
    resultado.append(' '.join(acumulador))
    
    return resultado

print(dividir_en_n('Ayer fui al concierto de Taylor Swift', 12))
        