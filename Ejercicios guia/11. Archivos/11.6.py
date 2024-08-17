# Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave y el segundo como valor.
# Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo, con el formato clave, valor.

def cargar_archivo(path):
    notas = {}

    with open(path) as f:
        for linea in f:
            nota_alumno = linea.split(',')
            notas[nota_alumno[0]] = nota_alumno[1].rstrip()

    return notas

def guardar_archivo(path, dict):

    with open(path, 'w') as destino:
        for clave, valor in dict.items():
            linea = f'{clave}, {valor}\n'
            destino.write(linea)
            
 