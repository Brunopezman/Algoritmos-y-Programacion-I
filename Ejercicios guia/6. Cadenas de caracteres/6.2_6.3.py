# Escribir funciones que dada una cadena y un caracter:
# - Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'
# - Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_' debería devolver 'mi_archivo_de_texto.txt'
# - Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y debería devolver 'su clave es: XXXX'
# - Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'
# Modificar las funciones anteriores, para que reciban un parámetro que indique la cantidad máxima de reemplazos o inserciones a realizar.

def separar_por_caracter(cadena, caracter, cantidad_reemplazos):

    nueva_cadena = ''
    acumulado = 0

    for letra in cadena[0:-1]:
        if acumulado <= cantidad_reemplazos: 
            acumulado +=1  
            nueva_cadena += letra + caracter
        else:
            nueva_cadena += letra

    nueva_cadena += cadena[-1]

    return nueva_cadena

def replace(cadena, caracter, cantidad_reemplazos):
    
    nueva_cadena = ''
    acumulado = 0

    for letra in cadena:
        
        if letra == ' ':
            acumulado +=1
            if acumulado <= cantidad_reemplazos: 
                nueva_cadena += caracter  
            nueva_cadena += letra
        else:
            nueva_cadena += letra
    return nueva_cadena

def replace_x(cadena, caracter, cantidad_reemplazos):

    nueva_cadena = ''
    acumulado = 0

    for digito in cadena:
        acumulado +=1
        if acumulado <= cantidad_reemplazos:    
            nueva_cadena += caracter
        else:
            nueva_cadena += digito
    
    return nueva_cadena

def cada_tres_digitos(cadena, caracter):

    nueva_cadena = ''
    intervalo = 3
    acumulado = 0

    for digito in cadena:
        if acumulado == intervalo:
            nueva_cadena += caracter
            acumulado += 1
        
        nueva_cadena += digito
        acumulado += 1

    return nueva_cadena


       
