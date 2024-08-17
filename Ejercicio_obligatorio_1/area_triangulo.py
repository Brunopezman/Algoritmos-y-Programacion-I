from vectores import norma, prodvect, diferencia

def area_triangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    """Recibe las cordenadas de 3 puntos distintos y les aplica las funciones norma, prodvect, diferencia del modulo vectores.py para calcular el area del triangulo."""
    
    x_base, y_base, z_base = diferencia(x1,y1,z1,x2,y2,z2)
    x_altura, y_altura, z_altura = diferencia(x1,y1,z1,x3,y3,z3)
    x, y, z  = prodvect(x_base, y_base, z_base, x_altura, y_altura, z_altura)
    area = norma(x, y, z) / 2

    return area

print("Area triangulo 1: "+ str(area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0)))
print("Area triangulo 2: "+ str(area_triangulo(6, 8, -1, -3, 4, 4, -3, 6, 0)))
print("Area triangulo 3: "+ str(area_triangulo(5, 8, -2, -2, 4, 6, -3, 4, 0)))
