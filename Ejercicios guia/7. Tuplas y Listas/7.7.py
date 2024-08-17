# Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido.

def id(datos_personales:list[tuple]):
    '''Recibe una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido. '''

    info_persona = ''
    listado_personas = []
    
    for i in range(len(datos_personales)):
        apellido = datos_personales[i][0]
        nombre = datos_personales[i][1]
        Inicial_segundo_nombre = datos_personales[i][2]

        info_persona = nombre + ' ' + Inicial_segundo_nombre+'.' + ' ' + apellido
        listado_personas.append(info_persona)
    
    return listado_personas
