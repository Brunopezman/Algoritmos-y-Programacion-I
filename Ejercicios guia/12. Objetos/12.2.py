# Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se asignan en el constructor, y se imprimen como X/Y en el método __str__.
# Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción con la suma de ambas.
# Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción con el producto de ambas.
# Crear un método simplificar que modifica la fracción actual de forma que los valores del dividendo y divisor sean los menores posibles.

from math import lcm, gcd

class Fraccion:

    def __init__(self, num, den) -> None:
        if den == 0:
            raise ZeroDivisionError ('No se puede dividir por 0')
        self.num = num
        self.den = den

        #agrego el metodo simplificar para que modifique desde el constructor
        self.simplificar()

    def __str__(self) -> str:
        return f'{self.num}/{self.den}'

    def __add__(self, fraccion) -> int:
        den_fraccion = lcm(self.den, fraccion.den)
        num_fraccion_1 = den_fraccion // self.num * self.num
        num_fraccion_2 = den_fraccion // fraccion.den * fraccion.num

        return fraccion(num_fraccion_1 + num_fraccion_2, den_fraccion)
    
    def __mul__(self, fraccion) -> int:
        num = self.num * fraccion.num
        den = self.den * fraccion.den

        return fraccion(num, den)

    def simplificar(self):
        gcd_fraccion = gcd(self.num, self.den)
        self.num //= gcd_fraccion
        self.den //= gcd_fraccion


num = Fraccion(1,2)
den = Fraccion(3,4)

try:
    fraccion = Fraccion(num,den)
except ValueError as e:
    print('Error: ', e)

try:
    suma = Fraccion(num,den)
except ValueError as e:
    print('Error: ', e)
   
try:
    mul = Fraccion(num,den)
except ValueError as e:
    print('Error: ', e)