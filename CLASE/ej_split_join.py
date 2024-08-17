def separar_por_caracter(cadena, sep): 
    return sep.join(cadena)

def reemplazar(s, a_reemplazar, reemplazo):
    acum = ''
    for c in s:
        if c == a_reemplazar:
            acum += reemplazo
        else:
            acum += c

    return acum

def reemplazar_pro(s,a_r, r): 
    return r.join(s.split(a_r))


