# Escribir funciones que permitan:

# - Calcular el perímetro de un rectángulo dada su base y su altura.
def perimetro_rectangulo(lado1, lado2):
    """
        Recibe dos INT, los multiplica a ambos por 2, luego los suma.
    """
    
    return lado1*2 + lado2*2

# - Calcular el área de un rectángulo dada su base y su altura.
def area_rectangulo(base, altura):
    """
        Recibe dos INT, los multiplica a ambos por 2, luego los suma.
    """
    return base * altura

# - Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2.
def area_rectangulo2(x1:int,x2:int,y1:int,y2:int):
    base = x2 - x1  
    altura = y2 - y1  

    return base * altura

# - Calcular el perimetro de un círculo dado su radio.
def area_circulo(d):
    pi = 3.14159

    return pi * d

# - Calcular el área de un círculo dado su radio.
def area_circulo(r):
    pi = 3.14159

    return pi * (r**2)

# - Calcular el volumen de una esfera dado su radio.
def volumen_esfera(r):
    pi = 3.14159

    return (4/3)* pi * (r**3)

# - Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
def hipotenusa(c1,c2):

    h = (c1**2 + c2**2)**0.5 
    
    return h

def mostrar_coords(columnas, filas):

    for f in range(filas):
        for c in range(columnas):
            print(str(f)+ ','+ str(c), end=' ')
        print()


mostrar_coords(3, 4)
