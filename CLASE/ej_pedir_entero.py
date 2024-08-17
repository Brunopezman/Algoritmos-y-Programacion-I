def pedir_entero():

    while True:
        n = input('Dame un numero entero: ')
        if n.isdigit() or (n[1:].isdigit() and n[0] == '-'):
            return int(n)

pedir_entero()

# Ahora con excepciones

def pedir_entero():

    n = input('Ingrese un numero entero: ')

    if not n.isdigit():
        raise TypeError('La entrada no es un numero')

    return int(n)

def main():

    try:
        pedir_entero()
    except TypeError:
        print('La entrada no es un numero')
    except:
        return