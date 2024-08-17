# Crear una clase Vector, que en su constructor reciba una lista de elementos que serán sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
# Implementar el método __add__ que reciba otro vector, verifique si tienen la misma cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la misma cantidad de elementos debe levantar una excepción
# Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con los elementos multiplicados por ese número.

class Vector:

    def __init__(self, coords) -> None:
        
        self.coords = coords

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise 'Deben tener la misma dimension'
        
        nuevas_coords = []

        c1 = self.coords
        c2 = other.coords

        for i in range(len(c1)):
            nuevas_coords.append(c1[i] + c2[i])
        
        return Vector(nuevas_coords)
    
    def __mul__(self, n):

        coords = []
        for i in self.coords:
            coords.append(i*n)
        
        return Vector(coords)
    
    def __str__(self) -> str:
        return self.coords
