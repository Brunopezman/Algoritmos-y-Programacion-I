# Escribir una función que reciba las coordenadas de un vector en ℝ3 (x,y,z) y devuelva la norma del vector.

def norma(x, y, z):
    return (x**2 + y**2 + z**2)**0.5

# Escribir una función que reciba las coordenadas de dos vectores en ℝ3 (x1,y1,z1,x2,y2,z2) y devuelva las coordenadas del vector diferencia (debe devolver 3 valores numéricos).

def vector_diferencia(x1,y1,z1,x2,y2,z2):
    return (x2-x1),(y2-y1),(z2-z1)

# Escribir una función que reciba las coordenadas de dos vectores en ℝ3 y devuelva las coordenadas del producto vectorial.

def producto_vectorial(x1,y1,z1,x2,y2,z2):
    return print((y1*z2 - y2*z1), (x1*z2 - x2*z1), (x1*y2 - x2*y1))

# Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de 3 puntos en ℝ3 y devuelva el área del triángulo que conforman.

def area_triangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3):

    x, y, z = vector_diferencia(x1,y1,z1,x2,y2,z2)
    base = norma(x, y, z)
    x, y, z = vector_diferencia(x1,y1,z1,x3,y3,z3)
    altura = norma(x, y, z)

    return (base*altura)/2

# Escribir una función que reciba las coordenadas de 4 puntos en el plano ℝ2 (x1,y1,x2,y2,x3,y3,x4,y4) que conforman un cuadrilátero convexo, y devuelva el área del mismo.

def vector_diferencia_2(x1,y1,z1,x4,y4,z4):
    return (x4-x1),(y4-y1),(z4-z1)

def area_triangulo_2(x1,y1,z1,x2,y2,z2,x4,y4,z4):

    x, y, z = vector_diferencia(x1,y1,z1,x2,y2,z2)
    base = norma(x, y, z)
    x, y, z = vector_diferencia(x1,y1,z1,x4,y4,z4)
    altura = norma(x, y, z)

    return (base*altura)/2

def area_cuadrilatero(x1,y1,x2,y2,x3,y3,x4,y4):

    area_1 = area_triangulo(x1,y1,0,x2,y2,0,x3,y3,0)
    area_2 = area_triangulo_2(x1,y1,0,x2,y2,0,x4,y4,0)

    return print(area_1 + area_2)

area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5)