def imprimir_estrellas(n):
    if n == 0:
        #caso base
        return 
    
    # caso recursivo - Hacer la minima unidad de esfuerzo para acercarme al caso base
    print('*')
    imprimir_estrellas(n - 1)


def factorial_iterativa(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r

def factorial_recursivo(n):
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)    

def potencia_iterativa(b, n):
    r = 1
    for i in range(1, n + 1):
        r = r * b 
    return r

def potencia_recursiva(b,n):
    if n == 0:
        return 1 
    if n % 2 == 0:
        r = potencia_recursiva(b, n//2)
        return r * r
    else:
        r = potencia_recursiva(b, (n - 1)//2)
        return r * r
    
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

def _buscar(L, x, izq, der):
    if izq > der:
        return -1
    med = len(L) // 2
    if L[med] == x:
        return med
    if L[med] > x:
        return _buscar(L, x, izq, med - 1)
    else:
        return _buscar(L, x, med + 1, der)

def buscar(L, x):
    return _buscar(L, x, 0, len(L) - 1)

def producto_entre_posiciones(lista):
    i = 0
    return _producto_entre_posiciones(lista, i)

def _producto_entre_posiciones(lista, i):

    if len(lista) == 0:
        return []
    
    e = lista[i]

    if i == 0:
        producto = e
    else:
        producto = e * lista[i - 1]

    return [producto] + _producto_entre_posiciones(lista, i + 1)

lista = [3,4,2,1,0,6]

productos = producto_entre_posiciones(lista)

print(productos)