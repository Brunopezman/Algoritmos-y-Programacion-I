# Escribir funciones que permitan encontrar:
# - El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y c), indicando si es un máximo o un mínimo.
# - Las raíces (reales o complejas) de un polinomio de segundo grado. Nota: validar que las operaciones puedan efectuarse antes de realizarlas.
# - La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta). Nota: validar que no sean dos rectas con la misma pendiente.

def encontrar_max_min(a, b, c):
    # Calcula el punto critico del polinomio a través de despejar 0 = 2ax + b
    punto_critico = -b / (2 * a)

    while a == 0:
        print("a debe ser distinto de 0")
        a = float(input("Ingrese un valor para a: "))
    
    # Calcula el valor del polinomio en el punto crítico
    valor_en_punto_critico = a * punto_critico**2 + b * punto_critico + c
    
    # Determina si es un máximo o mínimo usando el coeficiente 'a'
  
    es_maximo = True if a < 0 else False
    if es_maximo == True:
        print('Es un Maximo')
    else:
        print('Es un minimo')

    return print(f"Punto critico: {punto_critico} Valor: {valor_en_punto_critico}")

def raices(a,b,c):

    while a == 0:
        print("a debe ser distinto de 0")
        a = float(input("Ingrese un valor para a: "))
       
    discriminante = b**2 - 4 * a * c

    while discriminante < 0 :
        print("No tiene raices racionales")
        a = float(input("Ingrese un valor para a: "))
        b = float(input("Ingrese un valor para b: "))
        c = float(input("Ingrese un valor para c: "))

        discriminante = b**2 - 4 * a * c

    raiz_1 = (-b + (discriminante ** 0.5))/(2*a)
    raiz_2 = (-b - (discriminante ** 0.5))/(2*a)

    return print(f"Raíces: {raiz_1, raiz_2}")


def interseccion_rectas(a,b,c,d):
    
    # recta_1 : y = a*x + b
    # recta_2 : y = c*x + d

    while a == c:
        print("Los valores de a y c deben ser distintos")
        a = float(input("Ingrese otro valor para a: "))
        b = float(input("Ingrese un valor para b: "))
        c = float(input("Ingrese otro valor para c: "))
        d = float(input("Ingrese un valor para d: "))

    x = (d - b)/(a - c)
    y = a * (d - b)/(a - c) + b

    return print(x,y)

def imprimir_opciones():

    print("-"*10)
    print("Menu de Opciones:")
    print("a. Raices")
    print("b. Encontrar los maximos y minimos de un polinomio")
    print("c. Interseccion de rectas")
    print("d. Salir")
    print("-"*10)

def valor_invalido(valor, valores_validos):
    return valor not in valores_validos

def seleccionar_opcion():

    imprimir_opciones()
    
    opt = input("Seleccione una opcion: ")

    while valor_invalido(opt, ['a','b', 'c', 'd']):
        opt = input(f'La opcion {opt} es invalida. Por favor, seleccione una opcion válida: ')
    
    return opt

def main():
    
    print("-"*10)
    print("Math Calculator")
    print("-"*10)

    print("Elija un valor para a, b, c y d: ")
    a = float(input("Ingrese un valor para a: "))
    b = float(input("Ingrese un valor para b: "))
    c = float(input("Ingrese un valor para c: "))
    d = float(input("Ingrese un valor para d: "))

    print("-"*10)
    print("Elija una operacion para realizar: ")

    opt = seleccionar_opcion()

    while opt != 'd':
        if opt == 'a':
            raices(a,b,c)
        elif opt == 'b':
            encontrar_max_min(a, b, c)
        elif opt == 'c':
            interseccion_rectas(a,b,c,d)
        
        opt = seleccionar_opcion()
    
    return

main()