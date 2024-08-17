# Escribir un programa que vaya solicitando al usuario que ingrese nombres:
# - Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# - Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena ”*”, para salir del programa.

def agendar_nombres():

    agenda = {}
    nombre = input('Ingrese nombre: ')
    while not nombre == '*':
        if not nombre in agenda:
            telefono = input('Ingrese el telefono: ')
            agenda[nombre] = [telefono]
        else:
            print(agenda[nombre])
        
        nombre = input('Ingrese nombre: ')
        
    return agenda

agendar_nombres()

