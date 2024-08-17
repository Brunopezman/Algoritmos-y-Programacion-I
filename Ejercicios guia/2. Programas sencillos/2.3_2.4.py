# Escribir una función que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5C + 32

def farenheit_a_celcius(f):
    c = round((5/9)*f - (5/9*32),1)

    return c

# Escribir un programa que utilice la función anterior para generar una tabla de conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.

def tabla_grados_celcius():
    for f in range(10,130,10):
        print(str(f)+ "ºF",end=" son ")
        print(farenheit_a_celcius(f))
        


